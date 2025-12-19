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
points.remove(distances[0]["point_a"])
points.remove(distances[0]["point_b"])
distances.pop(0)
for item in distances:
    a = item["point_a"]
    b = item["point_b"]
    idx_a = idx_of_circuit_contains_point(a, circuits)
    idx_b = idx_of_circuit_contains_point(b, circuits)
    if idx_a == -1 and idx_b == -1:
        circuits.append([a, b])
        points.remove(a)
        points.remove(b)
    elif idx_a != -1 and idx_b == -1:
        circuits[idx_a].append(b)
        points.remove(b)
    elif idx_a == -1 and idx_b != -1:
        circuits[idx_b].append(a)
        points.remove(a)
    elif idx_a != idx_b:
        circuits[idx_a].extend(circuits[idx_b])
        circuits.pop(idx_b)

    if(len(circuits) == 1 and not points):
        print(a[0]*b[0])
        break
