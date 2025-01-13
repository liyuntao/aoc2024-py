from functools import cmp_to_key
from typing import Tuple


def union_parse(raw_input: str) -> Tuple[dict[int, set[int]], list[list[int]]]:
    result1: dict[int, set[int]] = {}
    result2: list[list[int]] = []

    # Skip empty lines and process each non-empty line
    for line in raw_input.strip().splitlines():
        if not line:
            continue

        if line.find("|") != -1:
            left, right = map(int, line.split("|"))

            # Initialize set if key doesn't exist
            if left not in result1:
                result1[left] = set()
            result1[left].add(right)
        elif line.find(",") != -1:
            numbers = [int(x) for x in line.strip().split(",")]
            result2.append(numbers)

    return result1, result2


def main() -> None:
    with open("./inputs/input05.txt", "r") as file:
        content = file.read()

    relation_dict, input_lists = union_parse(content)

    result1 = q1(relation_dict, input_lists)
    print("Q1 - Result:", result1)
    result2 = q2(relation_dict, input_lists)
    print("Q2 - Result:", result2)


def is_valid_order(single_list: list[int], relation_dict: dict[int, set[int]]) -> bool:
    is_valid = True
    for a, b in zip(single_list, single_list[1:]):
        if a in relation_dict and b in relation_dict[a]:
            is_valid = is_valid and True
        else:
            is_valid = is_valid and False
            break
    return is_valid


def q1(relation_dict: dict[int, set[int]], input_lists: list[list[int]]) -> int:
    result: int = 0
    for single_list in input_lists:
        if is_valid_order(single_list, relation_dict):
            result += middle_of_list(single_list)
    return result


def q2(relation_dict: dict[int, set[int]], input_lists: list[list[int]]) -> int:
    def custom_comparator(x, y):
        if x in relation_dict and y in relation_dict[x]:
            return -1
        elif y in relation_dict and x in relation_dict[y]:
            return 1
        else:
            return 1

    result: int = 0
    for single_list in input_lists:
        if not is_valid_order(single_list, relation_dict):
            sorted_list = sorted(single_list, key=cmp_to_key(custom_comparator))
            result += middle_of_list(sorted_list)
    return result


def middle_of_list(single_list: list[int]) -> int:
    return single_list[len(single_list) // 2]


if __name__ == "__main__":
    main()
