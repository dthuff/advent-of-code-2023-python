from day4_1 import Card
import linecache


if __name__ == "__main__":
    cards = []
    card_count = 0
    # Get the starting set of cards - 1 copy of each.
    with open("../inputs/day4.txt") as f:
        for line in f:
            cards.append(Card(line))
            card_count += 1

    # Now, deal with the copies
    while len(cards):
        this_card = cards.pop()
        copies_won = this_card.get_score()
        for i in range(this_card.index + 1, this_card.index + copies_won + 1):
            line = linecache.getline('../inputs/day4.txt', i)
            cards.append(Card(line))
            card_count += 1

    print(f"The answer to day 4-2 is: {card_count}")
