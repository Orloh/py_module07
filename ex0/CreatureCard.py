# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    CreatureCard.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/05 23:25:31 by orhernan         #+#    #+#              #
#    Updated: 2026/04/05 23:33:50 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from typing import Any
from ex0.Card import Card

class CreatureCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            health: int
    ) -> None:
        super().__init__(name, cost, rarity)

        if attack < 0 or health < 0:
            raise ValueError("Attack and health must be positive integers.")

        self.type = "Creature"
        self.attack = attack
        self.health = health

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: str) -> dict[str, Any]:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resoved": True
        }

    def get_card_info(self) -> dict[str, Any]:
        info = super().get_card_info()
        info.update({
            "type": self.type,
            "attack": self.attack,
            "health": self.health
        })
        return info
