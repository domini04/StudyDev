package main

import (
	"net/http"

	"github.com/gin-gonic/gin"

	"strconv"
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

func getUniversityByID(c *gin.Context) {
	id := c.Param("id") //Context.Param() returns the value of the URL parameter from Request
	idInt, err := strconv.Atoi(id)
	if err != nil {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"message": "Invalid university ID"})
		return
	}
	//loop through the universities slice
	for _, u := range universities {
		if u.ID == idInt {
			c.IndentedJSON(http.StatusOK, u)
			return
		}
	}
}

func main() {
	router := gin.Default()
	router.GET("/universities", getUniversities)
	router.GET("/universities/:id", getUniversityByID) //:id is a placeholder for the university ID
	router.Run("localhost:8080")                       //run the server on port 8080
}
