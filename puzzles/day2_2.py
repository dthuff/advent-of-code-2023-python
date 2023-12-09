counter = 0

with open("../inputs/day2.txt") as f:
    for line in f:
        REQ_RED = 0
        REQ_GREEN = 0
        REQ_BLUE = 0

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
                        if int(count) > REQ_RED:
                            REQ_RED = int(count)
                    case "green":
                        if int(count) > REQ_GREEN:
                            REQ_GREEN = int(count)
                    case "blue":
                        if int(count) > REQ_BLUE:
                            REQ_BLUE = int(count)

        counter += REQ_RED * REQ_GREEN * REQ_BLUE

print(f"The answer to Day 2-2 is {counter}")
