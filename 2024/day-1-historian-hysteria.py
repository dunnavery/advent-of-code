
file_path = './puzzle-input.txt'

# Part 1: Take difference of two sorted lists
with open(file_path, 'r') as file:
    left_list = []
    right_list = []
    for line in file:
        line = line.strip()
        line = line.split('   ')
        left_list.append(int(line[0]))
        right_list.append(int(line[1]))

    left_list = sorted(left_list)
    right_list = sorted(right_list)
    total_distance = 0

    # Part 1, sort the lists and compare items
    for i in range(len(left_list)):
        distance = 0
        if left_list[i] < right_list[i]:
            distance = right_list[i] - left_list[i]
        elif left_list[i] > right_list[i]:
            distance = left_list[i] - right_list[i]
        total_distance += distance

    # Part 2, determine how many of each number in the left list appears in
    # the right list and calculate similarity score
    similarity_score = 0
    similarity_count = {}
    for i in range(len(left_list)):
        if left_list[i] not in similarity_count:
            similarity_count[left_list[i]] = 0
        for j in range(len(right_list)):
            if left_list[i] == right_list[j]:
                similarity_count[left_list[i]] += 1

    for key in similarity_count:
        similarity_score += key * similarity_count[key]

    print(f"Total distance between the lists: {total_distance}") # Part 1
    print(f"Similarity score = {similarity_score}") # Part 2
