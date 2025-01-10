from aoc02 import (
    gen_sub_list,
    is_any_safe,
    q1,
    q2,
    is_all_increasing_or_decreasing,
    is_gap_ok,
)
from typing import List


def parse() -> List[List[int]]:
    raw_input: str = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

    test_input: List[List[int]] = [
        [int(num) for num in line.split()] for line in raw_input.strip().split("\n")
    ]
    return test_input


def test_gen_sub_list():
    test_input = [7, 6, 4, 2, 1]
    assert gen_sub_list(test_input) == [
        [6, 4, 2, 1],
        [7, 4, 2, 1],
        [7, 6, 2, 1],
        [7, 6, 4, 1],
        [7, 6, 4, 2],
    ]


def test_is_any_safe():
    test_input = [[1, 2, 7, 8], [2, 7, 8, 9]]
    assert is_any_safe(test_input) == False


def test_q1():
    test_input = parse()
    assert is_all_increasing_or_decreasing(test_input[1]) == True
    assert is_gap_ok(test_input[1]) == False

    assert q1(test_input) == 2


def test_q2():
    test_input: List[List[int]] = parse()
    assert q2(test_input) == 4
