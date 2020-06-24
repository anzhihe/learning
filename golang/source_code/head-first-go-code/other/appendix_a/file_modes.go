package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Printf("%09b %s\n", 0000, os.FileMode(0000))
	fmt.Printf("%09b %s\n", 0111, os.FileMode(0111))
	fmt.Printf("%09b %s\n", 0222, os.FileMode(0222))
	fmt.Printf("%09b %s\n", 0333, os.FileMode(0333))
	fmt.Printf("%09b %s\n", 0444, os.FileMode(0444))
	fmt.Printf("%09b %s\n", 0555, os.FileMode(0555))
	fmt.Printf("%09b %s\n", 0666, os.FileMode(0666))
	fmt.Printf("%09b %s\n", 0777, os.FileMode(0777))
}
