package utils

import (
	"fmt"
	"net"
	"go_code/chatsys/common"
	"errors"
	"encoding/binary"
	"encoding/json"
)

//这个结构体，完成对客户端发送和接收消息包的读取
type Transfer struct {
	Conn   net.Conn
	Buf    [8192]byte
}

//读取客户端发送的消息包，并封装到Message
func (transfer *Transfer) ServerReadPackage() (msg common.Message, err error) {

	n, err := transfer.Conn.Read(transfer.Buf[0:4])
	if n != 4 {
		err = errors.New("read header failed")
		return 
	}
	fmt.Println("read package:", transfer.Buf[0:4])

	var packLen uint32
	packLen = binary.BigEndian.Uint32(transfer.Buf[0:4])

	fmt.Printf("receive len:%d", packLen)
	//读取客户端发送的消息包的长度..
	n, err = transfer.Conn.Read(transfer.Buf[0:packLen])
	if n != int(packLen) {
		err = errors.New("read body failed")
		return 
	}

	fmt.Printf("receive data:%s\n", string(transfer.Buf[0:packLen]))
	err = json.Unmarshal(transfer.Buf[0:packLen], &msg)
	if err != nil {
		fmt.Println("unmarshal failed, err:", err)
	}
	return 
}


//发送的消息包给客户端
func (transfer *Transfer) ServerWritePackage(data []byte) (err error) {

	packLen := uint32(len(data))

	binary.BigEndian.PutUint32(transfer.Buf[0:4], packLen)
	n, err := transfer.Conn.Write(transfer.Buf[0:4])
	if err != nil {
		fmt.Println("write data  failed")
		return
	}

	n, err = transfer.Conn.Write(data)
	if err != nil {
		fmt.Println("write data  failed")
		return
	}

	if n != int(packLen) {
		fmt.Println("write data  failed")
		err = errors.New("write data  failed")
		return
	}
	return 
}