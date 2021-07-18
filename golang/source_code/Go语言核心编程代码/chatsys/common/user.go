package common

//使用常量，表示用户的状态 
//1 表示在线
//2 表示离线 
//3 这里使用iota 来自动增长
const (
	UserStatusOnline  = 1
	UserStatusOffline = iota
)


//一个用户信息的结构体
type User struct {
	Id     int    `json:"userId"`
	Name   string `json:"userName"`
	Pwd string `json:"userPwd"`
	//后续可以加入的字段
	// Nick      string `json:"nick"`
	// Sex       string `json:"sex"`
	// Header    string `json:"header"`
	// LastLogin string `json:"last_login"`
	Status    int    `json:"status"`
}
