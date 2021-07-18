package main
import (
	"fmt"
	"net"
	"time"
	"go_code/chatroom/server/model"
)


// func readPkg(conn net.Conn) (mes message.Message, err error) {

// 	buf := make([]byte, 8096)
// 	fmt.Println("读取客户端发送的数据...")
// 	//conn.Read 在conn没有被关闭的情况下，才会阻塞
// 	//如果客户端关闭了 conn 则，就不会阻塞
// 	_, err = conn.Read(buf[:4])
// 	if err != nil {
// 		//err = errors.New("read pkg header error")
// 		return
// 	}
// 	//根据buf[:4] 转成一个 uint32类型
// 	var pkgLen uint32
// 	pkgLen = binary.BigEndian.Uint32(buf[0:4])
// 	//根据 pkgLen 读取消息内容
// 	n, err := conn.Read(buf[:pkgLen])
// 	if n != int(pkgLen) || err != nil {
// 		//err = errors.New("read pkg body error")
// 		return 
// 	}
// 	//把pkgLen 反序列化成 -> message.Message
// 	// 技术就是一层窗户纸 &mes！！
// 	err = json.Unmarshal(buf[:pkgLen], &mes)
// 	if err != nil {
// 		fmt.Println("json.Unmarsha err=", err)
// 		return 
// 	}
// 	return 
// }

// func writePkg(conn net.Conn, data []byte) (err error) {

// 	//先发送一个长度给对方
// 	var pkgLen uint32
// 	pkgLen = uint32(len(data)) 
// 	var buf [4]byte
// 	binary.BigEndian.PutUint32(buf[0:4], pkgLen)
// 	// 发送长度
// 	n, err := conn.Write(buf[:4])
// 	if n != 4 || err != nil {
// 		fmt.Println("conn.Write(bytes) fail", err)
// 		return 
// 	}

// 	//发送data本身
// 	n, err = conn.Write(data)
// 	if n != int(pkgLen) || err != nil {
// 		fmt.Println("conn.Write(bytes) fail", err)
// 		return 
// 	}
// 	return 
// }

// //编写一个函数serverProcessLogin函数， 专门处理登录请求
// func serverProcessLogin(conn net.Conn, mes *message.Message) (err error) {
// 	//核心代码...
// 	//1. 先从mes 中取出 mes.Data ，并直接反序列化成LoginMes
// 	var loginMes message.LoginMes
// 	err = json.Unmarshal([]byte(mes.Data), &loginMes) 
// 	if err != nil {
// 		fmt.Println("json.Unmarshal fail err=", err)
// 		return 
// 	}
// 	//1先声明一个 resMes
// 	var resMes message.Message
// 	resMes.Type = message.LoginResMesType
// 	//2在声明一个 LoginResMes，并完成赋值
// 	var loginResMes message.LoginResMes
// 	//如果用户id= 100， 密码=123456, 认为合法，否则不合法
	
// 	if loginMes.UserId == 100 && loginMes.UserPwd == "123456" {
// 		//合法
// 		loginResMes.Code = 200
		
// 	} else {
// 		//不合法
// 		loginResMes.Code = 500 // 500 状态码，表示该用户不存在
// 		loginResMes.Error = "该用户不存在, 请注册再使用..."
// 	}

// 	//3将 loginResMes 序列化
// 	data, err := json.Marshal(loginResMes)
// 	if err != nil {
// 		fmt.Println("json.Marshal fail", err)
// 		return 
// 	}

// 	//4. 将data 赋值给 resMes
// 	resMes.Data = string(data)

// 	//5. 对resMes 进行序列化，准备发送
// 	data, err = json.Marshal(resMes)
// 	if err != nil {
// 		fmt.Println("json.Marshal fail", err)
// 		return 
// 	}
// 	//6. 发送data, 我们将其封装到writePkg函数
// 	err = writePkg(conn, data)
// 	return 
// }

// //编写一个ServerProcessMes 函数
// //功能：根据客户端发送消息种类不同，决定调用哪个函数来处理
// func serverProcessMes(conn net.Conn, mes *message.Message) (err error) {

// 	 switch mes.Type {
// 		 case message.LoginMesType :
// 			//处理登录登录
// 			err = serverProcessLogin(conn, mes)
// 		 case message.RegisterMesType :
// 			//处理注册
// 		 default :
// 			fmt.Println("消息类型不存在，无法处理...")
// 	 }
// 	 return 
// }

//处理和客户端的通讯
func process(conn net.Conn) {
	//这里需要延时关闭conn
	defer conn.Close()
	
	//这里调用总控, 创建一个
	processor := &Processor{
		Conn : conn,
	}
	err := processor.process2()
	if err != nil {
		fmt.Println("客户端和服务器通讯协程错误=err", err)
		return 
	}
}

func init() {
	//当服务器启动时，我们就去初始化我们的redis的连接池
	initPool("localhost:6379", 16, 0, 300 * time.Second)
	initUserDao()
}

//这里我们编写一个函数，完成对UserDao的初始化任务
func initUserDao() {
	//这里的pool 本身就是一个全局的变量
	//这里需要注意一个初始化顺序问题
	//initPool, 在 initUserDao
	model.MyUserDao = model.NewUserDao(pool)
}

func main() {
	
	//提示信息
	fmt.Println("服务器[新的结构]在8889端口监听....")
	listen, err := net.Listen("tcp", "0.0.0.0:8889")
	defer listen.Close()
	if err != nil {
		fmt.Println("net.Listen err=", err)
		return 
	}
	//一旦监听成功，就等待客户端来链接服务器
	for {
		fmt.Println("等待客户端来链接服务器.....")
		conn, err := listen.Accept()
		if err != nil {
			fmt.Println("listen.Accept err=" ,err)
		}

		//一旦链接成功，则启动一个协程和客户端保持通讯。。
		go process(conn)
	}
}