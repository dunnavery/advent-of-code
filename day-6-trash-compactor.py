
file_path = './puzzle-input.txt'

# PART 2: Vertically add or multiply the individual digits read from right to left (just account for spaces)
# and calculate the grand total by adding the solutions per column
with open(file_path, 'r') as file:
    grid = []
    for line in file:
        grid.append(line)

    operators = grid[-1]
    numbers = grid[:-1]

    max_length = len(max(grid, key=len))
    operators = operators.ljust(max_length) # Fill the rest of the operators row with spaces

    operator = ''
    current_total = 0 # To keep a running total
    grand_total = 0 # To calculate the grand total per column

    for i in range(len(operators)):
        if operators[i] != ' ':
            operator = operators[i]
            solution = 1 if operators[i] == '*' else 0
            # Update grand total, since we are at a new column
            grand_total += current_total
            current_total = 1 if operators[i] == '*' else 0

        products = []
        product = ''

        for row in numbers:
            row = row.replace('\n', '')
            row = row.ljust(max_length) # Make all rows the same width

            if row[i] == ' ':
                product = ''.join(products)
                if product:
                    if operator == '*':
                        current_total *= int(product)
                    else:
                        current_total += int(product)
                products = []
            else:
                products.append(row[i])

        product = ''.join(products)
        if product:
            if operator == '*':
                current_total *= int(product)
            else:
                current_total += int(product)

    grand_total += current_total
    print(f'AND THE GRAND TOTAL IS = {grand_total}')


# Part 1: Vertically add or multiply numbers together
with open(file_path, 'r') as file:
    grid = []
    for line in file:
        line = line.split()
        grid.append(line)

    numbers = grid[:-1]
    operators = grid[-1]

    grand_total = 0

    for i in range(len(operators)):
        solution = 1 if operators[i] == '*' else 0
        for row in numbers:
            if operators[i] == '*':
                solution *= int(row[i])
            elif operators[i] == '+':
                solution += int(row[i])

        grand_total += solution

    print(f"Grand total = {grand_total}")
