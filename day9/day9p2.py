from itertools import combinations
from scipy.spatial import ConvexHull
import numpy as np
def is_point_in_rectangle(p0, p1, p2, p3, p4):

    if abs(p1[0]-p2[0]) == 0 or abs(p1[1]-p2[1]) == 0:
        return False

    xs = [p1[0], p2[0], p3[0], p4[0]]
    ys = [p1[1], p2[1], p3[1], p4[1]]

    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)

    x, y = p0
    return x_min < x < x_max and y_min < y < y_max


points = []

with open("../data/test.txt", "r") as file:
    for line in file:
        points.append([int(x) for x in line.rstrip().split(',')])


base_hull = ConvexHull(points)
max_ = 0


for p1, p2 in combinations(points, 2):
    p3 = [p1[0],p2[1]]
    p4 = [p2[0],p1[1]]
   # print(p1,p2,p3,p4)
    x_len = abs(p1[0]-p2[0]) + 1
    y_len = abs(p1[1]-p2[1]) + 1
    new_points = points + [p3, p4]
    new_points = [
        p for p in new_points
        if not is_point_in_rectangle(p, p1, p2, p3, p4)
    ] 
    new_hull = ConvexHull(new_points)
    if x_len * y_len > max_ and set(base_hull.vertices) == set(new_hull.vertices):
        max_ = x_len * y_len
print(max_)