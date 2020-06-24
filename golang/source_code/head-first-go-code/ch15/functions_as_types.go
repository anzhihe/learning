package main

import "fmt"

func sayHi() {
	fmt.Println("Hi")
}

func doMath(passedFunction func(int, int) float64) {
	result := passedFunction(10, 2)
	fmt.Println(result)
}

func divide(a int, b int) float64 {
	return float64(a) / float64(b)
}
func multiply(a int, b int) float64 {
	return float64(a * b)
}

func main() {
	doMath(divide)
	doMath(multiply)
}
