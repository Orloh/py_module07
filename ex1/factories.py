# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    factories.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/13 16:57:26 by orhernan         #+#    #+#              #
#    Updated: 2026/04/13 17:05:55 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from ex0 import creatures
from ex0 import CreatureFactory


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> creatures.Creature:
        return creatures.Sproutling()

    def create_evolved(self) -> creatures.Creature:
        return creatures.Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> creatures.Creature:
        return creatures.Shiftling()

    def create_evolved(self) -> creatures.Creature:
        return creatures.Morphagon()
