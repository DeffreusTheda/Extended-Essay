import math
import statistics

def printt(s):
    print(s, end='\t')
def calculate(numbers):
    # print('data: ', end='')
    # for idx in range(len(numbers)):
    #     print(numbers[idx], end=(', ' if idx+1 != len(numbers) else '\n'))

    numbers = sorted(numbers)
    n = len(numbers)
    if n < 2:
        return 0  # Standard deviation is undefined for a single number

    Q1      = statistics.median(numbers[:n//2])
    Q2      = statistics.median(numbers)
    Q3      = statistics.median(numbers[n//2+(n&1):])
    IQR     = Q3 - Q1
    STD_DEV = math.sqrt(sum((x - (sum(numbers) / n)) ** 2 for x in numbers) / (n - 1))
 
    printt(f'{sum(numbers) / n}')             # AVG
    printt(f'{max(numbers) - min(numbers)}')  # RANGE
    printt(f'{statistics.median(numbers)}')   # MED
    printt(f'{statistics.mode(numbers)}')     # MODE
    printt(f'{Q1}')                           # Q1
    printt(f'{Q2}')                           # Q2
    printt(f'{Q3}')                           # Q3
    printt(f'{IQR}')                          # IQR
    printt(f'{statistics.variance(numbers)}') # VAR
    printt(f'{STD_DEV:.4f}')                  # STD_DEV
    for num in numbers:
        print((str(num)+',') if num < (Q1 - (1.5 * IQR)) or num > (Q3 + (1.5 * IQR)) else '', end='')
    print('\n')
    for num in numbers:
        print((str(num)+',') if num >= (Q1 - (1.5 * IQR)) and num <= (Q3 + (1.5 * IQR)) else '', end='')

# Get input from the user
numbers = []
input_num = {}
input_str = ''
while True:
    input_str = input("<data> [frequency]: ").strip()
    # Convert input string to a list of floats
    if input_str == '':
        break
    input_arr = input_str.split()
    if len(input_arr) > 2: 
        print(f'Warn: ignoring {input_arr[2:]}')
    if len(input_str.split()) > 1:
        input_str = input_str.split()
        input_num[float(input_str[0])] = int(input_str[1])
        continue
    try:
        input_num[float(input_str)] += 1
    except:
        input_num[float(input_str)] = 1
for data in sorted(input_num):
    for i in range(input_num[data]):
        numbers.append(data)

# Calculate and print the standard deviation
if len(numbers) < 2:
    print("At least two numbers are required to calculate standard deviation.")
    exit(1)

calculate(numbers)
