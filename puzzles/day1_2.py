import numpy as np

counter = 0
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
            first_digit = line[numeric_ind[0]]
        if numeric_ind[-1] > last_digit_position:
            last_digit = line[numeric_ind[-1]]

        line_answer = int(first_digit + last_digit)
        counter += line_answer

print(f"The answer for part 2 is: {counter}")
