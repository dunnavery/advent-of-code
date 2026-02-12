file_path = './puzzle-input.txt'

# Part 1: Determine safe reports vs unsafe reports
def is_report_safe(report):
    """
    Report is safe if all numbers of the array are increasing or decreasing
    and there is no difference greater than 3
    """

    if all(report[i] <= report[i+1] and 1 <= (report[i+1]-report[i]) <= 3 for i in range(len(report)-1)):
        return True
    if all(report[i] >= report[i+1] and 1 <= (report[i]-report[i+1]) <= 3 for i in range(len(report)-1)):
        return True
    
    return False


# Part 2: Report is safe if it could be safe if one element were removed
def temporary_remove(arr, idx_to_remove):
    new_arr = arr[:idx_to_remove] + arr[idx_to_remove+1:]
    return new_arr


with open(file_path, 'r') as file:
    reports = []
    for line in file:
        line = line.strip().split(' ')
        levels = [int(level) for level in line]
        reports.append(levels)
    
    safe_count = 0
    unsafe_count = 0
    for report in reports:
        i = 0
        is_safe = False
        while i < len(report):
            new_report = temporary_remove(report, i)
            i += 1
            if is_report_safe(new_report):
                is_safe = True

        if is_safe:
            safe_count += 1
        else:
            unsafe_count += 1
    
    print(f"Safe count = {safe_count}")
    print(f"Unsafe count = {unsafe_count}")
