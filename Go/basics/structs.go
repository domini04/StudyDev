// A Struct is a collection of fields.
// Corresponds to a class in other languages.
package main

import "fmt"

type Book struct {
	title string
	author string
	year int
}


func main() {
	book := Book{"The Great Gatsby", "F. Scott Fitzgerald", 1925} 
	book.title = "A Different Title" 
	fmt.Println(book)

	//Struct Pointers
	p := &book
	p.title = "A Different Title Again"
	fmt.Println(book)

	//Struct Literals
	book2 := Book{title: "The Great Gatsby", author: "F. Scott Fitzgerald", year: 1925}
	fmt.Println(book2)
}	