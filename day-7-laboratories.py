
file_path = './puzzle-input.txt'

# Part 2, this was very hard for me
# Example visualization
# . . . . . . . S . . . . . . .
# . . . . . . . 1 . . . . . . .
# . . . . . . 1 ^ 1 . . . . . . # only one way to get to each spot
# . . . . . . 1 . 1 . . . . . . # still only one way to get to each spot
# . . . . . 1 ^ 2 ^ 1 . . . . .
# . . . . . 1 . 2 . 1 . . . . .
# . . . . 1 ^ 3 ^ 3 ^ 1 . . . .
# . . . . 1 . 3 . 3 . 1 . . . .
# . . . 1 ^ 4 ^ 3 3 1 ^ 1 . . .
# . . . 1 . 4 . 3 3 1 . 1 . . .
# . . 1 ^ 5 ^ 4 3 4 ^ 2 ^ 1 . .
# . . 1 . 5 . 4 3 4 . 2 . 1 . .
# . 1 ^ 1 5 4 ^ 7 4 . 2 1 ^ 1 .
# . 1 . 1 5 4 . 7 4 . 2 1 . 1 .
# 1 ^ 2 ^ 10 ^ 11 ^ 11 ^ 2 1 1 ^ 1


# Part 2: Count unique paths down the manifold
# Calculate all possible paths from the start (S) to the bottom
with open(file_path, 'r') as file:
    grid = []
    for line in file:
        line = line.strip()
        grid.append(list(line))

    last_row = []
    for i in range(len(grid)):
        row = grid[i]
        if i == 0:
            for j in range(len(row)):
                if row[j] == 'S':
                    row[j] = 1
        elif i != len(grid)-1:
            row_above = grid[i-1]
            for j in range(len(row)):
                if row_above[j] != '.' and row_above[j] != '^' and row[j] != '^':
                    if row[j] != '.':
                        row[j] += row_above[j]
                    else:
                        row[j] = row_above[j]
                elif row[j] == '^' and row_above[j] != '.':
                    if row[j-1] != '.':
                        row[j-1] += row_above[j]
                    else:
                        row[j-1] = row_above[j]
                    row[j+1] = row_above[j]
            last_row = row

    num_paths = 0
    for element in last_row:
        if isinstance(element, int):
            num_paths += element

    print(f"Number of unique paths from S to the bottom: {num_paths}")

#  Part 1: Count how many times the beam will be split
with open(file_path, 'r') as file:
    grid = []
    for line in file:
        line = line.strip()
        grid.append(list(line))

    # print(grid)
    split_count = 0
    for i in range(len(grid)):
        if i != len(grid)-1:
            row = grid[i]
            for j in range(len(row)):
                if row[j] == 'S':
                    # Start
                    grid[i+1][j] = '|'
                elif row[j] == '|':
                    # Check if there is a splitter beneath
                    if grid[i+1][j] == '^':
                        grid[i+1][j-1] = '|'
                        grid[i+1][j+1] = '|'
                        split_count += 1
                    else:
                        grid[i+1][j] = '|'

    print(f"Number of times the beam is split: {split_count}")
