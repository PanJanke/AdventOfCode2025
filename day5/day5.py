ranges = []
counter = 0
with open("../data/test.txt", "r") as file:
    for line in file:
        line = line.strip()
        if '-' in line:
            min_val, max_val = line.split('-')
            ranges.append((
                int(min_val.strip()),
                int(max_val.strip())
            ))
        elif len(line) > 0:
            for min, max in ranges:
                if min <= int(line.strip()) <= max:
                    counter += 1
                    break
print(counter)