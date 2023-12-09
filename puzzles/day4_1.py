def clean_list_of_numbers(s: str):
    s = s.strip().split(" ")
    s = [int(ss) for ss in s if ss.isnumeric()]
    return s


class Card:
    def __init__(self, line):
        card_number, numbers = line.split(":")
        winning_numbers, our_numbers = line.split("|")

        self.index = int(card_number.split(" ")[-1])
        self.winning_numbers = clean_list_of_numbers(winning_numbers)
        self.numbers = clean_list_of_numbers(our_numbers)

    def get_score(self):
        return sum([1 for o in self.numbers if o in self.winning_numbers])


if __name__ == "__main__":
    answer = 0
    with (open("../inputs/day4.txt") as f):
        for line in f:
            card = Card(line)
            if card.get_score() > 0:
                answer += 2 ** (card.get_score() - 1)

    print(f"The answer to day 4-1 is {answer}")
