lines = []
lasers = {}
# pascal triangle approach
with open("../data/day3.txt", "r") as file:
    for line in file:
        lines.append(line.rstrip())

start_idx = lines[0].find('S')
lasers = {start_idx: 1}
lines.pop(0)
counter = 0
for line in lines:
    splitters = [i for i, c in enumerate(line) if c == '^']
    new_lasers = {}

    for idx, value in lasers.items():
        if idx in splitters:
            for new_idx in (idx - 1, idx + 1):
                    new_lasers[new_idx] = new_lasers.get(new_idx, 0) + value
        else:
            new_lasers[idx] = new_lasers.get(idx, 0) + value
    lasers = new_lasers
print(sum(lasers.values()))