from pydantic import BaseModel

from .cards import CardDict, DECK


class Player(BaseModel):
    name: str
    hand: list[CardDict]


class Context(BaseModel):
    current_deck: list[CardDict]
    players: list[Player] = []


def context_instance(
    players: list[Player] | None = None
) -> Context:
    return Context(
        current_deck=DECK.copy(),
        players=players or []
    )