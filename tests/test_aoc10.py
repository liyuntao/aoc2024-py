from aoc10 import q1, q2, parse_input_10


def test_q1_q2():
    raw_input = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
    grid = parse_input_10(raw_input)

    assert 36 == q1(grid)
    assert 81 == q2(grid)
