from collections import Counter
from random import randint

import numpy as np

CARD_ORDER = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
HAND_ORDER = ["FIVE_OF_A_KIND", "FOUR_OF_A_KIND", "FULL_HOUSE", "THREE_OF_A_KIND", "TWO_PAIR", "ONE_PAIR", "HIGH_CARD"]


class Hand:
    def __init__(self, cards, joker_indices=[False, False, False, False, False]):
        self.cards = cards
        self.joker_indices = joker_indices
        self.determine_hand_type()
        self.most_common_non_joker_card = self.determine_most_common_non_joker_card()

    def determine_most_common_non_joker_card(self):
        c = Counter(self.cards)
        if "J" in c.keys():
            c.pop("J")
        if not c:  # Edge case for hand of all "J"
            return "A"
        else:
            most_common_non_joker_card = max(c, key=c.get)
            for key, value in c.items():
                if value >= c[most_common_non_joker_card]:
                    if CARD_ORDER.index(key) < CARD_ORDER.index(most_common_non_joker_card):
                        most_common_non_joker_card = key
            return most_common_non_joker_card

    def determine_hand_type(self):
        c = Counter(self.cards)
        match max(c.values()):
            case 5:
                self.type = "FIVE_OF_A_KIND"
            case 4:
                self.type = "FOUR_OF_A_KIND"
            case 3:
                if len(c.values()) == 2:
                    self.type = "FULL_HOUSE"
                else:
                    self.type = "THREE_OF_A_KIND"
            case 2:
                if len(c.values()) == 3:
                    self.type = "TWO_PAIR"
                else:
                    self.type = "ONE_PAIR"
            case 1:
                self.type = "HIGH_CARD"
            case _:
                raise ValueError(f"Unable to determine hand type for hand {self.cards}")


def hand1_beats_hand2_tiebreaker(hand1: Hand, hand2: Hand) -> bool:
    for idx, (c1, c2) in enumerate(zip(hand1.cards, hand2.cards)):
        if hand1.joker_indices[idx] and hand2.joker_indices[idx]:
            continue
        elif hand1.joker_indices[idx] and not hand2.joker_indices[idx]:
            return False
        elif hand2.joker_indices[idx] and not hand1.joker_indices[idx]:
            return True
        else:
            if CARD_ORDER.index(c1) < CARD_ORDER.index(c2):
                return True
            elif CARD_ORDER.index(c1) > CARD_ORDER.index(c2):
                return False


def hand1_beats_hand2(hand1: Hand, hand2: Hand) -> bool:
    if HAND_ORDER.index(hand1.type) < HAND_ORDER.index(hand2.type):
        return True
    elif HAND_ORDER.index(hand1.type) > HAND_ORDER.index(hand2.type):
        return False
    else:
        return hand1_beats_hand2_tiebreaker(hand1, hand2)


def quicksort(array):
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    pivot_hand = array[randint(0, len(array) - 1)]
    for hand in array:
        if hand == pivot_hand:
            same.append(hand)
        elif hand1_beats_hand2(hand, pivot_hand):
            low.append(hand)
        else:
            high.append(hand)
    return quicksort(low) + same + quicksort(high)


def load_data(path: str, _track_jokers=False):
    hands = []
    bids = []
    with open(path) as f:
        for line in f:
            hand, bid = line.strip().split(" ")
            if _track_jokers:
                hands.append(Hand([a for a in hand], [a == "J" for a in hand]))
            else:
                hands.append(Hand([a for a in hand]))
            bids.append(int(bid))
    return hands, bids


if __name__ == "__main__":
    hands, bids = load_data("../inputs/day7.txt")
    sorted_hands = quicksort(hands)
    ranks = [len(hands) - sorted_hands.index(h) for h in hands]
    print(f"The answer to day 7-1 is {np.dot(ranks, bids)}")
