# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    factories.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/09 21:21:00 by orhernan         #+#    #+#              #
#    Updated: 2026/04/09 21:30:51 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from . import creatures
from abc import ABC, abstractmethod


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> creatures.Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> creatures.Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> creatures.Creature:
        return creatures.Flameling()

    def create_evolved(self) -> creatures.Creature:
        return creatures.Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> creatures.Creature:
        return creatures.Aquabub()

    def create_evolved(self) -> creatures.Creature:
        return creatures.Torragon()
