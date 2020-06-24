package main

import "fmt"

func main() {
	fmt.Printf("false || false == %t\n", false || false)
	fmt.Printf("true  || false == %t\n", true || false)
	fmt.Printf("true  || true  == %t\n", true || true)

	fmt.Printf("%b | %b == %b\n", 0, 0, 0|0)
	fmt.Printf("%b | %b == %b\n", 0, 1, 0|1)
	fmt.Printf("%b | %b == %b\n", 1, 1, 1|1)

	fmt.Printf("%02b\n", 1)
	fmt.Printf("%02b\n", 0)
	fmt.Printf("%02b\n", 1|0)

	fmt.Printf("%02b\n", 2)
	fmt.Printf("%02b\n", 0)
	fmt.Printf("%02b\n", 2|0)

	fmt.Printf("%08b\n", 170)
	fmt.Printf("%08b\n", 15)
	fmt.Printf("%08b\n", 170|15)
}
