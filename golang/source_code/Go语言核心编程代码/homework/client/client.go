package main
import (
	"fmt"
	"net"
	"bufio"
	"os"
	"strings"
)

func main() {
	conn, err := net.Dial("tcp", "localhost:8888")
	if err != nil {
		fmt.Println("net.Dial err = ", err)
		return
	}
	//功能：客户端可以发送单行数据,然后就退出
	//os.Stdin 代表标准输入[终端]
	reader := bufio.NewReader(os.Stdin)
	for {
		//从终端读取一行用户输入，并准备发送给服务器
		line, err := reader.ReadString('\n')
		if err != nil {
			fmt.Println("reader.ReaderString err = ", err)
		}
		//如果用户输入的是 exit 就退出
		line = strings.Trim(line, " \r\n")
		if line ==  "exit" {
			fmt.Println("客户端退出")
			return
		}

		//再将 line 发送给服务器
		_, err = conn.Write([]byte(line ))
		if err != nil {
			fmt.Println("conn.Write err = ", err)
		}

	}
	// fmt.Print("客户端发送了%d字节的数据,并退出", n)
}