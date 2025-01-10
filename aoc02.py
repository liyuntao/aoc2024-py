import re
from typing import List

def q1(input: List[List[int]]) -> int:
    return len(list(filter(lambda x: is_safe(x), input)))

def main():
    # Hardcoded input string
    input_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    
    # Extract and evaluate 'mul(a, b)' expressions
    mul_matches = re.findall(r'mul\((\d+),\s*(\d+)\)', input_string)
    for match in mul_matches:
        a, b = map(int, match)  # Convert to integers
        result = a * b
        print(f"mul({a}, {b}) = {result}")

    # If you still want to process the input for q1, you can parse it accordingly
    # For example, you can extract numbers from the input string
    input_numbers = [int(num) for num in re.findall(r'\d+', input_string)]
    input_list = [input_numbers]  # Wrap in a list of lists for q1

    print(q1(input_list))

def is_all_increasing_or_decreasing(numbers: List[int]) -> bool:
    if len(numbers) <= 1:
        return True
    
    # Check if increasing
    is_increasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
    # Check if decreasing
    is_decreasing = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))
    
    return is_increasing or is_decreasing

def is_gap_ok(numbers: List[int]) -> bool:
    if len(numbers) <= 1:
        return True
    
    # Check if all adjacent differences are 1, 2, or 3
    return all(1 <= abs(numbers[i] - numbers[i + 1]) <= 3 
              for i in range(len(numbers) - 1))

def is_safe(numbers: List[int]) -> bool:
    return is_all_increasing_or_decreasing(numbers) and is_gap_ok(numbers)

def gen_sub_list(numbers: List[int]) -> List[List[int]]:
    assert len(numbers) >= 2, "Input list must have at least 2 elements"
    return [
        numbers[:i] + numbers[i+1:] 
        for i in range(len(numbers))
    ]

if __name__ == "__main__":
    main()
