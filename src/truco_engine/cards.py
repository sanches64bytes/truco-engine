import random

from typing import TypedDict, Literal


class CardDict(TypedDict):
    label: str
    suit: Literal['diamond', 'spades', 'hearts', 'clubs']
    suit_value: int
    value: int


SUITS = ('diamond', 'spades', 'hearts', 'clubs')

RANKS = ('4', '5', '6', '7', 'Q', 'J', 'K', 'A', '2', '3')

DECK: list[CardDict] = [
    {
        'label': rank,
        'suit': suit,
        'suit_value': suit_value,
        'value': value,
    }
    for value, rank in enumerate(RANKS, start=1)
    for suit_value, suit in enumerate(SUITS, start=1)
]


def random_card(
    specific_deck: list[CardDict] | None = None,
    exclude_cards: list[CardDict] | None = None
) -> CardDict | None:
    deck = specific_deck or DECK
    if not exclude_cards:
        return random.choice(deck)
    deck = [card for card in deck if card not in exclude_cards]
    return random.choice(deck) or None