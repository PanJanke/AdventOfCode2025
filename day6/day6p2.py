import math

ranges = []
counter = 0
each_line = []
with open("../data/day3.txt", "r") as file:
  matrix = [list(line.rstrip()) for line in file]


max_len = max(len(line) for line in matrix)
for line in matrix:
    while len(line) < max_len:
        line.append(' ')
num_in_col = []
results = []
for x in range(max_len-1, -1, -1):
    num = 0
    for y in range(len(matrix)-1):
        if matrix[y][x] != ' ':
            if num == 0:
                num = int(matrix[y][x])
            else:
                num = num * 10 + int(matrix[y][x])
    if num != 0:
        num_in_col.append(num)

    if matrix[-1][x] == '*':
        results.append(math.prod(num_in_col))
        num_in_col = []
    elif matrix[-1][x] == '+':
        results.append(sum(num_in_col))
        num_in_col = []

print(sum(results))
