package model

import (
	"fmt"
	_ "time"
	"encoding/json"
	"github.com/garyburd/redigo/redis"
	"go_code/chatsys/common"
)

//完成一些初始化工作，比如 MyUserDao, 这个后面需要
//操作Redis的时候，会使用到
var (
	MyUserDao *UserDao
)

type UserDao struct {
	pool *redis.Pool
}

//一个工厂模式，获取到一个UserDao 变量(实例)
func NewUserMgr(pool *redis.Pool) (userDao *UserDao) {

	userDao = &UserDao{
		pool: pool,
	}
	return
}

func (ud *UserDao) getUser(conn redis.Conn, id int) (user *common.User, err error) {

	result, err := redis.String(conn.Do("HGet", "users", fmt.Sprintf("%d", id)))

	fmt.Printf("result=%v\n", result)
	//如果对应的用户id,返回  ErrUserNotExist
	if err != nil {
		
		if err == redis.ErrNil {
			err = ErrUserNotExist
		}
		return
	}
	//声明一个 *User
	user = &common.User{}
	//将user 进行反序列化，并返回反序列化后的user实例
	err = json.Unmarshal([]byte(result), user)
	if err != nil {
		fmt.Printf("xxx~=%v\n", err)
		return
	}
	fmt.Printf("从数据库得到的user=%v", user)
	return
}

//完成登录操作，到Redis验证
//1.如果登录的用户信息有效，则返回一个User实例
//2.如果登录的用户信息无效，则返回一个nil 和 对应的自定义错误信息
func (ud *UserDao) Login(id int, passwd string) (user *common.User, err error) {

	//得到一个链接
	conn := ud.pool.Get()
	//defer关闭链接
	defer conn.Close()

	//通过id来获取对应的用户信息，注意在
	//getUser 方法中，已经封装好了user
	user, err = ud.getUser(conn, id)
	if err != nil {
		return
	}

	//比较通过id查询到的用户密码是否和登录的密码一种
	//如果不一致，则返回一个 ErrInvalidPasswd 信息
	if user.Pwd != passwd {
		err = ErrInvalidPasswd
		return
	}

	//user.Status = common.UserStatusOnline
	//user.LastLogin = fmt.Sprintf("%v", time.Now())

	return
}

//在服务器端完成注册
func (ud *UserDao) Register(user *common.User) (err error) {

	//得到一个链接
	conn := ud.pool.Get()
	//defer关闭链接
	defer conn.Close()

	_, err = ud.getUser(conn, user.Id)
	if err == nil { //如果获取到一个用户，说明该用户存在了
		err = ErrUserExist //用户存在了...
		return
	}

	//序列化这个user
	data, err := json.Marshal(user)
	if err != nil {
		return
	}
	//存入数据库
	_, err = conn.Do("HSet", "users", fmt.Sprintf("%d", user.Id), string(data))
	if err != nil {
		return
	}
	return
}