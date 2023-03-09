// Go has pointers. A pointer holds the memory address of a value. (Not the value itself.)
// The type *T is a pointer to a T value. Its zero value is nil.

package main

import "fmt"

func main() {
	var p *int // p, of type *int, points to an int

	i := 42
	p = &i // & operator generates a pointer to its operand.  thus p points to i

	fmt.Println(p) 
	fmt.Println(*p) // read i through the pointer

	*p = 21 // set i through the pointer
	fmt.Println(i) // this is called "dereferencing" or "indirecting"
}