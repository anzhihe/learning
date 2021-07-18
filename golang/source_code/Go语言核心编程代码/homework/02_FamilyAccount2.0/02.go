// 01
package main

import (
	"fmt"
	"strconv"

	"github.com/garyburd/redigo/redis"
)

type FamilySystem struct {
	k       int
	Datails string
	Money   float64
	Total   float64
	loop    bool
}

func (f *FamilySystem) Menu() {
	for {
		fmt.Print(`----------------家庭收入系统----------------
		1.账户明细
		2.登记收入
		3.登记支出
		4.退出系统
		5.保存数据退出
		6.恢复账户明细
请输入选项(1-4):`)
		fmt.Scanln(&f.k)
		switch f.k {
		case 1:
			fmt.Println("收支\t账户金额\t收支金额\t说明")
			fmt.Println(f.Datails)
		case 2:
			fmt.Println("本次收入金额")
			fmt.Scanln(&f.Money)
			f.Total += f.Money
			fmt.Println("本次收入说明")
			var note string
			fmt.Scanln(&note)
			f.Datails += fmt.Sprintf("收入\t%v\t\t%v\t\t%v\n", f.Total, f.Money, note)
			fmt.Println("------------------存入成功------------------")
		case 3:
			fmt.Println("本次支出金额")
			fmt.Scanln(&f.Money)
			f.Total -= f.Money
			fmt.Println("本次支出说明")
			var note string
			fmt.Scanln(&note)
			f.Datails += fmt.Sprintf("支出\t%v\t\t%v\t\t%v\n", f.Total, f.Money, note)
			fmt.Println("------------------支出成功------------------")
		case 4:
			for {
				var char string
				fmt.Println("你确定退出吗?请输入y/n")
				fmt.Scanln(&char)
				if char == "y" || char == "Y" {
					f.loop = false
					break
				} else if char == "n" || char == "N" {
					break
				}
			}
		case 5:
			//连接到redis
			conn, err := redis.Dial("tcp", "127.0.0.1:6379")
			defer conn.Close()
			if err != nil {
				fmt.Println(err)
				return
			}
			_, err = conn.Do("hmset", "FamilyAccount", "Datails", 
				f.Datails, "Money", f.Money, "Total", f.Total)
			if err != nil {
				fmt.Println("存储失败", err)
				return
			}
		case 6:
			conn, err := redis.Dial("tcp", "127.0.0.1:6379")
			defer conn.Close()
			if err != nil {
				fmt.Println(err)
				return
			}
			r, err := redis.Strings(conn.Do("hmget", "FamilyAccount", "Datails", 
				"Money", "Total"))
			if err != nil {
				fmt.Println("读取失败", err)
				return
			}
			f.Datails = r[0]
			f.Money, _ = strconv.ParseFloat(r[1], 64)
			f.Total, _ = strconv.ParseFloat(r[2], 64)
		default:
			fmt.Println("请输入正确的选项")
		}
		if f.loop == false {
			break
		}
	}
}

func main() {
	var fs FamilySystem
	fs = FamilySystem{0, "", 0, 10000, true}
	fs.Menu()
	fmt.Println("退出系统成功...")
}
