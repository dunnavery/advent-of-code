import ast
from itertools import combinations
import math
import numpy as np

file_path = './puzzle-input.txt'

with open(file_path, 'r') as file:
    machines = []
    for line in file:
        # machine = line.strip().split(' ')[:-1] # Part 1, we don't care about joltage
        machine = line.strip().split(' ') # Part 1, now we care about joltage
        machines.append(machine)

    total_button_presses = 0

    for machine in machines:
        indicator_lights = machine[0]
        button_inputs = machine[1:-1] # We care about joltage
        joltage_counter = machine[-1]
        joltage_counter = ast.literal_eval(joltage_counter.replace('{', '[').replace('}', ']'))


        indicator_lights = [1 if light == '#' else 0 for light in indicator_lights]
        indicator_lights = indicator_lights[1:-1]
        print(f"Indicator lights: {indicator_lights}")
        button_inputs = [ast.literal_eval(button) for button in button_inputs]
        print(f"Button inputs: {button_inputs}")
        joltage = [int(joltage_count) for joltage_count in joltage_counter]
        print(f"Joltage: {joltage}")

        start = [0 for i in range(len(indicator_lights))]
        start_joltage = start.copy()

        # Part 2: Now we only care about joltage count
        button_inputs = sorted(button_inputs, key=lambda x: len(x) if not isinstance(x, int) else 1, reverse=True)

        joltage = np.array(joltage)
        start_joltage = np.array(start_joltage)

        for buttons in button_inputs:
            if not isinstance(buttons, tuple):
                # Single press
                if start_joltage[buttons] < joltage[buttons]:
                    start_joltage[buttons] += 1
            else:

                buttons = list(buttons)
                print(f"buttons: {buttons}")

                while all(start_joltage[buttons] < joltage[buttons]):
                    print("here")
                    start_joltage[buttons] += 1
                    print(start_joltage)

            # print(f"start joltage = {start_joltage}, joltage={joltage}")
            if all(start_joltage == joltage):
                print(f"start joltage = {start_joltage}, joltage={joltage}")
                print("DONE")
            print(start_joltage)



#         # Part 1: Get fewest number of combinations
#         all_combinations = []
#         min_combination = math.inf
#         for i in range(1, len(button_inputs)+1):
#             all_combinations.extend(list(combinations(button_inputs, i)))
#
#         for combination in all_combinations:
#             for button in combination:
#                 if not isinstance(button, tuple): # Just one flip
#                     start[button] = 0 if start[button] == 1 else 1
#                 else:
#                     for press in button:
#                         start[press] = 0 if start[press] == 1 else 1
#
#             if start == indicator_lights:
#                 if len(combination) < min_combination:
#                     min_combination = len(combination)
#                     print(f"{start} = {indicator_lights} with buttons: {combination}, length = {len(combination)}")
#             else:
#                 start = [0 for i in range(len(indicator_lights))]
#
#         total_button_presses += min_combination
#
#     print(f"Fewest total button presses = {total_button_presses}")
