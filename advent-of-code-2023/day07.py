from advent import groupby, itemgetter, parse
from typing import Callable, List, Tuple

Hand = List[int]
CategoryFun = Callable[[Hand], int]
Round = Tuple[int, int]


def parse_input(get_category: CategoryFun) -> List[Round]:
    def card_positions(jokers_wild: bool) -> str:
        return '_J23456789T_QKA' if jokers_wild else '__23456789TJQKA'

    def get_hand(cards: str, jokers_wild: bool = False) -> Hand:
        return [card_positions(jokers_wild).index(card) for card in cards]

    def parse_round(cards: str, bid: int) -> Round:
        jokers_wild = True if get_category == get_category_with_wild else False
        a, b, c, d, e = hand = get_hand(cards, jokers_wild)
        return (get_category(hand) * 14**5 + a * 14**4 + b * 14**3 + c * 14**2 + d * 14 + e, bid)

    return [parse_round(cards, int(bid)) for cards, bid in parse(7, str.split)]


def solve(get_category: CategoryFun) -> int:
    ranked_input = sorted(parse_input(get_category), key=itemgetter(0))
    return sum(rank * bid for rank, bid in enumerate([bid for _, bid in ranked_input], 1))


def get_category(card_hand: Hand):
    match sorted([len(list(group)) for _, group in groupby(sorted(card_hand))], reverse=True):
        case [5]:
            return 7  # Five of a kind
        case [4, 1]:
            return 6  # Four of a kind
        case [3, 2]:
            return 5  # Full house
        case [3, 1, 1]:
            return 4  # Three of a kind
        case [2, 2, 1]:
            return 3  # Two pair
        case [2, 1, 1, 1]:
            return 2  # One pair
        case [1, 1, 1, 1, 1]:
            return 1  # High card
        case _:
            raise RuntimeError('Invalid hand')


def get_category_with_wild(hand: Hand):
    def replace_joker(replacement: int):
        joker = 1
        return [replacement if card == joker else card for card in hand]

    return sorted(
        [
            get_category(replace_joker(replacement))
            for replacement in [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
        ]
    )[-1]


assert solve(get_category) == 246409899
assert solve(get_category_with_wild) == 244848487
