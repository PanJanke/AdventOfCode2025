def merge_ranges(ranges):
    ranges = sorted(ranges)# sort by first element - min , if ties , sort by max
    merged = []

    for start, end in ranges:
        if not merged or start > merged[-1][1] + 1: #array[-1] means last element
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return merged

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
ranges = merge_ranges(ranges)
print(ranges)
for min, max in ranges:
    counter += (max - min + 1)
print(counter)