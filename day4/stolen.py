InputList = []
with open("../data/test.txt", "r") as data:
    for t in data:
        Line = t.strip()
        InputList.append(Line)

OriginalRollSet = set()
for y, f in enumerate(InputList):
    for x, c in enumerate(f):
        if c == "@":
            OriginalRollSet.add((x, y))

RollSet = OriginalRollSet.copy()
Part1Answer = 0
Part2Answer = 0
Part1 = True
while True:
    RemoveSet = set()
    for R in RollSet:
        RX, RY = R
        CheckSet = set()
        for DX, DY in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
            NX, NY = RX + DX, RY + DY
            CheckSet.add((NX, NY))
        NeighborSet = RollSet & CheckSet
        if len(NeighborSet) < 4:
            Part2Answer += 1
            RemoveSet.add(R)
    RollSet = RollSet - RemoveSet
    if Part1:
        Part1Answer = Part2Answer
    Part1 = False
    if len(RemoveSet) == 0:
        break

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")