from enum import Enum, auto


class ModulStatus(Enum):
    OFFEN = auto()
    IN_BEARBEITUNG = auto()
    BESTANDEN = auto()