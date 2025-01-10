from typing import List

def main():
    # Read from input file
    with open('./inputs/input01.txt', 'r') as file:
        lines: List[str] = [line.strip() for line in file if line.strip()]

    first_column: List[int] = [int(line.split()[0]) for line in lines]
    second_column: List[int] = [int(line.split()[1]) for line in lines]

    result1 = q1(first_column, second_column)
    result2 = q2(first_column, second_column)
    
    print("Q1 - Result:", result1)
    print("Q2 - Result:", result2)

def q1(first_column: List[int], second_column: List[int]) -> int:
    first_copy = first_column.copy()
    second_copy = second_column.copy()

    differences: List[int] = [abs(a - b) for a, b in zip(first_copy, second_copy)]
    return sum(differences)

def q2(first_column: List[int], second_column: List[int]) -> int:
    total = 0
    for num in first_column:
        count = second_column.count(num)
        tmp = num * count
        total += tmp
    return total

if __name__ == "__main__":
    main()
