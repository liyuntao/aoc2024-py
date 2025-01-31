from typing import List


def main():
    # Read from input file
    with open("./inputs/input02.txt", "r") as file:
        lines: List[str] = [line.strip() for line in file if line.strip()]

    input: List[List[int]] = [list(map(int, line.split())) for line in lines]

    result1 = q1(input)
    result2 = q2(input)

    print("Q1 - Result:", result1)
    print("Q2 - Result:", result2)


def q1(input: List[List[int]]) -> int:
    return len(list(filter(lambda x: is_safe(x), input)))


def q2(input: List[List[int]]) -> int:
    total_safe = 0
    for element in input:
        if is_safe(element):
            total_safe += 1
        elif is_any_safe(gen_sub_list(element)):
            total_safe += 1
    return total_safe


def is_any_safe(sub_list: List[int]) -> bool:
    return any(is_safe(sub_element) for sub_element in sub_list)


def is_all_increasing_or_decreasing(numbers: List[int]) -> bool:
    if len(numbers) <= 1:
        return True

    # Check if increasing
    is_increasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
    # Check if decreasing
    is_decreasing = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))

    return is_increasing or is_decreasing


def is_gap_ok(numbers: List[int]) -> bool:
    if len(numbers) <= 1:
        return True

    # Check if all adjacent differences are 1, 2, or 3
    return all(
        1 <= abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1)
    )


def is_safe(numbers: List[int]) -> bool:
    return is_all_increasing_or_decreasing(numbers) and is_gap_ok(numbers)


def gen_sub_list(numbers: List[int]) -> List[List[int]]:
    assert len(numbers) >= 2, "Input list must have at least 2 elements"
    return [numbers[:i] + numbers[i + 1 :] for i in range(len(numbers))]


if __name__ == "__main__":
    main()
