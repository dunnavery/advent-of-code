
file_path = './puzzle-input.txt'

with open(file_path, 'r') as file:
    # Part 1: Determine how many available ingredients are fresh
    fresh_ingredients = []
    available_ingredients = [] # For Part 1: List of available ingredients
    tmp_array = fresh_ingredients
    for line in file:
        line = line.strip()
        if not line:
            tmp_array = available_ingredients
            continue
        tmp_array.append(line)

    for i in range(len(fresh_ingredients)):
        ing_range = fresh_ingredients[i].split('-')
        tmp_range = [int(ing_range[0]), int(ing_range[1])]
        fresh_ingredients[i] = tmp_range

    available_ingredients = [int(ingredient) for ingredient in available_ingredients]
    fresh_count = 0

    # Part 1: Count how many available ingredients are fresh
    total_fresh_ingredients = set()
    for ingredient in available_ingredients:
        for ingredient_range in fresh_ingredients:
            if ingredient_range[0] <= ingredient <= ingredient_range[1]:
                fresh_count += 1
                break

    # Part 2: Determine how many total fresh ingredients there are
    # Sort ingredient ranges first by first element, then by second element
    sorted_ingredient_ranges = sorted(fresh_ingredients, key=lambda x: (x[0], x[1]))

    total_fresh_count = 0
    min_i = sorted_ingredient_ranges[0][0] # example: 3
    max_i = sorted_ingredient_ranges[0][1] # example: 5
    print(f"Min = {min_i} Max = {max_i}")
    for ingredient_range in sorted_ingredient_ranges[1:]:
        if min_i <= ingredient_range[0] <= max_i:
            if ingredient_range[1] >= max_i:
                max_i = ingredient_range[1]
        else:
            total_fresh_count += max_i - min_i + 1
            min_i = ingredient_range[0]
            max_i = ingredient_range[1]

        print(ingredient_range)
        print(f"Min = {min_i} Max = {max_i}")
        print(f"Fresh count = {total_fresh_count}")

    total_fresh_count += max_i - min_i + 1

    print(f"Available ingredients that are fresh = {fresh_count}")
    print(f"Count of ingredient IDs considered fresh = {total_fresh_count}")
