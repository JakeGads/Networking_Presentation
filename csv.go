package main

import (
	"encoding/csv"
	"fmt"
	"net/http"
)

func main() {
	csvReader()
}

func csvReader() {
	// I couldn't get my csv to function correctly
	url := "https://raw.githubusercontent.com/mledoze/countries/master/dist/countries.csv"
	resp, err := http.Get(url)
	if err != nil {
		fmt.Println("Encountered an error in dl", err)
		return
	}

	defer resp.Body.Close()
	reader := csv.NewReader(resp.Body)
	reader.Comma = ','
	data, err := reader.ReadAll()
	if err != nil {
		fmt.Println("Encountered an error in file", err)
		return
	}

	fmt.Println(data)
}
