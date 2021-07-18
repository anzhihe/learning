package utils

import (
	"encoding/binary"
	"encoding/json"
	"errors"
	"fmt"
	"go_code/chatsys/common"
	"net"
	"time"
)

//这个结构体，完成对服务器端发送和接收消息包的读取
type Transfer struct {
	Conn   net.Conn
	Buf    [8192]byte
}

func (tf *Transfer) ClientReadPackage() (msg common.Message, err error) {
	//var buf [8192]byte
	n, err := tf.Conn.Read(tf.Buf[0:4])
	if n != 4 {
		err = errors.New("read header failed")
		fmt.Println("如果读取错误, 则休息30秒，再读数据...")
		time.Sleep(time.Second * 30)
		return
	}
	//fmt.Println("read package:", buf[0:4])

	var packLen uint32
	packLen = binary.BigEndian.Uint32(tf.Buf[0:4])

	//fmt.Printf("receive len:%d", packLen)
	n, err = tf.Conn.Read(tf.Buf[0:packLen])
	if n != int(packLen) {
		err = errors.New("read body failed")
		return
	}

	//fmt.Printf("receive data:%s\n", string(buf[0:packLen]))
	err = json.Unmarshal(tf.Buf[0:packLen], &msg)
	if err != nil {
		fmt.Println("unmarshal failed, err:", err)
	}
	return
}
