import pytest
from aoc01 import q1, q2
from typing import List, Tuple


def parse() -> Tuple[List[int], List[int]]:
    raw_input: str = """
3   4
4   3
2   5
1   3
3   9
3   3
"""
    # Split the raw_input into lines and strip any leading/trailing whitespace
    lines: List[str] = [line.strip() for line in raw_input.strip().split('\n')]

    first_column: List[int] = [int(line.split()[0]) for line in lines]
    second_column: List[int] = [int(line.split()[1]) for line in lines]
    
    return first_column, second_column


def test_q1(): 
    parsed_input = parse()
    assert q1(parsed_input[0], parsed_input[1]) == 11

def test_q2(): 
    parsed_input = parse()
    assert q2(parsed_input[0], parsed_input[1]) == 31