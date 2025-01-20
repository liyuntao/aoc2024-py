import array
from aoc09 import count_block_size, checksum, parse_and_defrag


def test_count_block_size():
    input_data = "2333133121414131402"
    block_detail = count_block_size(input_data)
    assert 42 == block_detail.total
    assert 14 == block_detail.free_total


def test_checksum():
    input_data = array.array("i", [0, 0, 9, 9, 8])
    assert 77 == checksum(input_data)


def test_parse_and_defrag():
    input_data = "2333133121414131402"
    block_detail = count_block_size(input_data)
    result = parse_and_defrag(input_data, block_detail)

    assert (
        array.array(
            "i",
            [
                0,
                0,
                -1,
                -1,
                -1,
                1,
                1,
                1,
                -1,
                -1,
                -1,
                2,
                -1,
                -1,
                -1,
                3,
                3,
                3,
                -1,
                4,
                4,
                -1,
                5,
                5,
                5,
                5,
                -1,
                6,
                6,
                6,
                6,
                -1,
                7,
                7,
                7,
                -1,
                8,
                8,
                8,
                8,
                9,
                9,
            ],
        )
        == result
    )
