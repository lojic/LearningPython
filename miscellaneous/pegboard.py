# Peg solitaire (Triangular, 15 hole version a la Cracker Barrel)
# https://en.wikipedia.org/wiki/Peg_solitaire
# https://blog.crackerbarrel.com/2021/08/13/how-to-beat-the-cracker-barrel-peg-game/
#
#                 (0,0)
#                /     \
#             (1,0) - (1,1)
#            /     \ /     \
#         (2,0) - (2,1) - (2,2)
#        /     \ /     \ /     \
#     (3,0) - (3,1) - (3,2) - (3,3)
#    /     \ /     \ /     \ /     \
# (4,0) - (4,1) - (4,2) - (4,3) - (4,4)

class Board:
    def __init__(self, empty_hole=(0,0), goal=None):
        self.board = [ [ True ],
                       [ True, True ],
                       [ True, True,  True ],
                       [ True, True,  True,  True ],
                       [ True, True,  True,  True,  True  ] ]
        self[empty_hole] = False
        self.goal = goal

    def __getitem__(self, pos):
        return self.board[pos[0]][pos[1]]

    def __setitem__(self, pos, val):
        self.board[pos[0]][pos[1]] = val

    def move(self, m):
        self[m[0]], self[m[1]], self[m[2]] = False, False, True

    def unmove(self,m):
        self[m[0]], self[m[1]], self[m[2]] = True, True, False

    def is_goal(self):
        return False if self.goal and not self[self.goal] else sum(1 for _ in self.pegs()) == 1

    def pegs(self):
        return [pos for pos in [ (row, col) for row in range(5) for col in range(row + 1) ] if self[pos] ]

    def position_moves(self, pos):
        add      = lambda p1, p2: (p1[0] + p2[0], p1[1] + p2[1])
        is_valid = lambda pos: pos and 0 <= pos[1] <= pos[0] <= 4

        for dir in ( (-1, 0), (0, 1), (1, 1), (1, 0), (0, -1), (-1, -1) ):
            neighbor = add(pos, dir)
            if is_valid(neighbor) and self[neighbor]:
                dst = add(neighbor, dir)
                if is_valid(dst) and not self[dst]:
                    yield (pos, neighbor, dst)

    def play(self, moves=[]):
        if next_moves := [ m for peg in self.pegs() for m in self.position_moves(peg) ]:
            for m in next_moves:
                self.move(m)
                yield from self.play(moves + [ m ])
                self.unmove(m)
        elif self.is_goal():
            yield moves

# Display the first solution starting from (2,1). No goal is chosen
# because this is one starting position where you can't have the
# remaining peg end up in the starting hole.
print(next(Board(empty_hole=(2,1)).play()))

# Count the number of solutions with a starting hole of (0,0) with no
# goal specified.
print(sum(1 for _ in Board(empty_hole=(0,0)).play()))

# Same, but specify a goal of (0,0)
print(sum(1 for _ in Board(empty_hole=(0,0),goal=(0,0)).play()))
