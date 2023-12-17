from itertools import cycle
from math import lcm

from day8_1 import load_data, next_node

if __name__ == "__main__":
    instructions, nodes = load_data("../inputs/day8.txt")

    starting_nodes = [node for node in nodes if node[-1] == "A"]
    step_counts = []

    for idx, node in enumerate(starting_nodes):
        step_counter = 0
        instruction_gen = cycle(instructions)

        while node[-1] != "Z":
            node = next_node(nodes, node, next(instruction_gen))
            step_counter += 1
        step_counts.append(step_counter)

    print(f"The answer to day 8-2 is {lcm(*step_counts)}")
