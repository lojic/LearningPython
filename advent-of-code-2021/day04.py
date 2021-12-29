# Port of my Racket solution:
# https://github.com/lojic/LearningRacket/blob/master/advent-of-code-2021/solutions/day04/day04.rkt
from advent import *

order, *boards = parse(4, ints, sep="\n\n")
dim = 5

def part1():
    return solve(lambda xs: xs[0], boards)

def part2():
    return solve(lambda xs: xs[-1], boards)

def cols(board):
    """Return a list of board columns"""
    return [[ get(board, row, col) for row in range(dim) ] for col in range(dim) ]

def get(board, row, col):
    """Return the value at board[row, col]"""
    return board[ row * dim + col ]

def is_winning(board):
    """Indicate whether the board is a winning board"""
    return any([ not any(lst) for lst in (rows(board) + cols(board)) ])

def mark_board(n, board):
    """Functionally mark the board by replacing any values equal to n with #f"""
    return [ False if i == n else i for i in board ]

def mark_boards(n, boards):
    """Return a new list of boards that have been marked"""
    return [ mark_board(n, board) for board in boards ]

def rows(board):
    """Return a list of board rows"""
    return [[ get(board, row, col) for col in range(dim) ] for row in range(dim) ]

def solve(accessor, boards):
    """Associate numbers with a list of boards the number caused to
       win. Then simply choose either the first board from the first
       number, or the last board from the last number according to the part
       via the accessor function which is either first or last."""
    n, boards = accessor(winning_numbers(order, boards))
    return n * sum_unmarked(accessor(boards))

def sum_unmarked(board):
    """Return the sum of all unmarked positions on the board"""
    return sum([ board[i] or 0 for i in range(dim*dim) ])

def winning_numbers(numbers, boards):
    """Return an associaton list of the form:
       [ [<m>, [<winning-board-m-1>, <winning-board-m-2>, ...]]
         [<n>, [<winning-board-n-1>, <winning-board-n-2>, ...]] ]"""
    result = []

    for n in numbers:
        boards = mark_boards(n, boards)
        yes, no = partition(boards, is_winning)
        if yes:
            result.append([n, yes])
        boards = no

    return result

# Tests ---------------------------------------------------------------------------------------

class TestDay04(unittest.TestCase):
    def test_is_winning(self):
        self.assertFalse(is_winning([1]*25))
        self.assertTrue(is_winning([1,1,1,1,1,False,False,False,False,False,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
        self.assertTrue(is_winning([1,False,1,1,1,1,False,1,1,1,1,False,1,1,1,1,False,1,1,1,1,False,1,1,1]))

    def test_mark_board(self):
        self.assertEqual(mark_board(7,[1,2,3,7,6,5,7,8,9,7]), [1,2,3,False,6,5,False,8,9,False])

    def test_mark_boards(self):
        self.assertEqual(mark_boards(7,[[1,7,2,3,7],[7,7,1,2,3]]), [[1,False,2,3,False],[False,False,1,2,3]])

    def test_part1(self):
        self.assertEqual(part1(), 8442)

    def test_part2(self):
        self.assertEqual(part2(), 4590)

unittest.main()
