from dataclasses import dataclass


@dataclass
class Day7InputItem:
    target_value: int
    input: list[int]


def q1(input: list[Day7InputItem]) -> int:
    total: int = 0
    for item in input:
        all_possible = generate_all_possible_v1(len(item.input) - 1)
        for expression in all_possible:
            if evaluate(item, expression) == item.target_value:
                total += item.target_value
                break
    return total


def q2(input: list[Day7InputItem]) -> int:
    total: int = 0
    for item in input:
        all_possible = generate_all_possible_v2(len(item.input) - 1)
        for expression in all_possible:
            if evaluate(item, expression) == item.target_value:
                total += item.target_value
                break
    return total


def parse_input_q7(raw_input: str) -> list[Day7InputItem]:
    result: list[Day7InputItem] = []
    for line in raw_input.strip().splitlines():
        target_raw, list_part = line.split(":")
        target_value = int(target_raw)
        input_list = [int(x) for x in list_part.split()]
        result.append(Day7InputItem(target_value, input_list))
    return result


def generate_all_possible_v1(count: int) -> list[list[str]]:
    if count == 1:
        return [["+"], ["*"]]
    else:
        N_1 = generate_all_possible_v1(count - 1)
        return [["+"] + x for x in N_1] + [["*"] + x for x in N_1]


def generate_all_possible_v2(count: int) -> list[list[str]]:
    if count == 1:
        return [["+"], ["*"], ["||"]]
    else:
        N_1 = generate_all_possible_v2(count - 1)
        return (
            [["+"] + x for x in N_1]
            + [["*"] + x for x in N_1]
            + [["||"] + x for x in N_1]
        )


def evaluate(item: Day7InputItem, expression: list[str]) -> int:
    input: list[int] = item.input
    target_value: int = item.target_value

    total: int = 0
    for idx in range(len(input)):
        if idx == 0:
            total = input[idx]
        else:
            if expression[idx - 1] == "+":
                total += input[idx]
            elif expression[idx - 1] == "*":
                total *= input[idx]
            elif expression[idx - 1] == "||":
                total = int(str(total) + str(input[idx]))
        if total > target_value:
            return -1
    return total


def main() -> None:
    with open("./inputs/input07.txt", "r") as file:
        raw_input = file.read()

    result_q1 = q1(parse_input_q7(raw_input))
    print(result_q1)
    result_q2 = q2(parse_input_q7(raw_input))
    print(result_q2)


if __name__ == "__main__":
    main()
