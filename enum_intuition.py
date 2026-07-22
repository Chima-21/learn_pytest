from enum import Enum, Flag, auto


class Team(Flag):
    AQUAMARINE: str = auto()
    EMERALD: str = auto()
    RUBY: str = auto()
    TOPAZ: str = auto()


winners: Team = Team.AQUAMARINE | Team.TOPAZ
myteam: Team = Team.EMERALD

print(myteam in winners)
