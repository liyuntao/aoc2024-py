from dataclasses import dataclass
import itertools


@dataclass
class Area:
    width: int
    height: int
    dataset: dict[tuple[int, int], str]
    grouped_value: dict[str, list[tuple[int, int]]]


def parse_input_08(raw_input: str) -> Area:
    lines = [line for line in raw_input.strip().split("\n") if line]

    height = len(lines)
    width = len(lines[0]) if height > 0 else 0
    dataset: dict[tuple[int, int], str] = {}
    grouped_value: dict[str, list[tuple[int, int]]] = {}

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ".":
                coord = (x, y)
                dataset[coord] = char
                # Add coordinate to grouped_value
                if char not in grouped_value:
                    grouped_value[char] = []
                grouped_value[char].append(coord)

    return Area(
        width=width, height=height, dataset=dataset, grouped_value=grouped_value
    )


def permutation_2(
    data: list[tuple[int, int]],
) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    return list(itertools.combinations(data, 2))


def anti_nodes_q1(
    d1: tuple[int, int], d2: tuple[int, int], guard_x: int, guard_y: int
) -> list[tuple[int, int]]:
    result = []
    target_x = 2 * d1[0] - d2[0]
    target_y = 2 * d1[1] - d2[1]
    if target_x >= 0 and target_y >= 0 and target_x < guard_x and target_y < guard_y:
        result.append((target_x, target_y))

    target_x2 = 2 * d2[0] - d1[0]
    target_y2 = 2 * d2[1] - d1[1]
    if (
        target_x2 >= 0
        and target_y2 >= 0
        and target_x2 < guard_x
        and target_y2 < guard_y
    ):
        result.append((target_x2, target_y2))
    return result


def q1(area: Area) -> int:
    final_set: set[tuple[int, int]] = set()
    for key, value in area.grouped_value.items():
        if len(value) > 1:
            for d1, d2 in permutation_2(value):
                for anti_node in anti_nodes_q1(d1, d2, area.width, area.height):
                    final_set.add(anti_node)

    return len(final_set)


def main() -> None:
    with open("./inputs/input08.txt", "r") as file:
        raw_input = file.read()
    input = parse_input_08(raw_input)
    # print(input)
    print(q1(input))


if __name__ == "__main__":
    main()
