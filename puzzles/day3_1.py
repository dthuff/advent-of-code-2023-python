import numpy as np
from scipy.signal import convolve2d
from itertools import groupby


def get_symbol_array(filepath):
    a = np.loadtxt(filepath, dtype=str)
    arr = np.zeros((len(a), len(a[0])))
    with open(filepath) as f:
        for i, line in enumerate(f):
            for j, char in enumerate(line.strip()):
                if not char.isnumeric() and not char == ".":
                    arr[i, j] = True
    return arr


def get_string_repr(filepath):
    s = ''
    with open(filepath) as f:
        for line in f:
            s += line.strip()

    return s


if __name__ == "__main__":
    symbol_array = get_symbol_array("../inputs/day3.txt")
    symbol_array = convolve2d(symbol_array, np.ones((3, 3)), 'same')
    symbol_vec = np.reshape(symbol_array, -1)
    symbol_vec_indices = np.where(symbol_vec > 0)[0]
    array = get_string_repr("../inputs/day3.txt")

    parts_sum = 0
    for i, c in enumerate(array):
        if c.isnumeric() and not array[i - 1].isnumeric():  # The start of a number
            this_number = c
            len_this_number = 1
            indices_of_this_number = [i]
            while array[i + len_this_number].isnumeric():
                this_number += array[i + len_this_number]
                indices_of_this_number.append(i + len_this_number)
                len_this_number += 1

            if set(indices_of_this_number) & set(symbol_vec_indices):
                parts_sum += int(this_number)

    print(f"The answer to day 3-1 is {parts_sum}")
