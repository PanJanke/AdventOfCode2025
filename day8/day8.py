from math import sqrt

def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

def idx_of_circuit_contains_point(point, circuits_):
    for i in range(len(circuits_)):
        circuit = circuits_[i]
        if point in circuit:
            return i
    return -1

points = []
distances = []
circuits = []
with open("../data/test.txt", "r") as file:
    for line in file:
        points.append([int(x) for x in line.rstrip().split(',')])

for i in range(len(points)):
    for j in range(i+1, len(points)):
        d = distance(points[i], points[j])
        distances.append({
            "distance": d,
            "point_a": points[i],
            "point_b": points[j]
        })
distances = sorted(distances, key=lambda x: x["distance"])
circuits.append([distances[0]["point_a"], distances[0]["point_b"]])
distances.pop(0)
for item in distances[:999]:
    a = item["point_a"]
    b = item["point_b"]
    idx_a = idx_of_circuit_contains_point(a, circuits)
    idx_b = idx_of_circuit_contains_point(b, circuits)
    if idx_a == -1 and idx_b == -1:
        circuits.append([a, b])
    elif idx_a != -1 and idx_b == -1:
        circuits[idx_a].append(b)
    elif idx_a == -1 and idx_b != -1:
        circuits[idx_b].append(a)
    elif idx_a != idx_b:
        circuits[idx_a].extend(circuits[idx_b])
        circuits.pop(idx_b)

circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
result = 1
for i in range(3):
    result *= len(circuits[i])
print(result)
