import random

DECK = {
    0: ['4', [0, 1, 2, 3]],
    1: ['5', [0, 1, 2, 3]],
    2: ['6', [0, 1, 2, 3]],
    3: ['7', [0, 1, 2, 3]],
    4: ['Q', [0, 1, 2, 3]],
    6: ['J', [0, 1, 2, 3]],
    7: ['K', [0, 1, 2, 3]],
    8: ['A', [0, 1, 2, 3]],
    9: ['2', [0, 1, 2, 3]],
    10: ['3', [0, 1, 2, 3]]
}


type HandType = dict[int, list[tuple[int, int]]]
type CardType = tuple[int, int]


class Context:
    def __init__(self):
        self.__hands: HandType | None = None
        self.__shackle: CardType | None = None

    def get_hands(self) -> HandType | None:
        return self.__hands

    def get_shackle(self) -> CardType | None:
        return self.__shackle
    
    def set_hands(self, hands: HandType) -> None:
        assert self.__hands is None
        self.__hands = hands

    def set_shackle(self, shackle: CardType) -> None:
        assert self.__shackle is None
        self.__shackle = shackle


class Engine:
    def __init__(self, number_players: int):
        self.number_players = number_players
        self.context = Context()
    
    def random_choose_card(self) -> CardType:
        card = random.choice(DECK.keys())
        suit = random.choice(DECK[card][1])
        return card, suit
    
    def deal_cards(self) -> HandType:
        hands = {
            i: [
                self.random_choose_card()
                for _ in range(3)
            ]
            for i in range(self.number_playes)
        }
        self.context.set_hands(hands)
        return hands
    
    def choose_shackle(self) -> CardType:
        shackle = self.random_choose_card()
        self.context.set_shackle(shackle)
        return shackle
    
    
