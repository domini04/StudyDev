package main

import "fmt"

// An array is a numbered sequence of elements of a single type with a fixed length.
// an array in go cannot be resized
func main() {
	var a [5]int // An array of 5 integers
	fmt.Println("emp:", a)

	//array slicing
	b := a[2:4] //array slices are like references to arrays
	b[0] = 10
	fmt.Println("a:", a)

	//capacity of array : the number of elements in the array or slice
	fmt.Println("cap:", cap(a))

	//length of array : the number of elements referred to by the slice
	fmt.Println("len:", len(a))

	//capacity vs. length : capacity is the number of elements in the underlying array (5)
	//length is the number of elements referred to by the slice (2)
	s := []int{2, 3, 5, 7, 11, 13}
	printSlice(s)

	// Slice the slice to give it zero length.
	s = s[:0] // the capacity of the slice remains the same
	printSlice(s)

	// Extend its length.
	s = s[:4]
	printSlice(s)

	// Drop its first two values.
	s = s[2:] // this reduces the capacity of the slice
	printSlice(s)

	c := make([]int, 5) // len(s)=5, cap(s)=5
	printSlice(c)
}

func printSlice(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}