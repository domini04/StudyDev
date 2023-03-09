package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

type university struct {
	ID      int    `json:"id"`
	Name    string `json:"name"`
	Ranking int    `json:"ranking"`
	Tuition int    `json:"tuition"`
}

var universities = []university{
	{ID: 1, Name: "MIT", Ranking: 1, Tuition: 50000},
	{ID: 2, Name: "Stanford", Ranking: 2, Tuition: 45000},
	{ID: 3, Name: "Harvard", Ranking: 3, Tuition: 48000},
	{ID: 4, Name: "Cambridge", Ranking: 4, Tuition: 42000},
}

func getUniversities(c *gin.Context) { //gin.Context is a struct that contains the request and response objects
	c.IndentedJSON(http.StatusOK, universities) //Context.IndentedJSON() is a method that formats the JSON response
}

func main() {
	router := gin.Default()
	router.GET("/universities", getUniversities)
	router.Run("localhost:8080")
}