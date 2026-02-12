
file_path = './puzzle-input.txt'

# Part 1: finding largest joltage of numbers per battery
try:
    with open(file_path, 'r') as file:
        total_joltage = 0
        for line in file:
            max_joltage = 0
            for i in range(len(line)):
                for j in range(i+1, len(line)):
                    joltage = f"{line[i]}{line[j]}"
                    joltage = int(joltage)
                    if joltage > max_joltage:
                        max_joltage = joltage
            total_joltage += max_joltage
        print(f"Total joltage = {total_joltage}")
except FileNotFoundError:
    print(f"Error: the file path was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


# Part 2: finding largest joltage of numbers per battery
try:
    with open(file_path, 'r') as file:
        total_joltage = 0
        for line in file:
            line = line.strip()
            remaining_list = line
            joltage = []
            for i in reversed(range(12)):
                if i != 0:
                    element = max(remaining_list[:-i])
                    joltage.append(element)
                    element_idx = remaining_list.index(f'{element}')
                    remaining_list = remaining_list[element_idx+1:]
                elif len(remaining_list) > 0:
                    element = max(remaining_list)
                    joltage.append(element)

            joltage = int(''.join(joltage))
            print(f"Joltage per battery {joltage}")
            total_joltage += joltage

        print(f"Total joltage = {total_joltage}")
except FileNotFoundError:
    print(f"Error: the file path was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


