import math

def try_int(x):
    try:
        return int(x)
    except ValueError:
        return x

ranges = []
counter = 0
each_line = []
with open("../data/test.txt", "r") as file:
    for line in file:
        line = line.split(' ')
        symbols = []
        for symbol in line:
            symbol = symbol.rstrip().lstrip()
            if symbol is not None and len(symbol) > 0:
                symbols.append(symbol)
        each_line.append(symbols)
        symbols = []

results = []
transposed = [list(col) for col in zip(*each_line)]
transposed = [
    [try_int(item) for item in col]
    for col in transposed
]
for line in transposed:
    operation = line[-1]
    print(line)
    if operation == '*':
        results.append(math.prod(line[:-1]))

    elif operation == '+':
        results.append(sum(line[:-1]))
print(results)
print(sum(results))