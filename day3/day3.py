def find_max_two_digits_number(line):
    digit_map = {}
    for i, ch in enumerate(line):
        if ch not in digit_map:
            digit_map[ch] = []
        digit_map[ch].append(i)
    a = max(line)
    pos_a = digit_map[a][0]
    if pos_a != len(line) - 1:
        b = max(line[pos_a + 1:])
        return str(a+b)
    else:
        b = max(line[:pos_a])
        return str(b+a)

result = 0
with open('../data/day3.txt', 'r') as f:
    sum = 0
    for line in f:
        line = line.rstrip('\n')
        sum += int(find_max_two_digits_number(line))
    print(sum)





