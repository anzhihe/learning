package main
import (
	"fmt"
	"reflect"
)
func main() {
	var str string = "tom"   //ok
	fs := reflect.ValueOf(&str) //ok fs -> string
	fs.Elem().SetString("jack") //ok
	fmt.Printf("%v\n", str) // jack
}
