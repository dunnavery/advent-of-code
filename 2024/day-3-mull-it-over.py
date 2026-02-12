import re

file_path = './puzzle-input.txt'

def compute_matching_multiplication(matching):
    total = 0
    for match in matching:
        match = match.split(',')
        first = match[0].split('(')[-1]
        second = match[1].split(')')[0]

        mult = int(first) * int(second)
        total += mult
    
    return total


with open(file_path, 'r') as file:
    part_one_total = 0
    part_two_total = 0
    memory = ""
    for line in file:
        line = line.strip()
        memory += line

    # Part 1: Use regex to determine where the in the line there is strictly mul([1-3], [1-3])
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matching = re.findall(pattern, memory)

    part_one_total += compute_matching_multiplication(matching)

    # Part 2: Scanning through corrupted memory and must handle conditional do() or don't() statements
    memory = memory.split("don't()")
    print(f"split at don't(): {memory}")
    
    # memory[0] is always do
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matching = re.findall(pattern, memory[0])

    part_two_total += compute_matching_multiplication(matching)

    memory = memory[1:]
    print(f"remaining memory array: {memory}")
    # In remaining memory we have to look for do()'s in the str and split
    for remaining in memory:
        mem = remaining.split('do()')
        if len(mem) > 1:
            mem = mem[1:]
            for m in mem:
                matching = re.findall(pattern, m)
                part_two_total += compute_matching_multiplication(matching)
            
    
    print(f"Part 1 total: {part_one_total}")
    print(f"Part 2 total: {part_two_total}")
