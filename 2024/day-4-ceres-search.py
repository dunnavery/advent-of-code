
file_path = './puzzle-input.txt'

with open(file_path, 'r') as file:
    stream = file.read().splitlines()
    print(''.join(stream))

    chars = [s[i] for s in stream for i in range(len(stream[0]))]
    print(chars)

