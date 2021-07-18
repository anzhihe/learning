package common

const (
	LoginMesType           	= "LoginMes"
	LoginResMesType       	= "LoginResMes"
	RegisterMesType       	= "RegisterMes"
	RegisterResMesType 		= "RegisterResMes"
	UserStatusNotifyMesType = "UserStatusNotifyMes"
)



//消息结构体，含有两个部分,消息的类别和消息的内容
type Message struct {
	Type  string `json:"type"`
	Data string `json:"data"`
}

//消息种类: LoginMes 登录消息, 包含id和密码 
type LoginMes struct {
	Id     int    `json:"userId"`
	Name   string `json:"userName"`
	Pwd string `json:"userPwd"`
}

//消息种类: LoginResMes 登录返回的消息包, 包含code(int)和错误信息(string)
type LoginResMes struct {
	Code  int    `json:"code"`
	User  []int  `json:"users"`//增加一个切片,返回当前在线用户的id
	Error string `json:"error"`
}

//消息种类: RegisterMes 注册用户信息, 是一个User实例 
type RegisterMes struct {
	User User `json:"user"`
}

//消息种类: RegisterResMes 登录返回的消息包, 包含code(int)和错误信息(string)
//这个RegisterResMes 和  LoginResMes ，其实是可以合并的
//我这里为了比较好阅读，就不合并了，同学们可以自行合并
type RegisterResMes struct {
	Code  int    `json:"code"`
	Error string `json:"error"`
}

//用户状态通知消息
type UserStatusNotifyMes struct {
	UserId int `json:"userId"`
	Status int `json:"userStatus"`
}

