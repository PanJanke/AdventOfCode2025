#okropne podejście brute force, nie działa dla dużych case'ów, chciałem tworzyć wszysktie kombinacje
# dla współrzednej x, gdzie x to współrzędna występująca w najmniejszej liczbie przycisków, następnie rekurencyjnie
# wywoływać funkcję dla zredukowanej bazy przycisków i zredukowanego wektora. ilość kombinacji przerasta to podejście :<

from functools import lru_cache

def calculate_joltage(buttons, combination, length):
    result = [0] * length
    for i in range(len(combination)):
        btn = buttons[i]
        for b in btn:
            result[b] += combination[i]
    return tuple(result)

def generate_pruned_combinations(max_value, buttons, target_vector):
    results = []

    def backtrack(pos, remaining, current, partial_sum):
        if pos == len(buttons):
            if remaining == 0:
                results.append(tuple(current))
            return
        for coeff in range(remaining + 1):
            new_partial_sum = list(partial_sum)
            for b in buttons[pos]:
                new_partial_sum[b] += coeff
                if new_partial_sum[b] > target_vector[b]:
                    break
            else:
                backtrack(pos + 1, remaining - coeff, current + [coeff], new_partial_sum)
    backtrack(0, max_value, [], [0]*len(target_vector))
    return results

def button_base_creator(buttons):
    button_base = {}
    for b in buttons:
        for l in b:
            if l not in button_base:
                button_base[l] = []
            button_base[l].append(tuple(b))
    return button_base

def min_key_by_len(button_base):
    if not button_base:
        return None
    return min(button_base.keys(), key=lambda k: len(button_base[k]))

def subtract_vectors(v1, v2):
    return tuple(v1[i] - v2[i] for i in range(len(v1)))

def button_base_filtered(button_base, used_button):
    new_base = {}
    for k, blist in button_base.items():
        new_list = [b for b in blist if b != used_button]
        if new_list:
            new_base[k] = new_list
    return new_base


@lru_cache(maxsize=None)
def recur_p2_cached(button_base_keys, button_base_vals, joltage, depth, best_so_far):
    button_base = {k:list(v) for k,v in zip(button_base_keys, button_base_vals)}
    if best_so_far is not None and depth >= best_so_far:
        return best_so_far
    if all(j == 0 for j in joltage):
        return depth
    if not button_base:
        return best_so_far
    min_key = min_key_by_len(button_base)
    buttons = button_base[min_key]
    min_key_val = joltage[min_key]
    combinations = generate_pruned_combinations(min_key_val, buttons, joltage)

    best = best_so_far
    for comb in combinations:
        new_joltage = subtract_vectors(joltage, calculate_joltage(buttons[:len(comb)], comb, len(joltage)))
        new_base = button_base
        for b in buttons:
            new_base = button_base_filtered(new_base, b)
        new_keys = tuple(new_base.keys())
        new_vals = tuple(tuple(v) for v in new_base.values())
        result = recur_p2_cached(new_keys, new_vals, new_joltage, depth + sum(comb), best)
        if result is not None and (best is None or result < best):
            best = result
    return best

buttons = [[1, 6, 7], [0, 1, 3, 5, 9], [0, 4, 7, 8, 9], [1, 2, 5, 6, 9],
           [1, 3, 5, 6], [0, 1, 2, 3, 4, 5, 6, 9], [3, 4, 8], [3, 4], [0, 1, 2, 3, 4, 5, 8, 9],
           [1, 2, 4, 9], [2, 5, 6, 7, 8], [3, 8], [0, 7, 8, 9]]

joltage = [26, 75, 63, 62, 37, 69, 71, 31, 48, 55]

#buttons = [[3], [1,3], [2], [2,3], [0,2], [0,1]]


#joltage = [3,5,4,7]

button_base = button_base_creator(buttons)
button_keys = tuple(button_base.keys())
button_vals = tuple(tuple(v) for v in button_base.values())
#part_solution = recur_p2_cached(button_keys, button_vals, tuple(joltage), 0, None)
#print(part_solution)