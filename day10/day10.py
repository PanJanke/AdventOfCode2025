def press_button(button, light):
    new_light = light.copy()
    for b in button:
        if b in new_light:
            new_light.remove(b)
        else:
            new_light.append(b)
    return sorted(new_light)


def print_button_base(button_base: dict) -> None:
    for key, lst in button_base.items():
        print(f"{key}: {lst}")


def button_base_filtered(button_base: dict, b) -> dict[int, list]:
    new_button_base = {}
    for key, lst in list(button_base.items()):
        filtered = [btn for btn in lst if btn != b]
        if filtered:
            new_button_base[key] = filtered
    return new_button_base


def recur(buttons, button_base, lights, depth, best_so_far):
    # PRUNING
    if best_so_far is not None and depth >= best_so_far:
        # print(f"Pruned at depth {depth}")
        return None

    # rozwiązanie
    if lights in buttons:
        steps = depth + 1
        # print(f"Solved in {steps} steps")
        return steps

    if not buttons:
        return None

    min_len = float("inf")
    min_key = None

    for l in lights:
        if l not in button_base:
            # print(f"Light {l} cannot be turned off anymore")
            return None

        if len(button_base[l]) < min_len:
            min_len = len(button_base[l])
            min_key = l

    best = best_so_far

    for b in button_base[min_key]:

        result = recur(
            [btn for btn in buttons if btn != b],
            button_base_filtered(button_base, b),
            press_button(b, lights),
            depth + 1,
            best
        )
        # print(f"Backtracking from depth {depth} after trying button {b}")

        if result is not None:
            if best is None or result < best:
                best = result

    return best
