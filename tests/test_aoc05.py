from aoc05 import union_parse, q1, q2


def test_q1_q2():
    raw_input: str = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

    relation_dict, input_lists = union_parse(raw_input)

    result_q1 = q1(relation_dict, input_lists)
    assert result_q1 == 143, f"Expected 143, but got {result_q1}"

    result_q2 = q2(relation_dict, input_lists)
    assert result_q2 == 123, f"Expected 123, but got {result_q2}"
