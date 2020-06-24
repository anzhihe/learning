package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {

	asciiString := "ABCDE"
	utf8String := "БГДЖИ"

	fmt.Println("Byte lengths:")
	fmt.Println(len(asciiString))
	fmt.Println(len(utf8String))

	fmt.Println("Rune lengths:")
	fmt.Println(utf8.RuneCountInString(asciiString))
	fmt.Println(utf8.RuneCountInString(utf8String))

	fmt.Println("Slice operator on bytes:")
	asciiBytes := []byte(asciiString)
	utf8Bytes := []byte(utf8String)
	asciiBytesPartial := asciiBytes[3:]
	utf8BytesPartial := utf8Bytes[3:]
	fmt.Println(string(asciiBytesPartial))
	fmt.Println(string(utf8BytesPartial))

	fmt.Println("Slice operator on runes:")
	asciiRunes := []rune(asciiString)
	utf8Runes := []rune(utf8String)
	asciiRunesPartial := asciiRunes[3:]
	utf8RunesPartial := utf8Runes[3:]
	fmt.Println(string(asciiRunesPartial))
	fmt.Println(string(utf8RunesPartial))

	fmt.Println("Range on bytes:")
	for index, currentByte := range asciiBytes {
		fmt.Printf("%d: %s\n", index, string(currentByte))
	}
	for index, currentByte := range utf8Bytes {
		fmt.Printf("%d: %s\n", index, string(currentByte))
	}

	fmt.Println("Range on string:")
	for position, currentRune := range asciiString {
		fmt.Printf("%d: %s\n", position, string(currentRune))
	}
	for position, currentRune := range utf8String {
		fmt.Printf("%d: %s\n", position, string(currentRune))
	}
}
