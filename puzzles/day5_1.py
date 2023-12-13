class Map:
    def __init__(self, lines):
        self.src_range_starts = []
        self.dest_range_starts = []
        self.range_lengths = []

        for line in lines[1:-1]:
            dest_range_start, src_range_start, range_length = [int(x) for x in line.split(" ")]
            self.src_range_starts.append(src_range_start)
            self.dest_range_starts.append(dest_range_start)
            self.range_lengths.append(range_length)


def get_dest_seed_value(seed: int, map: Map) -> int:
    relevant_index = determine_relevant_range(seed, map)
    if relevant_index:
        dest_seed_value = map.dest_range_starts[relevant_index] + (seed - map.src_range_starts[relevant_index])
    else:
        dest_seed_value = seed
    return dest_seed_value


def determine_relevant_range(seed, map):
    for idx, (src_range_start, range_length) in enumerate(zip(map.src_range_starts, map.range_lengths)):
        if src_range_start <= seed < src_range_start + range_length:
            return idx


def compute_maps(file_path):
    with open(file_path) as f:
        a = f.readlines()

    map_start_lines = [ind for ind, line in enumerate(a) if "map" in line]
    map_start_lines.append(len(a))
    maps = []
    for idx, map_start in enumerate(map_start_lines[:-1]):
        map_lines = a[map_start:map_start_lines[idx + 1]]
        maps.append(Map(map_lines))
    return maps


if __name__ == "__main__":
    maps = compute_maps("../inputs/day5.txt")

    with open("../inputs/day5.txt") as f:
        a = f.readline()
        junk, *seeds = a.split(" ")

    answer = 1e12
    for seed in seeds:
        seed = int(seed)
        dest_seed_value = seed
        for m in maps:
            dest_seed_value = get_dest_seed_value(dest_seed_value, m)
        answer = min(answer, dest_seed_value)
    print(f"The answer to day 5-1 is {answer}.")
