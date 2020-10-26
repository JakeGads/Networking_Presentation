func csvReader() {
	// 1. Open the file
	recordFile, err := os.Open("./records.csv")
	if err != nil {
	 fmt.Println("An error encountered ::", err)
	}  // 2. Initialize the reader
	reader := csv.NewReader(recordFile)  // 3. Read all the records
	records, _ := reader.ReadAll()  // 4. Iterate through the records as you wish
	fmt.Println(records)
}