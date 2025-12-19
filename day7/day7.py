lines = []
lasers = []
with open("../data/test.txt", "r") as file:
    for line in file:
        lines.append(line.rstrip())

lasers.append(lines[0].find('S'))
lines.pop(0)
counter = 0
for line in lines:
    splitters = [i for i, c in enumerate(line) if c == '^']
    indexes_of_split = list(set(lasers) & set(splitters))
    for index in indexes_of_split:
        lasers.remove(index)
        lasers.append(index+1)
        lasers.append(index-1)
        counter += 1
    lasers = list(set(lasers))
    for i in lasers:
         line = line[:i] + '|' + line[i+1:]
    print(line)
print(counter)
