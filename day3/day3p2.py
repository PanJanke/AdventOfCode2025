def create_digit_map(line):
    digit_map = {}
    for i, ch in enumerate(line):
        if ch not in digit_map:
            digit_map[ch] = []
        digit_map[ch].append(i)
    return digit_map

def find_max_twelve_digits_number(s):
    final_num = ''
    digit_counter = 12
    a = max(s)
    while digit_counter > 0:
        digit_map = create_digit_map(s)
        pos_a = digit_map[a][0]
        if len(s) - pos_a >= digit_counter:
            final_num += a
            digit_counter -= 1
            if digit_counter == 0: # to avoid lunch max() on empty string, ugly but works
                break
            s = s[pos_a + 1:]
            a = max(s)
        else:
            a = max(s[:pos_a])
    print(final_num)
    return int(final_num)

result = 0
with open('../data/day3.txt', 'r') as f:
    sum = 0
    for line in f:
        line = line.rstrip('\n')
        sum += find_max_twelve_digits_number(line)
    print(sum)





