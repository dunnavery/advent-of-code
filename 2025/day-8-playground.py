
import bisect
import math
import networkx as nx

G = nx.Graph()

file_path = './puzzle-input.txt'

# Part 1: Graph problem, connect 1000 junction boxes together that are the least distance away
with open(file_path, 'r') as file:
    junction_boxes = []
    for line in file:
        box = line.strip().split(',')
        box = [int(dim) for dim in box]
        junction_boxes.append(tuple(box))

    G.add_nodes_from(junction_boxes)

    connections = {}
    min_distance = math.inf
    min_edges = []
    for i in range(len(junction_boxes)):
        for j in range(i+1, len(junction_boxes)):
            first_box = junction_boxes[i]
            second_box = junction_boxes[j]

            x_1 = first_box[0]
            y_1 = first_box[1]
            z_1 = first_box[2]

            x_2 = second_box[0]
            y_2 = second_box[1]
            z_2 = second_box[2]

            distance = math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2 + (z_1 - z_2)**2)
            connections[(tuple(first_box), tuple(second_box))] = distance

    connections = sorted(connections.items(), key=lambda item: item[1])
    # connections = connections[:1000] # Part 1: connect 1000 boxes together that are the least distance away

    # Part 2: Connect ALL junction boxes together
    for connection in connections:
        if nx.number_connected_components(G) > 1:
            G.add_edge(connection[0][0], connection[0][1])
            if nx.number_connected_components(G) == 1:
                print(f"All graph components now connected, X times X = {connection[0][0][0] * connection[0][1][0]}")
        if nx.number_connected_components(G) == 1:
            break

        G.add_edge(connection[0][0], connection[0][1])

    # Part 1: First thousand closest junction boxes
    # Multiply together the three largest connections
    three_largest_circuits = []
    for i in list(nx.connected_components(G)):
        bisect.insort(three_largest_circuits, len(i))

    three_largest_circuits = three_largest_circuits[-3:]
    largest_circuits = 1
    for size in three_largest_circuits:
        largest_circuits *= size

    print(f"The three largest circuits multiplied is: {largest_circuits}")
