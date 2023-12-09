import numpy as np

counter = 0
with open("../inputs/day1.txt") as f:
    for line in f:
        ind = [a for a in line if a.isnumeric()]
        counter += int(ind[0] + ind[-1])
print(f"The answer for part 1 is: {counter}")

counter2 = 0
numbers_dict = {"one": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5,
                "six": 6,
                "seven": 7,
                "eight": 8,
                "nine": 9}

with open("../inputs/day1.txt") as f:
    for line in f:
        numeric_ind = np.where([a.isnumeric() for a in line])[0]
        numerics = [a for a in line if a.isnumeric()]
        line_answer = 0
        first_digit_position = 10000
        for key, value in numbers_dict.items():
            dd = line.find(key)
            if dd > -1:
                if dd < first_digit_position:
                    first_digit = str(value)
                    first_digit_position = dd

        last_digit_position = -1
        for key, value in numbers_dict.items():
            dd = line.rfind(key)
            if dd > -1:
                if dd > last_digit_position:
                    last_digit = str(value)
                    last_digit_position = dd

        if numeric_ind[0] < first_digit_position:
            first_digit = str()
        line_answer = int(first_digit + last_digit)
        counter2 += line_answer
print(f"The answer for part 1 is: {counter2}")
