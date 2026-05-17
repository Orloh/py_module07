# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    strategies.py                                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 15:24:19 by orhernan         #+#    #+#              #
#    Updated: 2026/04/18 15:31:57 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    def __init__(
            self,
            creature: Creature,
            strategy: 'BattleStrategy'
    ) -> None:
        self.creature = creature
        self.strategy = strategy

        creature_name = getattr(creature, "_name", creature.__class__.__name__)
        strategy_name = strategy.__class__.__name__

        message = (
            f"Invalid Creature '{creature_name}' for this '{strategy_name}'"
        )

        super().__init__(message)


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(creature, self)
        print(creature.attack())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(creature, self)
        if not isinstance(creature, HealCapability):
            return
        print(creature.attack())
        print(creature.heal(False))


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(creature, self)
        if not isinstance(creature, TransformCapability):
            return
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
