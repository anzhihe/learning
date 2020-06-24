package main

import "fmt"

func main() {
	for i := 0; i <= 19; i++ {
		fmt.Printf("%3d: %04o\n", i, i)
	}

	fmt.Printf("Decimal   1: %3d Octal   01: %2d\n", 1, 01)
	fmt.Printf("Decimal  10: %3d Octal  010: %2d\n", 10, 010)
	fmt.Printf("Decimal 100: %3d Octal 0100: %2d\n", 100, 0100)

	fmt.Printf("%09b\n", 0007)
	fmt.Printf("%09b\n", 0070)
	fmt.Printf("%09b\n", 0700)
}
