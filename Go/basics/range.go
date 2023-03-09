package main

import "fmt"

func main() {
	//range in Go returns both the index and value of the element. similar to python enumerate
	pow := []int{1, 2, 4, 8, 16, 32, 64, 128}
	for i, v := range pow {
		fmt.Printf("2**%d = %d\n", i, v)

	//either index or value can be ignored with _
	for _, value := range pow {
		fmt.Printf("%d\n", value)
	}

}