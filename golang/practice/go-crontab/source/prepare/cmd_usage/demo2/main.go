package main

import (
	"os/exec"
	"fmt"
)

func main() {
	var (
		cmd *exec.Cmd
		output []byte
		err error
	)

	// 生成Cmd
	cmd = exec.Command("C:\\cygwin64\\bin\\bash.exe", "-c", "/usr/bin/python xxx.py")

	// 执行了命令, 捕获了子进程的输出( pipe )
	if output, err = cmd.CombinedOutput(); err != nil {
		fmt.Println(err)
		return
	}

	// 打印子进程的输出
	fmt.Println(string(output))
}