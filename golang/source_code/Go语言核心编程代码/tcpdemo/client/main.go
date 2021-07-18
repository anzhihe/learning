package main
import (
	"bufio"
	"fmt"
	"net"
	"os"
	"strings"
)
func main() {

	conn, err := net.Dial("tcp", "localhost:8888")
	if err != nil {
		fmt.Println("Error dialing", err.Error())
		return
	}

	defer conn.Close()
	inputReader := bufio.NewReader(os.Stdin)
	for {
		input, _ := inputReader.ReadString('\n')
		trimmedInput := strings.Trim(input, "\r\n") //去掉空格
		if trimmedInput == "exit" {
			return
		}
		_, err = conn.Write([]byte(trimmedInput + "\n")) //让服务器端换行
		if err != nil {
			return
		}
	}
}
