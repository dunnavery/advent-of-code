from concurrent.futures import ThreadPoolExecutor
file_path = './puzzle-input.txt'

def is_point_in_polygon(point, vertices):
    num_intersections = 0
    num_vertices = len(vertices)
    px,py = point

    for i in range(num_vertices):
        v1 = vertices[i]
        v2 = vertices[(i+1) % num_vertices]

        v1x, v1y = v1
        v2x, v2y = v2

        # Edge check: is point on the segment
        if min(v1x, v2x) <= px <= max(v1x, v2x) and min(v1y, v2y) <= py <= max(v1y, v2y):
            dx = v2x - v1x
            dy = v2y - v1y
            if dx == 0: # vertical edge
                if px == v1x:
                    return True
            elif dy == 0: # horizontal edge
                if py == v1y:
                    return True
            else:
                # Check if point is on the line
                if (px - v1x) * dy == (py - v1y) * dx:
                    return True

        # Ray casting
        if ((v1y > py) != (v2y > py)):
            x_intersect = (v2x - v1x) * (py - v1y) / (v2y - v1y) + v1x
            if px < x_intersect:
                num_intersections += 1

    return num_intersections % 2 == 1


with open(file_path, 'r') as file:
    coordinates = []
    for line in file:
        line = line.strip().split(',')
        coordinates.append((int(line[0]), int(line[1])))

    red_coordinates = sorted(coordinates, key=lambda x: (x[0], x[1]))

    green_coordinates = set()
    for i in range(len(red_coordinates)):
        for j in range(i+1, len(red_coordinates)):

            x_1 = red_coordinates[i][0]
            y_1 = red_coordinates[i][1]
            x_2 = red_coordinates[j][0]
            y_2 = red_coordinates[j][1]

            if x_1 == x_2:
                for k in range(y_1+1, y_2):
                    green_coordinates.add((x_1, k))
                    print(f"Adding ({x_1}, {k}) to green coordinates")
            if y_1 == y_2:
                for k in range(x_1+1, x_2):
                    green_coordinates.add((k, y_1))
                    print(f"Adding ({k}, {y_1}) to green coordinates")

    border_coordinates = sorted(
        set(red_coordinates) | green_coordinates,
        key=lambda x: (x[0], x[1])
    )

    def process_pair(i, j):
        x_1, y_1 = red_coordinates[i]
        x_2, y_2 = red_coordinates[j]
        length = abs(x_2 - x_1) + 1
        width = abs(y_2 - y_1) + 1
        area = length * width
        if (
            is_point_in_polygon((x_1, y_2), border_coordinates) and
            is_point_in_polygon((x_2, y_1), border_coordinates)
        ):
            return area
        return 0

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(
            lambda args: process_pair(*args),
            [(i, j) for i in range(len(red_coordinates)) for j in range(i+1, len(red_coordinates))]
        ))

    max_area = max(results)
    print(f"Max area that can be made = {max_area}")

#     for i in range(len(red_coordinates)):
#         for j in range(i+1, len(red_coordinates)):
#             x_1 = red_coordinates[i][0]
#             y_1 = red_coordinates[i][1]
#             x_2 = red_coordinates[j][0]
#             y_2 = red_coordinates[j][1]
#
#             length = abs(x_2 - x_1) + 1
#             width = abs(y_2 - y_1) + 1
#             area = length * width
#
#             print(f"Red coordinates = ({x_1}, {y_1}), ({x_2}, {y_2}), Area = {area}")
#             print(f"Corners = ({x_1}, {y_2}), ({x_2}, {y_1})")
# #             print(f"Is ({x_1}, {y_2}) inside polygon? {is_point_in_polygon((x_1, y_2), border_coordinates)}")
# #             print(f"Is ({x_2}, {y_1}) inside polygon? {is_point_in_polygon((x_1, y_2), border_coordinates)}")
#             # print(f"Corners in green_coordinates or red coordinates: {(x_1, y_2) in green_coordinates or (x_1, y_2) in red_coordinates}, {(x_2, y_1) in green_coordinates or (x_2, y_1) in red_coordinates}")
#             if area > max_area:
#                 if is_point_in_polygon((x_1, y_2), border_coordinates) and is_point_in_polygon((x_1, y_2), border_coordinates):
#                     max_area = area

# Visualization
#     matrix = [['.' for _ in range(14)] for _ in range(9)]
#     print(red_coordinates)
#     for coord in red_coordinates:
#         matrix[coord[1]][coord[0]] = '#'
#
#     for coord in green_coordinates:
#         matrix[coord[1]][coord[0]] = 'X'
#
#     for coord in border_coordinates:
#         matrix[coord[1]][coord[0]] = '0'
#
#     # Need to visualize
#     for row in matrix:
#         print(''.join(row))

#     print(f"Max area that can be made = {max_area}")


