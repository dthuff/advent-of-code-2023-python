import numpy as np

from day7_1 import quicksort, load_data, Hand


def improve_with_jokers(hand: Hand):
    if "J" not in hand.cards:
        pass
    else:
        hand.cards = [hand.most_common_non_joker_card if c == "J" else c for c in hand.cards]
        hand.determine_hand_type()
    return hand


if __name__ == "__main__":
    hands, bids = load_data("../inputs/day7.txt", _track_jokers=True)
    hands = [improve_with_jokers(hand) for hand in hands]
    sorted_hands = quicksort(hands)
    ranks = [len(hands) - sorted_hands.index(h) for h in hands]
    print(f"The answer to day 7-2 is {np.dot(ranks, bids)}")
