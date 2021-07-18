package process
import (
	"net"
	"go_code/chatsys/common"
	"go_code/chatsys/client/utils"
	"fmt"
	"os"
	"encoding/json"
	"encoding/binary"
)

//UserProcessor.go 相当于一个控制器,装用于处理与用户相关的
type UserProcessor struct {
	//Conn   net.Conn
	//Buf    [8192]byte
}

func (up *UserProcessor) Register(userId int, passwd string, userName string) (err error) {
	
	//链接到Redis
	conn, err := net.Dial("tcp", "localhost:8889")
	if err != nil {
		fmt.Println("Error dialing", err.Error())
		return
	}
	//关闭链接
	//defer conn.Close()
	
	var msg common.Message
	//这个指定消息的种类...
	msg.Type = common.RegisterMesType
	var registerMes common.RegisterMes

	registerMes.User.Id = userId
	registerMes.User.Name = userName
	registerMes.User.Pwd = passwd

	//将registerMes序列化，便于网络传输
	data, err := json.Marshal(registerMes)
	if err != nil {
		return
	}

	//将注册用户的内容(data), 放入到msg的Data字段
	msg.Data = string(data)
	data, err = json.Marshal(msg)
	if err != nil {
		return
	}

	var buf [4]byte
	//这个是消息的长度
	packLen := uint32(len(data))
	binary.BigEndian.PutUint32(buf[0:4], packLen)

	//先发送消息的长度,便于服务器接收
	n, err := conn.Write(buf[:])
	if err != nil || n != 4 {
		fmt.Println("write data  failed")
		return
	}
	//发送消息给服务器
	_, err = conn.Write([]byte(data))
	if err != nil {
		return
	}
	//....

	//读服务器返回的消息包
	//因为要读取服务器返回的消息包，因此创建一个Transfer实例
	tf := &utils.Transfer{
		Conn : conn,
	}
	msg, err = tf.ClientReadPackage()
	if err != nil {
		fmt.Println("readPackage failed, err=", err)
	}

	var registerResMes common.RegisterResMes
	//通过反序列化，得到返回消息的 Data字段的内容
	json.Unmarshal([]byte(msg.Data), &registerResMes)
	if registerResMes.Code == 200 {
		fmt.Println("注册成功了...")
		os.Exit(0)
	}
	if registerResMes.Code == 100 {
		fmt.Println("用户id已经存在，请重新注册...")
		os.Exit(0)
	}
	return

}


func (up *UserProcessor) Login(userId int, passwd string) (err error) {
	
	//链接到Redis
	conn, err := net.Dial("tcp", "localhost:8889")
	if err != nil {
		fmt.Println("Error dialing", err.Error())
		return
	}

	var msg common.Message
	//这个指定消息的种类...
	msg.Type = common.LoginMesType

	var loginMes common.LoginMes
	loginMes.Id = userId
	loginMes.Pwd = passwd

	//将loginMes序列化，便于网络传输
	data, err := json.Marshal(loginMes)
	if err != nil {
		return
	}
	//将消息的内容(data), 放入到msg的Data字段
	msg.Data = string(data)
	//对msg序列化,然后再序列化
	data, err = json.Marshal(msg)
	if err != nil {
		return
	}

	var buf [4]byte
	//这个是消息的长度
	packLen := uint32(len(data))
	binary.BigEndian.PutUint32(buf[0:4], packLen)

	//先发送消息的长度,便于服务器接收
	n, err := conn.Write(buf[:])
	if err != nil || n != 4 {
		fmt.Println("write data  failed")
		return
	}
	//发送消息给服务器
	_, err = conn.Write([]byte(data))
	if err != nil {
		return
	}

	//读服务器返回的消息包
	//因为要读取服务器返回的消息包，因此创建一个Transfer实例
	tf := &utils.Transfer{
		Conn : conn,
	}
	msg, err = tf.ClientReadPackage()
	if err != nil {
		fmt.Println("readPackage failed, err=", err)
	}

	var loginResMes common.LoginResMes
	//通过反序列化，得到返回消息的 Data字段的内容
	json.Unmarshal([]byte(msg.Data), &loginResMes)
	if loginResMes.Code == 500 {
		fmt.Println("用户不存在, 请重新先注册新用户，再登录...")
		os.Exit(0)
	}
	if loginResMes.Code == 200 {

		//当登录成功后，我们现实一下当前在线的用户列表
		fmt.Println("在线用户列表如下:")
		for _, v := range loginResMes.User {
			if v == userId { //去掉自己
				continue
			}
			fmt.Println("在线用户id:\t", v)
			//客户端这边需要记录一个在线用户列表信息
			//用户列表信息使用切片保存
			user := &common.User{Id: v}
			//
			onlineUserMap[user.Id] = user
		}
		fmt.Printf("\n\n")

		//fmt.Println("登录成功...")
		//os.Exit(0) //暂时这样测试一把..
		//一旦登录成功，就需要实时的读取服务端发送的消息并处理
		//,因此专门其动一个goroutine
		go ProcessServerMessage(conn)
		//如果登录成功，我们就显示菜单, 并且是循环显示
		for {
			ShowMenu(conn)
		}
	}
	return 
}

