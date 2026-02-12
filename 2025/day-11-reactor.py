
file_path = './puzzle-input.txt'

# Part 1: Recursive devices
devices = {}
with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        line = line.split(':')
        devices[line[0]] = []
        connected_devices = line[1].strip().split(' ')
        for device in connected_devices:
            devices[line[0]].append(device)

def traverse_devices(device, devices):
    global out_count
    global fft_count
    global dac_count
    global fft_and_dac_count
    next_devices = devices[device]
    print(next_devices)
    if 'fft' in next_devices:
        fft_count += 1
    if 'dac' in next_devices:
        dac_count += 1
    if 'out' in next_devices:
        out_count += 1
        if fft_count and dac_count:
            fft_and_dac_count += 1
        return
    for next_device in next_devices:
        traverse_devices(next_device, devices)

start_devices = devices['you'] # Part 1: starts at 'you' and goes to 'out'
# Part 2: Starts at 'svr'
# start_devices = devices['svr']

# Must also visit 'dac' and 'fft'
out_count = 0
fft_and_dac_count = 0
for device in start_devices:
    memo = set()
    fft_count = 0
    dac_count = 0
    traverse_devices(device, devices)

print(f"FFT and DAC count: {fft_and_dac_count}")
print(f"Out count: {out_count}")






