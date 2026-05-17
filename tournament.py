#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    tournament.py                                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 18:50:45 by orhernan         #+#    #+#              #
#    Updated: 2026/04/19 01:53:40 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from ex0.factories import CreatureFactory, FlameFactory, AquaFactory
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability
from ex2.strategies import (
    BattleStrategy,
    NormalStrategy,
    DefensiveStrategy,
    AggressiveStrategy,
    InvalidStrategyError
)


def display_tournament_preview(
        label: str,
        opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    preview = []

    for factory, strategy in opponents:
        temp_creature = factory.create_base()
        if isinstance(temp_creature, HealCapability):
            creature_name = "Healing"
        elif isinstance(temp_creature, TransformCapability):
            creature_name = "Transform"
        else:
            creature_name = getattr(
                temp_creature,
                "_name",
                temp_creature.__class__.__name__
            )
        strategy_name = strategy.__class__.__name__.replace("Strategy", "")

        preview.append(f"({creature_name}+{strategy_name})")

    print(f"{label}")
    print(f"[{', '.join(preview)}]")


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()

    try:
        rest_of_opponents = opponents
        for fac_a, strat_a in opponents:
            rest_of_opponents = rest_of_opponents[1:]

            for fac_b, strat_b in rest_of_opponents:

                c1 = fac_a.create_base()
                c2 = fac_b.create_base()

                print("* Battle *")
                print(c1.describe())
                print("VS.")
                print(c2.describe())
                print("now fight!")

                strat_a.act(c1)
                strat_b.act(c2)
                print()

    except InvalidStrategyError as e:
        print(f"Battle error, aborting torunament: {e}")
        print()


def main() -> None:
    flame_fact = FlameFactory()
    aqua_fact = AquaFactory()
    heal_fact = HealingCreatureFactory()
    trans_fact = TransformCreatureFactory()

    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    aggressive = AggressiveStrategy()

    opp_basic = [(flame_fact, normal), (heal_fact, defensive)]
    display_tournament_preview("Tournament 0 (basic)", opp_basic)
    battle(opp_basic)

    opp_error = [(flame_fact, aggressive), (heal_fact, defensive)]
    display_tournament_preview("Tournament 1 (error)", opp_error)
    battle(opp_error)

    opp_multiple = [
        (aqua_fact, normal),
        (heal_fact, defensive),
        (trans_fact, aggressive)
    ]
    display_tournament_preview("Tournament 2 (multiple)", opp_multiple)
    battle(opp_multiple)


if __name__ == "__main__":
    main()
