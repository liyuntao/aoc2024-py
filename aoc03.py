import re
from typing import List

def q1(input: str) -> int:
    mul_matches: List[tuple] = re.findall(r'mul\((\d+),\s*(\d+)\)', input)
    total_sum: int = 0
    for match in mul_matches:
        a, b = map(int, match)  # Convert to integers
        result: int = a * b
        total_sum += result  # Add to total sum
    return total_sum  # Return the total sum

def extract_parts(input: str) -> List[str]:
    # Define the regex pattern to match 'mul(a, b)', 'do()', or 'don't()'
    pattern: str = r'mul\(\d+,\s*\d+\)|do\(\)|don\'t\(\)'
    
    # Find all matches in the input string
    matches: List[str] = re.findall(pattern, input)
    
    return matches  # Return the list of matched strings

def q2(input: str) -> int:
    parts = extract_parts(input)

    result = []
    collecting = True  # Flag to indicate whether to collect 'mul' elements

    for item in parts:
        if item == "don't()":
            collecting = False  # Stop collecting when 'don't()' is encountered
        elif item == "do()":
            collecting = True  # Resume collecting when 'do()' is encountered
            continue  # Skip adding 'do()' to the result
        
        if collecting and item.startswith("mul"):
            result.append(item)  # Collect 'mul' elements if collecting is True

    total_sum = 0
    for mul_item in result:
        # Extract a and b using regex
        match = re.match(r'mul\((\d+),\s*(\d+)\)', mul_item)
        if match:
            a = int(match.group(1))  # Get the first captured group as integer
            b = int(match.group(2))  # Get the second captured group as integer
            total_sum += a * b  # Multiply a and b and add to total_sum

    return total_sum

def main() -> None:
    # Read the entire content of the file into the variable 'input'
    raw_input: str = ""
    with open('inputs/input03.txt', 'r') as file:
        raw_input = file.read()  # Read the whole file content into 'input'
    
    print("Parsed results from q1:", q1(raw_input))
    print("Parsed results from q2:", q2(raw_input))

if __name__ == "__main__":
    main()
