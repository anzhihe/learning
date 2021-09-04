package main

import (
	"fmt"
	"sort"
)

func main() {

	strs := []string{"c", "a", "b"}
	sort.Strings(strs)
	fmt.Println("Strings:", strs)

	ints := []int{7, 2, 4}
	sort.Ints(ints)
	fmt.Println("Ints:	", ints)

	s := sort.IntsAreSorted(ints)
	fmt.Println("Sorted:	", s)
}
