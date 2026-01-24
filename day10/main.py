from .day10 import recur
from pathlib import Path


def button_base_creator(buttons):
    button_base = {}
    for b in buttons:
        for l in b:
            if l not in button_base:
                button_base[l] = []
            button_base[l].append(b)
    return button_base


def lights_to_btn(lights):
    btn = []
    for i, l in enumerate(lights):
        if l == '#':
            btn.append(i)
    return btn


def buttons_list(input):
    buttons = []
    for b in input:
        b = b[1:len(b) - 1]
        button = b.split(',')
        button = [int(x) for x in button]
        buttons.append(button)
    return buttons


sum = 0

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR.parent / "data" / "test.txt"

with open(DATA_FILE, "r") as file:
    for line in file:
        data = line.rstrip().split(' ')
        lights = data[0]
        buttons = data[1:len(data) - 1]
        joltage = data[len(data) - 1]
        lights = lights_to_btn(lights[1:len(lights) - 1])
        buttons = buttons_list(buttons)
        button_base = button_base_creator(buttons)
        part_solution = recur(buttons, button_base, lights, 0, None)
        sum += part_solution
print(f"Solution p1: {sum}")
