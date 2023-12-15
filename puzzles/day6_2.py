from day6_1 import get_number_of_ways_to_win


if __name__ == "__main__":
    with open("../inputs/day6.txt") as f:
        time_line, distance_line = f.readlines()

    _, *times = time_line.strip().split(" ")
    _, *dists = distance_line.strip().split(" ")

    race_time = int(''.join(x for x in times if x))
    record_distance = int(''.join(x for x in dists if x))

    print(f"The answer to day 6-1 is {get_number_of_ways_to_win(race_time, record_distance)}.")
