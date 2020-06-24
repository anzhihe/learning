package main

import (
	"log"
	"os"
)

func check(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

func main() {
	options := os.O_WRONLY | os.O_APPEND | os.O_CREATE
	file, err := os.OpenFile("aardvark.txt", options, os.FileMode(0600))
	check(err)
	_, err = file.Write([]byte("amazing!\n"))
	check(err)
	err = file.Close()
	check(err)
}
