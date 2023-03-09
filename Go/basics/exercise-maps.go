package main

import (
	"fmt"
	"strings"
)

func WordCount(s string) map[string]int {
	//create a map
	words := make(map[string]int)
	//split the string into a slice of words
	slice := strings.Fields(s)
	//iterate over the slice and add the words to the map
	for _, word := range slice {
		words[word] += 1
	}
	//print the map
	fmt.Println(words)
	return words
}

func main() {

	WordCount("I am learning Go!")
}

