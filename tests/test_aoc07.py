from aoc07 import q1, q2, parse_input_q7, Day7InputItem


def test_q1_q2():
    raw_input = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

    parsed_items: list[Day7InputItem] = parse_input_q7(raw_input)

    result_q1 = q1(parsed_items)
    assert result_q1 == 3749, f"Expected 3749, but got {result_q1}"

    result_q2 = q2(parsed_items)
    assert result_q2 == 11387, f"Expected 11387, but got {result_q2}"
