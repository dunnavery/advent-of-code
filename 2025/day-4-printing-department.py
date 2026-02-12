
file_path = './puzzle-input.txt'


def find_accessible_rolls(grid):
    accessible_rolls = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            roll = grid[row][col]
            # We can throw away zeros
            if roll == 0:
                continue

            adjacent_count = 0
            row_indices = [row-1, row, row+1]
            col_indices = [col-1, col, col+1]

            if row == 0:
                row_indices = [row, row+1]
            elif row == len(grid)-1:
                row_indices = [row-1, row]

            if col == 0:
                col_indices = [col, col+1]
            elif col == len(grid)-1:
                col_indices = [col-1, col]

            for row_idx in row_indices:
                for col_idx in col_indices:
                    if grid[row_idx][col_idx] > 0:
                        adjacent_count += 1

            adjacent_count -= 1
            if adjacent_count < 4:
                accessible_rolls += 1
                # Part 2: Remove accessible rolls
                grid[row][col] = 0

    return accessible_rolls


grid = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        row = []
        for roll in line:
            if roll == '.':
                row.append(0)
            if roll == '@':
                row.append(1)

        grid.append(row)

    accessible_rolls = find_accessible_rolls(grid)
    print(f"Accessible rolls = {accessible_rolls}") # Part 1: Just rolls that can be removed
    removed_rolls = accessible_rolls

    # Part 2: Continue to remove rolls until none can be removed
    while accessible_rolls > 0:
        accessible_rolls = find_accessible_rolls(grid)
        removed_rolls += accessible_rolls

    print(f"Removed rolls = {removed_rolls}")
