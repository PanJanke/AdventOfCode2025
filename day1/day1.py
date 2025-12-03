def next_position(direction,num_of_ticks,current_pos):
    if direction == 'L':
        current_pos = (current_pos - num_of_ticks) % 100
        if current_pos < 0:
            current_pos += 100
    elif direction == 'R':
        current_pos = (current_pos + num_of_ticks) % 100
    return current_pos
zero_counter = 0
position = 50

with open('../data/day1.txt', 'r') as f:
    for  line in f:
        line = line.rstrip('\n')
        position = next_position(line[0], int(line[1:]), position)
        print(position)
        if position == 0:
            zero_counter += 1
print(zero_counter)
