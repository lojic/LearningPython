from app.day01_edge import rotate


def test_left_rotation():
    # Not touching zero
    assert rotate(10, 'L', 5) == (5, 0)

    # Directly to zero
    assert rotate(10, 'L', 10) == (0, 1)

    # Cross zero once
    assert rotate(2, 'L', 4) == (98, 1)

    # Cross zero to zero
    assert rotate(10, 'L', 110) == (0, 2)

    # Cross zero twice
    assert rotate(2, 'L', 104) == (98, 2)

    # From zero
    assert rotate(0, 'L', 2) == (98, 0)

    # From zero to zero
    assert rotate(0, 'L', 100) == (0, 1)

    # From zero cross zero
    assert rotate(0, 'L', 102) == (98, 1)

    # From zero to zero after crossing zero
    assert rotate(0, 'L', 200) == (0, 2)


def test_right_rotation():
    # Not touching zero
    assert rotate(95, 'R', 3) == (98, 0)

    # Directly to zero
    assert rotate(98, 'R', 2) == (0, 1)

    # Cross zero once
    assert rotate(98, 'R', 4) == (2, 1)

    # Cross zero to zero
    assert rotate(98, 'R', 102) == (0, 2)

    # Cross zero twice
    assert rotate(98, 'R', 104) == (2, 2)

    # From zero
    assert rotate(0, 'R', 4) == (4, 0)

    # From zero to zero
    assert rotate(0, 'R', 100) == (0, 1)

    # From zero cross zero
    assert rotate(0, 'R', 102) == (2, 1)

    # From zero to zero after crossing zero
    assert rotate(0, 'R', 200) == (0, 2)
