package main

import (
	"fmt"
	"time"
)

func sendLetters(channel chan string) {
	time.Sleep(1 * time.Second)
	channel <- "a"
	time.Sleep(1 * time.Second)
	channel <- "b"
	time.Sleep(1 * time.Second)
	channel <- "c"
	time.Sleep(1 * time.Second)
	channel <- "d"
}

func main() {
	fmt.Println(time.Now())
	channel := make(chan string, 3)
	go sendLetters(channel)
	time.Sleep(5 * time.Second)
	fmt.Println(<-channel, time.Now())
	fmt.Println(<-channel, time.Now())
	fmt.Println(<-channel, time.Now())
	fmt.Println(<-channel, time.Now())
	fmt.Println(time.Now())
}
