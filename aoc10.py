from collections import deque


def parse_input_10(raw_input: str) -> list[list[int]]:
    lines = raw_input.strip().splitlines()
    grid = [[int(ch) for ch in line.strip()] for line in lines if line.strip()]
    return grid


def q1(grid: list[list[int]]) -> int:
    if not grid:
        return 0

    n_rows = len(grid)
    n_cols = len(grid[0])
    total_endpoints_count = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == 0:
                queue: deque[tuple[int, int, int]] = deque()
                queue.append((i, j, 0))
                endpoints: set[tuple[int, int]] = set()

                while queue:
                    row, col, curr_value = queue.popleft()

                    if grid[row][col] == 9:
                        endpoints.add((row, col))
                        continue

                    next_value = curr_value + 1

                    # Explore neighbors (vertical and horizontal movements)
                    for dr, dc in directions:
                        new_row, new_col = row + dr, col + dc
                        if 0 <= new_row < n_rows and 0 <= new_col < n_cols:
                            if grid[new_row][new_col] == next_value:
                                queue.append((new_row, new_col, next_value))

                total_endpoints_count += len(endpoints)

    return total_endpoints_count


def q2(grid: list[list[int]]) -> int:
    if not grid:
        return 0

    n_rows = len(grid)
    n_cols = len(grid[0])
    total_available_paths = 0

    queue: deque[tuple[int, int, int]] = deque()

    for i, j in ((i, j) for i in range(n_rows) for j in range(n_cols)):
        if grid[i][j] == 0:
            queue.append((i, j, 0))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        row, col, curr_value = queue.popleft()

        if grid[row][col] == 9:
            total_available_paths += 1
            continue

        next_value = curr_value + 1

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n_rows and 0 <= new_col < n_cols:
                if grid[new_row][new_col] == next_value:
                    queue.append((new_row, new_col, next_value))

    return total_available_paths


def main() -> None:
    with open("./inputs/input10.txt", "r") as file:
        raw_input = file.read()

    grid = parse_input_10(raw_input)

    total_endpoints = q1(grid)
    print("q1 =", total_endpoints)

    total_available_paths = q2(grid)
    print("q2 =", total_available_paths)


if __name__ == "__main__":
    main()
