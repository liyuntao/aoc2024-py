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
    result = q1(relation_dict, input_lists)
    print(result)


def q1(relation_dict: dict[int, set[int]], input_lists: list[list[int]]) -> int:
    result: int = 0
    for single_list in input_lists:
        is_valid = True
        for a, b in zip(single_list, single_list[1:]):
            if a in relation_dict and b in relation_dict[a]:
                is_valid = is_valid and True
            else:
                is_valid = is_valid and False
        if is_valid:
            result += middle_of_list(single_list)

    return result


def middle_of_list(single_list: list[int]) -> int:
    return single_list[len(single_list) // 2]


if __name__ == "__main__":
    main()
