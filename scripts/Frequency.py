import math
import statistics

def printt(s):
    print(s, end='\t')

frequencies = {key: 0 for key in range(300)}
# Get input from the user
numbers = []
while True:
    input_str = input("<data>: ").strip()
    if input_str == '':
        break
    frequencies[int(input_str)] += 1
for idx, key in enumerate(frequencies):
    if frequencies[key] > 0:
        numbers.append((idx, frequencies[key]))
for idx, val in numbers:
    print(f'{idx}: {val}')
