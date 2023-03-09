package main

import "fmt"

func main() {
	var year, pageNumber int
	var grade float32

	publisher := "Star Books"
	writer := "Leo Tolstoy"
	artist := "Gustave Doré"
	title := "Anna Karenina"
	year = 1877
	pageNumber = 2000
	grade = 0.9

	fmt.Println(title, "written by", writer, "drawn by", artist)
	fmt.Println("It was published by", publisher, "in", year)
	fmt.Println("It has", pageNumber, "pages")
	fmt.Println("It has a grade of", grade)

	//switch the details to a different book
	title = "The Great Gatsby"
	writer = "F. Scott Fitzgerald"
	artist = "Francis Cugat"
	year = 1925
	pageNumber = 180
	grade = 0.8
	
	fmt.Println("=====================================")
	fmt.Println(title, "written by", writer, "drawn by", artist)
	fmt.Println("It was published by", publisher, "in", year)
	fmt.Println("It has", pageNumber, "pages")
	fmt.Println("It has a grade of", grade)

}