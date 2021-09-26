package main

import (
	"os/exec"
	"context"
	"time"
	"fmt"
)

type result struct {
	err error
	output []byte
}

func main() {
	//  执行1个cmd, 让它在一个协程里去执行, 让它执行2秒: sleep 2; echo hello;
	// 1秒的时候, 我们杀死cmd
	var (
		ctx context.Context
		cancelFunc context.CancelFunc
		cmd *exec.Cmd
		resultChan chan *result
		res *result
	)

	// 创建了一个结果队列
	resultChan = make(chan *result, 1000)

	// context:   chan byte
	// cancelFunc:  close(chan byte)

	ctx, cancelFunc = context.WithCancel(context.TODO())

	go func() {
		var (
			output []byte
			err error
		)
		cmd = exec.CommandContext(ctx, "C:\\cygwin64\\bin\\bash.exe", "-c", "sleep 2;echo hello;")

		// 执行任务, 捕获输出
		output, err = cmd.CombinedOutput()

		// 把任务输出结果, 传给main协程
		resultChan <- &result{
			err: err,
			output: output,
		}
	}()

	// 继续往下走
	time.Sleep(1 * time.Second)

	// 取消上下文
	cancelFunc()

	// 在main协程里, 等待子协程的退出，并打印任务执行结果
	res = <- resultChan

	// 打印任务执行结果
	fmt.Println(res.err, string(res.output))
}
