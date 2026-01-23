from itertools import combinations

points = []

with open("../data/test.txt", "r") as file:
    for line in file:
        points.append([int(x) for x in line.rstrip().split(',')])
max = 0
for p1, p2 in combinations(points, 2):
    x_len = abs(p1[0]-p2[0]) + 1
    y_len = abs(p1[1]-p2[1]) + 1
    if x_len * y_len > max:
        max = x_len * y_len
print(max)