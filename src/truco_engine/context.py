from .cards import CardDict, DECK


class Player:
    def __init__(
        self,
        name: str,
        hand: list[CardDict]
    ):
        self.name = name
        self.hand = hand


class Group:
    def __init__(self, players: list[Player]):
        self.players = players


class Context:
    def __init__(
        self,
        current_deck: list[CardDict],
        groups: list[Group] | None = None
    ):
        self.validate()
        self.current_deck = current_deck
        self.groups = groups

    def validate(self) -> bool:
        return all(
            [
                self.groups is None or len(self.groups) >= 2
            ]
        )


def context_instance(
    groups: list[Group] | None = None
) -> Context:
    return Context(
        current_deck=DECK.copy(),
        groups=groups
    )