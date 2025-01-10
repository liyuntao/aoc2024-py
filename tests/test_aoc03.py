from aoc03 import q1, q2

def test_q1():
    input_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    total_sum = q1(input_string)
    assert total_sum == 161, f"Expected 161, but got {total_sum}" 


def test_Q2():
    input_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    total_sum = q2(input_string)
    assert total_sum == 48, f"Expected 48, but got {total_sum}" 
