with open("../data/test2.txt", "r") as f:
    grid = [list(line.strip()) for line in f]


rows = len(grid)
cols = len(grid[0])
print(f"Rows: {rows}, Cols: {cols}")


dirs = [(-1,-1), (-1,0), (-1,1),
        (0,-1),         (0,1),
        (1,-1),  (1,0), (1,1)]

adj_count = [[0]*cols for _ in range(rows)]  # same shape as grid
counter=0
sum_of_total = 0
while True:
    for y in range(cols):
        for x in range(rows):
            if grid[y][x] == '@':
                count = 0
                for dr, dc in dirs:
                    new_y, new_x = y + dr, x + dc
                    if 0 <= new_y < rows and 0 <= new_x < cols:
                        if grid[new_y][new_x] == '@':
                            count += 1
                adj_count[y][x] = count

    total = 0
    for y in range(cols):
        for x in range(rows):
            if grid[y][x] == '@' and adj_count[y][x] < 4:
                grid[y][x] = 'x'
                total += 1
            elif grid[y][x] == 'x':
                grid[y][x] = '.'

    if total == 0:
        break

    sum_of_total += total
    print(f"======total: {total}")
    #for row in grid:
        #print(row)



print(sum_of_total)