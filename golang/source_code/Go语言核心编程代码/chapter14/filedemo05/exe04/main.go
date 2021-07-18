package main
import (
	"fmt"
	"bufio"
	"os"
	"io" 
)

func main() {
	
	//打开一个存在的文件，将原来的内容读出显示在终端，并且追加5句"hello,北京!"
	//1 .打开文件已经存在文件, d:/abc.txt
	filePath := "d:/abc.txt"
	file, err := os.OpenFile(filePath, os.O_RDWR | os.O_APPEND, 0666)
	if err != nil {
		fmt.Printf("open file err=%v\n", err)
		return 
	}
	//及时关闭file句柄
	defer file.Close()

	//先读取原来文件的内容，并显示在终端.
	reader := bufio.NewReader(file)
	for {
		str, err := reader.ReadString('\n')
		if err == io.EOF { //如果读取到文件的末尾
			break
		}
		//显示到终端
		fmt.Print(str)
	}


	//准备写入5句 "你好,尚硅谷!"
	str := "hello,北京!\r\n" // \r\n 表示换行
	//写入时，使用带缓存的 *Writer
	writer := bufio.NewWriter(file)
	for i := 0; i < 5; i++ {
		writer.WriteString(str)
	}
	//因为writer是带缓存，因此在调用WriterString方法时，其实
	//内容是先写入到缓存的,所以需要调用Flush方法，将缓冲的数据
	//真正写入到文件中， 否则文件中会没有数据!!!
	writer.Flush()

}