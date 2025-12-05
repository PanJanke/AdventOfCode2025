with open("../data/test.txt", "r") as f:
    grid = [list(line.strip()) for line in f]


rows = len(grid)
cols = len(grid[0])
print(f"Rows: {rows}, Cols: {cols}")


dirs = [(-1,-1), (-1,0), (-1,1),
        (0,-1),         (0,1),
        (1,-1),  (1,0), (1,1)]

adj_count = [[0]*cols for _ in range(rows)]  # same shape as grid

for y in range(rows):
    for x in range(cols):
        if grid[y][x] == '@':
            count = 0
            for dr, dc in dirs:
                new_y, new_x = y + dr, x + dc
                if 0 <= new_y < rows and 0 <= new_x < cols:
                    if grid[new_y][new_x] == '@':
                        count += 1
            adj_count[y][x] = count

for row in adj_count:
    print(row)

total = sum(1 for row in adj_count for v in row if (0 < v < 4))
print(total)