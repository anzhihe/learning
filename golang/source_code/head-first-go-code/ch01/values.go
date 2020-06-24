package main

import "fmt"

func main() {
	fmt.Println("Strings:")
	fmt.Println("Hello, Go!")
	fmt.Println("Hello,\nGo!")
	fmt.Println("Hello,\tGo!")
	fmt.Println("Quotes: \"\"")
	fmt.Println("Backslash: \\")

	fmt.Println("Runes:")
	fmt.Println('A')
	fmt.Println('B')
	fmt.Println('Җ')
	fmt.Println('\t')
	fmt.Println('\n')
	fmt.Println('\\')

	fmt.Println("Booleans:")
	fmt.Println(true)
	fmt.Println(false)

	fmt.Println("Numbers:")
	fmt.Println(42)
	fmt.Println(3.1415)

	fmt.Println("Math operations:")
	fmt.Println(1 + 2)
	fmt.Println(5.4 - 2.2)
	fmt.Println(3 * 4)
	fmt.Println(7.5 / 5)

	fmt.Println("Comparisons:")
	fmt.Println(4 < 6)
	fmt.Println(4 > 6)
	fmt.Println(2+2 == 5)
	fmt.Println(2+2 != 5)
	fmt.Println(4 <= 6)
	fmt.Println(4 >= 4)
}
