from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpInteger, PULP_CBC_CMD

# wynik za niski, robiłem reverse budująć zpowrotem joltage i sie zgadza, nie mam już siły szukać błędu.

# 1. relaxacja LP - solver szuka optymalnego rozkładu kliknięć, który spełnia wszystkie ograniczenia, nawet jeśli zmienne nie są całkowite.
# 2. Branch and Bound / Branch and Cut - CBC tworzy drzewo podproblemów: dla każdej zmiennej x_i, która nie jest całkowita, tworzy dwie gałęzie:
#       x_i ≤ floor(x_i)
#       x_i ≥ ceil(x_i)
# W każdej gałęzi ponownie rozwiązuje relaxację LP → sprawdza, czy możliwe jest poprawienie rozwiązania
# 3. Pruning - CBC odrzuca gałęzie, które nie mogą prowadzić do lepszego rozwiązania niż już znalezione.

def solve_min_clicks_ilp(buttons, joltage):
    n_buttons = len(buttons)
    n_coords = len(joltage)

    # Problem minimalizacji
    prob = LpProblem("MinButtonClicks", LpMinimize)

    # Zmienne: ile razy klikamy każdy przycisk
    click_vars = [LpVariable(f"click_{i}", lowBound=0, cat=LpInteger) for i in range(n_buttons)]

    # Ograniczenia: każda współrzędna musi być ≥ joltage
    for j in range(n_coords):
        prob += lpSum(click_vars[i] for i, btn in enumerate(buttons) if j in btn) >= joltage[j]

    # Cel: minimalna suma kliknięć
    prob += lpSum(click_vars)

    # Rozwiązanie
    prob.solve(PULP_CBC_CMD(msg=0))

    # Wynik
    clicks_result = [int(click_vars[i].varValue) for i in range(n_buttons)]
    total_clicks = sum(clicks_result)

    return total_clicks, clicks_result

buttons = [[1, 6, 7], [0, 1, 3, 5, 9], [0, 4, 7, 8, 9], [1, 2, 5, 6, 9],
           [1, 3, 5, 6], [0, 1, 2, 3, 4, 5, 6, 9], [3, 4, 8], [3, 4], [0, 1, 2, 3, 4, 5, 8, 9],
           [1, 2, 4, 9], [2, 5, 6, 7, 8], [3, 8], [0, 7, 8, 9]]

joltage = [26, 75, 63, 62, 37, 69, 71, 31, 48, 55]

print(solve_min_clicks_ilp(buttons, joltage))