from app.advent import (
    atom,
    atoms,
    binary_search,
    bool_list_to_decimal,
    compose,
    decimal_to_bool_list,
    digits,
    file_to_lines,
    findf,
    grid_to_hash,
    grid_word_search,
    ints,
    iterate,
    mapt,
    parse,
    partition,
    quantify,
    trunc,
    words,
)


def test_binary_search():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    idx = binary_search(lambda n: lst[n] >= 3, 0, len(lst) - 1)
    assert idx == 3

    lst = ['apple', 'banana', 'cherry', 'date', 'kiwi', 'strawberry']
    idx = binary_search(lambda n: lst[n] >= 'cherry', 0, len(lst) - 1)
    assert idx == 2


def test_bool_list_to_decimal():
    assert bool_list_to_decimal([1, 0, 1, 1]) == 11


def test_compose():
    def square(n: int) -> int:
        return n * n

    def double(n: int) -> int:
        return 2 * n

    def cast(s: str) -> int:
        return int(s)

    square_double = compose(square, double)
    assert square_double(7) == 196

    square_double_str = compose(square_double, cast)
    assert square_double_str('77') == 23716


def test_decimal_to_bool_list():
    assert decimal_to_bool_list(11) == [1, 0, 1, 1]
    assert decimal_to_bool_list(65535) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def test_file_to_lines():
    lines = file_to_lines('tests/test_advent.py')
    assert len(lines) > 150
    assert 'def test_file_to_lines():' in lines


def test_findf():
    lst = [-3, -4, -7, 5, 4, 3]
    first_positive = findf(lambda n: n > 0, lst)
    assert first_positive == 5
    assert findf(lambda n: n > 10, lst) is None


def test_grid_to_hash():
    #  ..#...#.
    #  ...#....
    #  .#.....#
    #  ##...#..
    lines = ["..#...#.", "...#....", ".#.....#", "##...#.."]
    hsh = grid_to_hash(lines)
    st = set(hsh.keys())

    assert len(st) == 32  # entire 8 x 4 grid
    assert 2 + 2j in st
    assert hsh[3 + 1j] == '#'

    hsh = grid_to_hash(lines, elem_filter=lambda col: col == '#')
    keys = hsh.keys()

    assert len(keys) == 8
    assert (1 + 2j) in hsh
    assert not (2 + 1j) in hsh

    hsh = grid_to_hash(lines, elem_transform=lambda c: "land" if c == '#' else "water")

    assert hsh[7 + 2j] == "land"
    assert hsh[7 + 3j] == "water"

    hsh = grid_to_hash(
        lines, row_transform=reversed, elem_transform=lambda c: "land" if c == '#' else "water"
    )

    assert hsh[+2j] == "land"
    assert hsh[1 + 2j] == "water"


def test_grid_word_search():
    # " xmas "
    # "smm sx"
    # " a am "
    # " smas "
    # " xsx  "
    grid = (" xmas ", "smm sx", " a am ", " smas ", " xsx  ")
    assert list(grid_word_search(grid, "xmas")) == [
        (1, 0, 1),
        (1, 0, (1 + 1j)),
        (1, 0, 1j),
        (5, 1, (-1 + 1j)),
        (3, 4, (-1 - 1j)),
        (1, 4, (1 - 1j)),
    ]


def test_iterate():
    thrice_squared = iterate(lambda n: n * n, 7, 3)
    assert thrice_squared == 5764801


def test_partition():
    pos, neg = partition([1, 4, -7, 5, -9, -1], lambda n: n >= 0)
    assert pos == [1, 4, 5]
    assert neg == [-7, -9, -1]


# Peter Norvig's functions


def test_atom():
    assert atom(" 7 ") == 7
    assert atom(" 7.3 ") == 7.3
    assert atom(" s ") == " s "


def test_atoms():
    assert atoms(" 7,foo   bar: 9.8 ") == (7, "foo", "bar", 9.8)


def test_digits():
    assert digits("3.14 is pi, 2.718 is e") == (3, 1, 4, 2, 7, 1, 8)


def test_ints():
    assert ints("3.14 is pi, 2.718 is e") == (3, 14, 2, 718)


def test_mapt():
    squares = mapt(lambda n: n * n, [1, 2, 3])
    assert squares == (1, 4, 9)


def test_parse():
    """
    See tests/day01.txt and tests/day05.txt for sample data.
    """
    left, right = zip(*parse(1, ints, root='tests'))
    assert left == (95228, 77437, 33685, 99368)
    assert right == (20832, 82573, 76537, 67870)

    rules, updates = parse(5, lambda s: mapt(ints, str.split(s)), sep='\n\n', root='tests')
    assert rules == ((96, 54), (79, 47), (79, 13))
    assert updates == (
        (78, 18, 57, 52, 59, 14, 87, 53, 15, 28, 94),
        (55, 88, 31, 49, 93, 59, 53, 13, 46, 57, 86, 43, 15, 18, 78, 94, 52, 27, 14),
        (33, 19, 35, 67, 62, 21, 47),
    )


def test_quantify():
    assert quantify([1, 2, 3, 4, 5, 6, 8], lambda n: (n % 2) != 0) == 3


def test_trunc():
    assert trunc("beginning to the end", left=3, right=3) == "beg ... end"


def test_words():
    assert words("one, two...three MixedCase") == ["one", "two", "three", "MixedCase"]
