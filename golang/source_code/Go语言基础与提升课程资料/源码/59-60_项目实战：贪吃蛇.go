package main

import (
	Clib "CLib"
	"fmt"
	"math/rand"
	"os"
	"time"
)

//游戏界面大小
const WIDE = 20
const HIGH = 20

//分数
var score = 0

//坐标父类
type Postion struct {
	X int
	Y int
}

//蛇 类型
type Snake struct {
	pos  [WIDE * HIGH]Postion //坐标位置（坐标点 20*20）
	size int
	dir  byte
}

//偏移量
var dx = 0
var dy = 0

//食物的父类
type Food struct {
	Postion
}

var food Food //具体的食物
//绘制界面
func DrawUI(p Postion, ch byte) {
	Clib.GotoPostion(p.X*2+4, p.Y+2) //打印出的位置区域（40*20）形成视觉的正方形；所以 x方向是：2倍的x，偏移4；y的偏移为2
	fmt.Fprintf(os.Stderr, "%c", ch) //格式化到控制台
}
func (s *Snake) Init() {
	s.size = 2 //蛇的长度为2
	//初始化蛇的坐标位置
	s.pos[0].X = WIDE / 2 //蛇头的横坐标
	s.pos[0].Y = HIGH / 2 //蛇头的纵坐标
	s.pos[1].X = WIDE/2 - 1
	s.pos[1].Y = HIGH / 2
	//初始化蛇的方向
	//U 上 L 左 R 右 D 下 P 暂停
	s.dir = 'R'
	// 输出初始画面
	fmt.Fprintln(os.Stderr,
		`
  #-----------------------------------------#
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  #-----------------------------------------#
`)
	//食物初始化
	food = Food{Postion{rand.Intn(WIDE), rand.Intn(HIGH)}}
	DrawUI(food.Postion, '#')
	showScore(false)
	go func() {
		for {
			switch Clib.Direction() {
			//方向上：  W、w、↑
			case 72, 87, 119:
				s.dir = 'U'
			//方向左： L、 l 、 ←
			case 65, 97, 75:
				s.dir = 'L'
				//方向右：R、r、→
			case 100, 68, 77:
				s.dir = 'R'
				//方向下:D、d、↓
			case 83, 115, 80:
				s.dir = 'D'
				//暂停  空格键
			case 32:
				s.dir = 'P'
			}
		}
	}()
}
func (s *Snake) PlayGame() {
	for {
		time.Sleep(time.Second / 3)
		if s.dir == 'P' {
			continue
		}
		//蛇头和墙的碰撞判断
		if s.pos[0].X < 0 || s.pos[0].X > WIDE || s.pos[0].Y < 0 || s.pos[0].Y > HIGH {
			Clib.GotoPostion(0, 23)
			return
		}
		//蛇头和身体碰撞
		for i := 1; i < s.size; i++ {
			if s.pos[0].X == s.pos[i].X && s.pos[0].Y == s.pos[i].Y {
				Clib.GotoPostion(0, 23)
				return
			}
		}
		//蛇和食物的碰撞
		if s.pos[0].X == food.X && s.pos[0].Y == food.Y {
			s.size++                                               //蛇的长度加1
			score++                                                //分数加1
			showScore(false)                                       //显示分数
			food = Food{Postion{rand.Intn(WIDE), rand.Intn(HIGH)}} //生成新的食物
			DrawUI(food.Postion, '#')

		}
		//方向的控制
		switch s.dir {
		case 'U':
			dx = 0
			dy = -1
		case 'L':
			dx = -1
			dy = 0
		case 'R':
			dx = 1
			dy = 0
		case 'D':
			dx = 0
			dy = 1
		}
		//将移动的蛇显示到界面中
		lp := s.pos[s.size-1]
		for i := s.size - 1; i > 0; i-- {
			s.pos[i] = s.pos[i-1]
			DrawUI(s.pos[i], '*')
		}
		DrawUI(lp, ' ')
		s.pos[0].X += dx
		s.pos[0].Y += dy
		DrawUI(s.pos[0], '@')

	}
}
func main() {
	Clib.HideCursor()                //去掉控制台光标
	rand.Seed(time.Now().UnixNano()) //创建随机数种子
	var s Snake
	s.Init()
	s.PlayGame()
	showScore(true)
	time.Sleep(time.Second * 20)
}

//显示分数，参数isEnd代表游戏是否结束
func showScore(isEnd bool) {
	Clib.GotoPostion(60, 6)
	if isEnd {
		fmt.Println("游戏已经结束，最后得分为：", score)
	} else {
		fmt.Println("当前得分为：", score)
	}
}
