from .enums import GameVariants
from .engine import Engine


class EngineConfig:
    def __init__(
        self,
        number_players: int,
        variant: GameVariants
    ):
        self.number_players = number_players
        self.variant = variant

    def init(self) -> Engine:
        match self.variant:
            case GameVariants.PAULISTA:
                ...
        raise ValueError(f"Variante '{self.variant}' não é suportada pelo motor de jogo.")