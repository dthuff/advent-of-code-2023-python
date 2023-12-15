import numpy as np


def get_number_of_ways_to_win(time, distance, eps=1e-6):
    top = np.floor(((time + np.sqrt((time ** 2) - 4 * distance)) / 2) - eps)
    bottom = np.ceil(((time - np.sqrt((time ** 2) - 4 * distance)) / 2) + eps)
    return int(top - bottom + 1)


if __name__ == "__main__":
    with open("../inputs/day6.txt") as f:
        time_line, distance_line = f.readlines()

    times = [int(t) for t in time_line.strip().split(" ") if t.isnumeric()]
    record_distances = [int(t) for t in distance_line.strip().split(" ") if t.isnumeric()]

    spreads = []
    for race_time, record_distance in zip(times, record_distances):
        spreads.append(get_number_of_ways_to_win(race_time, record_distance))

    print(f"The answer to day 6-1 is {np.prod(spreads)}.")
