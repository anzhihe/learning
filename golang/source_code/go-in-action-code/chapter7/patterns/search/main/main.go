// This sample program demonstrates how to implement a pattern for
// concurrent requesting results from different systems and either
// wait for all the results to return or just the first one.
package main

import (
	"log"

	"github.com/goinaction/code/chapter7/patterns/search"
)

// main is the entry point for all Go programs.
func main() {
	// Submit the search and display the results.
	results := search.Submit(
		"golang",
		search.OnlyFirst,
		search.Google,
		search.Bing,
		search.Yahoo,
	)

	for _, result := range results {
		log.Printf("main : Results : Info : %+v\n", result)
	}

	// This time we want to wait for all the results.
	results = search.Submit(
		"golang",
		search.Google,
		search.Bing,
		search.Yahoo,
	)

	for _, result := range results {
		log.Printf("main : Results : Info : %+v\n", result)
	}
}
