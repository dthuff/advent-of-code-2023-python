import numpy as np

counter = 0
with open("../inputs/day1.txt") as f:
    for line in f:
        ind = [a for a in line if a.isnumeric()]
        counter += int(ind[0] + ind[-1])
print(f"The answer for part 1 is: {counter}")
