package process

import (
	"encoding/json"
	"fmt"
	"net"
	"os"
	"go_code/chatsys/client/utils"
	"go_code/chatsys/common"
)

func ProcessServerMessage(conn net.Conn) {
	//创建一个tf 来不停的读取信息...
	tf := &utils.Transfer{
		Conn : conn,
	}
	// for {
	// 	fmt.Println("不停的读取从服务器来的信息，并准备处理...")
	// 	msg, err := tf.ClientReadPackage()
	// 	fmt.Println("msg=", msg, "err=", err)
	// }

	//不停的读取从服务器来的信息，并准备处理...
	for {
		msg, err := tf.ClientReadPackage()
		if err != nil {
			fmt.Println("read err:", err)
			fmt.Println("msg=", msg, "err=", err)
			//os.Exit(0)
		}

		var userStatus common.UserStatusNotifyMes
		//反序列化
		err = json.Unmarshal([]byte(msg.Data), &userStatus)
		if err != nil {
			fmt.Println("unmarshal failed, err:", err)
			return
		}

		switch msg.Type {
			case common.UserStatusNotifyMesType:
				updateUserStatus(userStatus)
		}
	}


}

//显示用户登录成功的可以使用的菜单
func ShowMenu(conn net.Conn) {
	fmt.Println("1. 显示在线用户列表")
	fmt.Println("2. 发送信息")
	fmt.Println("3. 信息列表")
	fmt.Println("4. 退出系统")

	var key int
	fmt.Scanf("%d\n", &key)
	switch key {
	case 1:
		outputUserOnline()
	case 2:
		//enterTalk(conn)
	case 3:
		//listUnReadMsg()
		return
	case 4:
		os.Exit(0)
	}
}

