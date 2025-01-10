import pytest
from aoc02 import q1, is_all_increasing_or_decreasing, is_gap_ok
from typing import List

def test_q1(capsys): 
    raw_input: str = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
    test_input: List[List[int]] = [
        [int(num) for num in line.split()]
        for line in raw_input.strip().split('\n')
    ]
    
    print(test_input[2])

    assert is_all_increasing_or_decreasing(test_input[1]) == True
    assert is_gap_ok(test_input[1]) == False
    assert q1(test_input) == 2

