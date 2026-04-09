# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    battle.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/08 00:42:08 by orhernan         #+#    #+#              #
#    Updated: 2026/04/09 21:20:09 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_types: list[str]) -> None:
        self._name: str = name.capitalize()
        self._types: list[str] = [
            _type.capitalize() for _type in creature_types
        ]

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        types_str = "/".join(self._types)
        return f"{self._name} is a {types_str} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("flameling", ["fire"])
        self._attack = "ember".capitalize()

    def attack(self) -> str:
        return f"{self._name} uses {self._attack}!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("pyrodon", ["fire", "flying"])
        self._attack = "flamethrower".capitalize()

    def attack(self) -> str:
        return f"{self._name} uses {self._attack}!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("aquabub", ["water"])
        self._attack = "water gun".capitalize()

    def attack(self) -> str:
        return f"{self._name} uses {self._attack}!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("torragon", ["water"])
        self._attack = "hydro pump".capitalize()

    def attack(self) -> str:
        return f"{self._name} uses {self._attack}!"
