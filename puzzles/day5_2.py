from day5_1 import get_dest_seed_value, compute_maps
from tqdm import tqdm


if __name__ == "__main__":
    maps = compute_maps("../inputs/day5.txt")

    with open("../inputs/day5.txt") as f:
        a = f.readline()
        junk, *seeds = a.split(" ")

    seed_range_starts = []
    seed_range_lengths = []

    for (s1, s2) in zip(seeds[::2], seeds[1::2]):
        seed_range_starts.append(int(s1))
        seed_range_lengths.append(int(s2))

    answer = 1e12
    for seed_range_start, seed_range_length in zip(seed_range_starts, seed_range_lengths):
        for seed in tqdm(range(seed_range_start, seed_range_start + seed_range_length)):
            for m in maps:
                seed = get_dest_seed_value(seed, m)
            answer = min(answer, seed)

    print(f"The answer to day 5-2 is {answer}.")
