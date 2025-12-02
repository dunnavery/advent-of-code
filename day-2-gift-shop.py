
file_path = "./puzzle-input.txt"

invalid_ids = []

def split_array_by_size(arr, k):
    subarrays = []
    for i in range(0, len(arr), k):
        subarrays.append(arr[i:i+k])
    return subarrays

try:
    with open(file_path, 'r') as file:
        for line in file:
            line_arr = line.split(',')
            for id_range in line_arr:
                id_range = id_range.split('-')
                bottom = int(id_range[0])
                top = int(id_range[1])

                for i in range(bottom, top+1):
                    id = str(i)
                    subarrays = subarrays = split_array_by_size(id, len(set(id)))
                    if len(id)%2 == 0: # Part 1: ids only sequence of digits repeated twice
                        half = int(len(id)/2)
                        first_half = id[:half]
                        second_half = id[half:]
                        if id[:half] == id[half:]:
                            invalid_ids.append(int(id))
                        else:
                            if len(subarrays) > 1:
                                if len(set(subarrays)) == 1:
                                    invalid_ids.append(int(id))
                    else: # Part 2: sequence of digits repeated AT LEAST twice
                        if len(subarrays) > 1:
                            if len(set(subarrays)) == 1:
                                invalid_ids.append(int(id))

    print(f"The invalid IDs add up to: {sum(invalid_ids)}")

except FileNotFoundError:
    print(f"Error: the file path was not found")
except Exception as e:
    print(f"An error occurred: {e}")

