from collections import deque

#BFS też za wolny lmao

buttons = [[3], [1,3], [2], [2,3], [0,2], [0,1]]
joltage = [3,5,4,7]

def bfs_min_clicks(joltage, buttons):
    start = tuple(joltage)
    queue = deque([(start, 0)])  # (current_joltage, clicks_so_far)
    visited = set()
    visited.add(start)

    while queue:
        current, clicks = queue.popleft()

        if all(x == 0 for x in current):
            return clicks

        for btn in buttons:
            next_state = list(current)
            for i, val in enumerate(btn):
                next_state[val] -= 1
                if next_state[val] < 0:
                    break
            else:
                next_state_tuple = tuple(next_state)
                if next_state_tuple not in visited:
                    visited.add(next_state_tuple)
                    queue.append((next_state_tuple, clicks + 1))
    return None