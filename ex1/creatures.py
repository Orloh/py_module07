# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    creatures.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/10 21:36:29 by orhernan         #+#    #+#              #
#    Updated: 2026/04/10 22:25:43 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from ex0.creatures import Creature
from . import capabilities


class Sproutling(Creature, capabilities.HealCapability):
    def __init__(self) -> None:
        super().__init__("sproutling", ["grass"])
        self._attack = "vine whip".capitalize()

    def attack(self) -> str:
        return f"{self._name} uses {self._attack}!"

    def heal(self, target: bool | None) -> str:
        if target:
            return f"{self._name} heals itself and other for a small amount"
        return f"{self._name} heals itself for a small amount"


class Bloomelle(Creature, capabilities.HealCapability):
    def __init__(self) -> None:
        super().__init__("bloomelle", ["grass", "fairy"])
        self._attack = "petal dance".capitalize()

    def attack(self) -> str:
        return f"{self._name} uses {self._attack}!"

    def heal(self, target: bool | None) -> str:
        if target:
            return f"{self._name} heals itself and other for a large amount"
        return f"{self._name} heals itself for a large amount"


class Shiftling(Creature, capabilities.TransformCapability):
    def __init__(self) -> None:
        super().__init__("shiftling", ["normal"])
        self._attack = "normal".capitalize()
        self._is_transformed = False

    def attack(self) -> str:
        if self._attack == "Normal":
            return f"{self._name} attacks normally"
        return f"{self._name} performs a boosted strike!"

    def transform(self) -> str:
        if self._is_transformed:
            return f"{self._name} is already in a sharper form!"

        self._attack = "Boosted"
        self._is_transformed = True
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        if not self._is_transformed:
            return f"{self._name} is already in normal form!"

        self._attack = "Normal"
        self._is_transformed = False
        return f"{self._name} returns to normal."


class Morphagon(Creature, capabilities.TransformCapability):
    def __init__(self) -> None:
        super().__init__("morphagon", ["normal", "dragon"])
        self._attack = "normal".capitalize()
        self._is_transformed = False

    def attack(self) -> str:
        if self._attack == "Normal":
            return f"{self._name} attacks normally"
        return f"{self._name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        if self._is_transformed:
            return f"{self._name} already morphed to a dragonic form!"

        self._attack = "Dragonic"
        self._is_transformed = True
        return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        if not self._is_transformed:
            return f"{self._name} is already in normal form!"

        self._attack = "Normal"
        self._is_transformed = False
        return f"{self._name} stabilizes its form."
