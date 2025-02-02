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
    for point1, point2 in [(d1, d2), (d2, d1)]:
        target = (2 * point1[0] - point2[0], 2 * point1[1] - point2[1])
        if all(0 <= t < g for t, g in zip(target, (guard_x, guard_y))):
            result.append(target)
    return result


def anti_nodes_q2(
    d1: tuple[int, int], d2: tuple[int, int], guard_x: int, guard_y: int
) -> list[tuple[int, int]]:
    result = []
    result.append(d1)
    result.append(d2)

    vector_x = d2[0] - d1[0]
    vector_y = d2[1] - d1[1]

    temp_x = d2[0] + vector_x
    temp_y = d2[1] + vector_y
    while 0 <= temp_x < guard_x and 0 <= temp_y < guard_y:
        result.append((temp_x, temp_y))
        temp_x += vector_x
        temp_y += vector_y

    temp_x = d1[0] - vector_x
    temp_y = d1[1] - vector_y
    while 0 <= temp_x < guard_x and 0 <= temp_y < guard_y:
        result.append((temp_x, temp_y))
        temp_x -= vector_x
        temp_y -= vector_y

    return result


def evaluate(area: Area, anti_nodes_generator: callable) -> int:
    final_set: set[tuple[int, int]] = set()
    for key, value in area.grouped_value.items():
        if len(value) > 1:
            for d1, d2 in permutation_2(value):
                for anti_node in anti_nodes_generator(d1, d2, area.width, area.height):
                    final_set.add(anti_node)
    return len(final_set)


def q1(area: Area) -> int:
    return evaluate(area, anti_nodes_q1)


def q2(area: Area) -> int:
    return evaluate(area, anti_nodes_q2)


def main() -> None:
    with open("./inputs/input08.txt", "r") as file:
        raw_input = file.read()
    input = parse_input_08(raw_input)
    print(q1(input))
    print(q2(input))


if __name__ == "__main__":
    main()
