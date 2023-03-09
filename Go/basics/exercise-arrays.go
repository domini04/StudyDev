package main

import "golang.org/x/tour/pic"

func Pic(dx, dy int) [][]uint8 {
	//create a slice of slices
	slice := make([][]uint8, dy)
	for i := range slice {
		slice[i] = make([]uint8, dx)
	}

	//fill the slice of slices
	for i := range slice {
		for j := range slice[i] {
			slice[i][j] = uint8((i + j) / 2)
		}
	}
	return slice
}

func main() {
	pic.Show(Pic)
}
