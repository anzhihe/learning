package process

import (
	"fmt"
	"go_code/chatsys/common"
)

//客户端这边用于维护客户信息的(比如列表)
var onlineUserMap map[int]*common.User = make(map[int]*common.User, 10)
var UserId int

//输出当前在线用户信息列表
func outputUserOnline() {
	fmt.Println("在线用户列表如下:")
	for id, _ := range onlineUserMap {
		if id == UserId {
			continue //过滤掉自己
		}
		fmt.Println("在线用户id:\t", id)
	}
}

//更新客户端 当前在线用户信息列表
//注意： 因为服务器端会返回一个新的登录用户信息包，因此更新返回这个用户的状态即可
//(1) 一种情况是新登录的用户 [加入到 onlineUserMap]
//(2) 一种情况是登录的用户下线了 [更新 ]
func updateUserStatus(userStatusNotifyMes common.UserStatusNotifyMes) {
	
	//看看是否已经在onlineUserMap了
	user, ok := onlineUserMap[userStatusNotifyMes.UserId]
	if !ok {
		//如果不在onlineUserMap,就先创建一个
		user = &common.User{}
		user.Id = userStatusNotifyMes.UserId
	}
	//更新状态[1.在线 2.离线]
	user.Status = userStatusNotifyMes.Status
	//更新onlineUserMap
	onlineUserMap[user.Id] = user
	//输出最新的在线用户列表
	outputUserOnline()
}
