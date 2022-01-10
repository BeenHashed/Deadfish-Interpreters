package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	accumulator := 0
	file := os.Args[1]
	code, err := ioutil.ReadFile(file)
	if err != nil {
		fmt.Println("File couldn't be found")
	}
	for _, v := range code {
		if accumulator >= 256 || accumulator < 0 {
			accumulator = 0
		}

		switch string(v) {
		case "i":
			accumulator++
		case "d":
			accumulator--
		case "s":
			accumulator *= accumulator
		case "o":
			fmt.Printf("%v ", accumulator)
		}

	}
}
