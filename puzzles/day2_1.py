counter = 0
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
with open("../inputs/day2.txt") as f:
    for line in f:
        game_id, game_string = line.split(": ")
        game_id = int(game_id.split(" ")[1])
        games = game_string.split("; ")
        for game in games:
            game = game.strip()
            colors = game.split(", ")
            for c in colors:
                (count, color) = c.split(" ")
                match color:
                    case "red":
                        if int(count) > MAX_RED:
                            game_id = 0
                    case "green":
                        if int(count) > MAX_GREEN:
                            game_id = 0
                    case "blue":
                        if int(count) > MAX_BLUE:
                            game_id = 0
        counter += game_id

print(f"The answer to Day 2-1 is {counter}")
