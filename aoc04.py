from typing import Dict, List, Tuple


WINDOW_SIZE: int = 4


def main() -> None:
    input_sample: str = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

    data_2d, row_cnt, col_cnt = raw_parse_04(input_sample)

    q1(data_2d, row_cnt, col_cnt)


def raw_parse_04(input: str) -> Tuple[Dict[Tuple[int, int], str], int, int]:
    char_dict: Dict[Tuple[int, int], str] = {}

    lines = input.strip().split("\n")

    row_cnt = len(lines)
    col_cnt = len(lines[0])

    for row_index, line in enumerate(lines):
        for col_index, char in enumerate(line):
            char_dict[(row_index, col_index)] = char

    return char_dict, row_cnt, col_cnt


def q1(matrix: Dict[Tuple[int, int], str], row_cnt: int, col_cnt: int) -> int:
    print(gen_single_horizontal_part(row_cnt, col_cnt))
    pass


def gen_single_horizontal_part(row_cnt: int, col_cnt: int) -> List[Tuple[int, int]]:
    result = []
    for y in range(row_cnt):
        for x in range(col_cnt):
            print(x, y)
            result.append((x, y))
    return result


if __name__ == "__main__":
    main()
