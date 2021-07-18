package process

import (
	_ "encoding/binary"
	"encoding/json"
	_ "errors"
	"fmt"
	"go_code/chatsys/common"
	"go_code/chatsys/server/utils"
	"go_code/chatsys/server/model"
	"net"
)

//UserProcessor.go 相当于一个控制器,装用于处理与用户相关的
//同时每登录一个用户，就对应一个UserProcessor的实例,
//因此也可以看做是登录的用户
type UserProcessor struct {
	Conn   net.Conn
	userId int //用户的id
	Buf    [8192]byte
}

func (up *UserProcessor) NotifyOthersUserOnline(userId int) {
	//得到当前所有在线用户
	users := clientMgr.GetAllUsers()
	for id, client := range users {
		if id == userId {
			//过滤掉自己...
			continue
		}
		//注意这里的一个client,就是*UserProcessor实例
		//每个*UserProcessor,都有自己维护的conn
		//每取出一个当前在线用户，就通知这个在线用户，userId
		//这个用户上线了
		client.NotifyUserOnline(userId)
	}
}

func (up *UserProcessor) NotifyUserOnline(userId int) {

	// 构建通知用户上线响应消息包
	var respMsg   common.Message
	respMsg.Type = common.UserStatusNotifyMesType //类型为用户上线响应包类型
	var userStatusNotifyMes common.UserStatusNotifyMes

	userStatusNotifyMes.UserId = userId
	userStatusNotifyMes.Status = common.UserStatusOnline

	data, err := json.Marshal(userStatusNotifyMes)
	if err != nil {
		fmt.Println("marshal failed, ", err)
		return
	}

	respMsg.Data = string(data)
	data, err = json.Marshal(respMsg)
	if err != nil {
		fmt.Println("marshal failed, ", err)
		return
	}

	//因为要返回消息包给客户端，因此创建一个Transfer实例
	tf := &utils.Transfer{
		Conn : up.Conn,
	}
	err = tf.ServerWritePackage(data)
	if err != nil {
		fmt.Println("send msg包 failed, ", err)
		return
	}
	return

}

func (up *UserProcessor) ServerProcessLogin(msg *common.Message) (err error) {

	//对msg.Data进行反序列化，得到用户名和密码

	var loginMes common.LoginMes
	err = json.Unmarshal([]byte(msg.Data), &loginMes)
	if err != nil {
		fmt.Println("unmarshal failed, err=", err)
		return
	}
	//fmt.Printf("id=%v pwd=%v\n", loginMes.Id, loginMes.Pwd)

	// 构建登录响应消息包
	var resMsg   common.Message
	resMsg.Type = common.LoginResMesType //类型为登录响应包类型
	var loginResMes common.LoginResMes

	//暂时不到Redis去验证
	//规则，如果输入的id为 100, 密码为 123456 则登录成功
	//否则, 登录失败
	//返回登录成功的消息包

	/*
	if loginMes.Id == 100 && loginMes.Pwd == "123456" {
		loginResMes.Code = 200
	} else {
		//返回登录失败的消息包
		loginResMes.Code = 500 //500表示没有这个用户
	}
	*/

	//现在改成到Redis中去验证用户是否存在
	//规则，用户id和密码都正确 则登录成功
	//否则, 登录失败
	//返回登录的响应消息包 

	//userDao这个变量，在main函数运行就已经被初始化了，是一个全局变量
	//Login如果成功，err为nil,同时会返回一个 User 变量
	var user *common.User
	user, err = model.MyUserDao.Login(loginMes.Id, loginMes.Pwd)
	if err != nil {
		//这里还可以加入到底是哪种登录的错误信息，然后返回不同的Code码值
		fmt.Printf("登录有错误，错误信息为%v\n", err)
		loginResMes.Code = 500 
		//return
	} else {
		//没有错误
		//这里我们输出一下这个user信息
		fmt.Printf("登录成功了, 从Redis得到的用户信息是%v\n", user)
		loginResMes.Code = 200
	}

	//登录成功后,将当前登录的用户加入到在线用户列表中(切片)
	clientMgr.AddClient(loginMes.Id, up)
	up.userId = loginMes.Id

	//当前用户[loginMes.Id]登录成功后，需要通知其它用户，我上线了
	up.NotifyOthersUserOnline(loginMes.Id)

	//登录成功后，还需要将当前在线用户列表(id),加入到
	//返回包的User切片中  loginResMes.User
	userMap := clientMgr.GetAllUsers()
	for userId, _ := range userMap {
		loginResMes.User = append(loginResMes.User, userId)
	}

	

	//序列化返回消息data，便于网络传输
	data, err := json.Marshal(loginResMes)
	if err != nil {
		fmt.Println("marshal failed, err=", err)
		return
	}
	//将序列化后的返回消息data，放到resMsg的Data字段
	resMsg.Data = string(data)
	//再对resMsg序列化化便于传输
	data, err = json.Marshal(resMsg)
	if err != nil {
		fmt.Println("marshal failed, ", err)
		return
	}
	fmt.Println("返回的package包=%", string(data))
	//因为要返回消息包给客户端，因此创建一个Transfer实例
	tf := &utils.Transfer{
		Conn : up.Conn,
	}
	err = tf.ServerWritePackage(data)
	if err != nil {
		fmt.Println("send msg包 failed, ", err)
		return
	}
	return 	
}

//处理用户注册嘻嘻
func (up *UserProcessor) ServerProcessRegister(msg *common.Message) (err error) {

	//对msg.Data进行反序列化，得到用户名和密码

	var registerMes common.RegisterMes
	err = json.Unmarshal([]byte(msg.Data), &registerMes)
	if err != nil {
		fmt.Println("unmarshal failed, err=", err)
		return
	}
	//fmt.Printf("id=%v pwd=%v\n", loginMes.Id, loginMes.Pwd)

	// 构建注册响应消息包
	var resMsg   common.Message
	resMsg.Type = common.RegisterResMesType //类型为注册响应包类型
	var registerResMes common.RegisterResMes


	//userDao这个变量，在main函数运行就已经被初始化了，是一个全局变量
	//Register如果成功，err == nil 
//	var user *model.User
//	err = model.MyUserDao.Register(registerMes.User.Id, 
//		registerMes.User.Name, registerMes.User.Pwd)

	err = model.MyUserDao.Register(&registerMes.User)
	if err != nil {
		fmt.Printf("注册用户, 用户id已经占用 err=%v\n", err)
		registerResMes.Code = 100 
		//return
	} else {
		//没有错误
		fmt.Printf("注册成功了...")
		registerResMes.Code = 200
	}
	//序列化返回消息data，便于网络传输
	data, err := json.Marshal(registerResMes)
	if err != nil {
		fmt.Println("marshal failed, err=", err)
		return
	}
	//将序列化后的返回消息data，放到resMsg的Data字段
	resMsg.Data = string(data)
	//再对resMsg序列化化便于传输
	data, err = json.Marshal(resMsg)
	if err != nil {
		fmt.Println("marshal failed, ", err)
		return
	}
	//因为要返回消息包给客户端，因此创建一个Transfer实例
	tf := &utils.Transfer{
		Conn : up.Conn,
	}
	err = tf.ServerWritePackage(data)
	if err != nil {
		fmt.Println("send msg包 failed, ", err)
		return
	}
	return 
	
}