package main

import (
	"bytes"
	"fmt"
	"log"
	"os"
)

type Pos struct {
	x int
	y int
}

type Guard struct {
	dir byte
	pos Pos
}

var input []byte
var width, height int
var rotate = map[byte]byte{ '^' : '>', '>' : 'v', 'v' : '<', '<' : '^' }
var grid map[Pos]byte

func parse() {
	data, err := os.ReadFile("day06.txt")
	
	if err != nil {
		log.Fatal(err)
	}

	input = bytes.ReplaceAll(data, []byte("\n"), []byte(""))

	lines := bytes.Split(bytes.Trim(data, "\n"), []byte("\n"))

	width  = len(lines[0])
	height = len(lines)

	for row, line := range lines {
		for col, ch := range line {
			grid[Pos{col, row}] = ch
		}
	}
}

func getguard() Guard {
	idx := bytes.IndexByte(input, byte('^'))
	return Guard{byte('^'), Pos{ idx % height, idx / height} }
}

func nextpos(guard Guard) Pos {
	x := guard.pos.x
	y := guard.pos.y
	
	switch guard.dir {
	case '^':
		return Pos{x, y-1}
	case '>':
		return Pos{x+1, y}
	case 'v':
		return Pos{x, y+1}
	case '<':
		return Pos{x-1, y}
	default:
		panic(fmt.Errorf("invalid dir %d", guard.dir))
	}
}

func move(guard Guard) (Guard, bool) {
	g		 := guard.dir
	pos  := guard.pos
	pos2 := nextpos(guard)

	if pos2.x >= 0 && pos2.x < width && pos2.y >= 0 && pos2.y < height {
		if grid[pos2] == '#' {
			return Guard{rotate[g], pos}, true
		} else {
			return Guard{g, pos2}, true
		}
	} else {
		return Guard{}, false
	}
}

func pathpositions(guard Guard) (map[Pos]bool, bool) {
	history := make(map[Guard]bool)
	ok := true

	for ok && !history[guard] {
		history[guard] = true
		guard, ok = move(guard)
	}

	positions := make(map[Pos]bool)

	for g, _ := range history {
		positions[g.pos] = true
	}
	
	return positions, ok
}

func part1(guard Guard) int {
	positions, _ := pathpositions(guard)
	return len(positions)
}

func part2(guard Guard) int {
	iscycle := func(guard Guard, pos Pos) bool {
		grid[pos] = '#'
		_, cycle := pathpositions(guard)
		delete(grid, pos)
		return cycle
	}

	total := 0
	positions, _ := pathpositions(guard)

	for pos, _ := range positions {
		if iscycle(guard, pos) {
			total += 1
		}
	}

	return total
}

func main() {
	fmt.Printf("begin\n")
	grid = make(map[Pos]byte, 20000)
	parse()
	guard := getguard()
	//	move(guard)
	nextpos(guard)
	fmt.Printf("part 1 = %d\n", part1(guard))
	fmt.Printf("part 2 = %d\n", part2(guard))
}
