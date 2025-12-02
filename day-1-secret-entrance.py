
start = 50

zero_count = 0 # Part 1, count landing at zero
pass_zero_count = 0 # Part 2, count passing zero

file_path = "./puzzle-input.txt"

try:
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            dir = line[0]
            clicks = int(line[1:])

            if dir == 'L':
                for i in range(0, clicks):
                    if start == 0:
                        start = 99
                        pass_zero_count += 1
                    else:
                        start -= 1

            elif dir == 'R':
                for i in range(0, clicks):
                    if start == 0:
                        pass_zero_count += 1
                    if start == 99:
                        start = 0
                    else:
                        start += 1

            if start == 0:
                zero_count += 1

    print(f"The dial landed at zero {zero_count} times.")
    print(f"The dial passed zero {pass_zero_count} times.")

except FileNotFoundError:
    print(f"Error: the file path {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
