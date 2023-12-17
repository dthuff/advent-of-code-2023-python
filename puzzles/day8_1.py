from itertools import cycle


def load_data(path):
    with open(path) as f:
        instructions, _, *nodes = f.readlines()
    instructions = [a for a in instructions.strip()]
    nodes_out = {}
    for node in nodes:
        node = ''.join(c for c in node if c not in '()=\n,').split(" ")
        nodes_out[node[0]] = (node[2], node[3])
    return instructions, nodes_out


def next_node(node_dict, curr_node, instruction):
    if instruction == "L":
        return node_dict[curr_node][0]
    else:
        return node_dict[curr_node][1]


if __name__ == "__main__":
    instructions, nodes = load_data("../inputs/day8.txt")

    current_node = "AAA"
    instruction_gen = cycle(instructions)
    step_counter = 0
    while current_node != "ZZZ":
        current_node = next_node(nodes, current_node, next(instruction_gen))
        step_counter += 1

    print(f"The answer to day 8-1 is {step_counter}")
