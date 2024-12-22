package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func parse(filename string) []int {
	file, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var numbers []int
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		num, err := strconv.Atoi(line)
		if err != nil {
			panic(err)
		}
		numbers = append(numbers, num)
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}

	return numbers
}

func evolve(n int) int {
	n = (n*64 ^ n) % 16777216
	n = (n/32 ^ n) % 16777216
	return (n*2048 ^ n) % 16777216
}

func getChanges(n int) [][2]int {
	prevDigit := n % 10
	changes   := make([][2]int, 0, 2000)

	for i := 0; i < 2000; i++ {
		n         = evolve(n)
		digit    := n % 10
		changes   = append(changes, [2]int{digit, digit - prevDigit})
		prevDigit = digit
	}

	return changes
}

func countSequences(n int) map[[4]int]int {
	changes := getChanges(n)
	d       := make(map[[4]int]int)

	for i := 3; i < len(changes); i++ {
		t := [4]int{ changes[i-3][1], changes[i-2][1], changes[i-1][1], changes[i][1] }
		if _, exists := d[t]; !exists {
			d[t] = changes[i][0]
		}
	}

	return d
}

func part1(input []int) int {
	totalSum := 0

	for _, n := range input {
		for i := 0; i < 2000; i++ {
			n = evolve(n)
		}
		totalSum += n
	}
	return totalSum
}

func part2(input []int) int {
	bananas := make(map[[4]int]int)

	for _, n := range input {
		for t, v := range countSequences(n) {
			bananas[t] += v
		}
	}

	maxValue := 0

	for _, v := range bananas {
		if v > maxValue {
			maxValue = v
		}
	}

	return maxValue
}

func main() {
	if part2(parse("day22.txt")) != 2189 {
		log.Fatalf("Part 2 failed")
	}
}
