import array
from dataclasses import dataclass


@dataclass
class BlockDetail:
    total: int
    usage_total: int
    free_total: int


## origin -> origin, ext -> defrag -> checksum


def count_block_size(raw_input: str) -> BlockDetail:
    assert len(raw_input) % 2 != 0
    usage_total = 0
    free_total = 0

    for i in range(len(raw_input)):
        if i % 2 == 0:
            usage_total += int(raw_input[i])
        else:
            free_total += int(raw_input[i])

    return BlockDetail(
        total=usage_total + free_total, usage_total=usage_total, free_total=free_total
    )


def parse_and_defrag(raw_input: str, block_detail: BlockDetail) -> array.array:
    memory_data = array.array("i", [-1] * block_detail.total)

    cnt = 0
    for i in range(len(raw_input)):
        value = int(raw_input[i])
        # data block part
        if i % 2 == 0:
            file_id = i // 2
            for _ in range(value):
                memory_data[cnt] = file_id
                cnt += 1
        # empty block part
        else:
            for _ in range(value):
                cnt += 1
    return memory_data


def checksum(data: array.array) -> int:
    return sum(index * value for index, value in enumerate(data))


def main() -> None:
    # with open("./inputs/input09.txt", "r") as file:
    # raw_input = file.read()

    pass


if __name__ == "__main__":
    main()
