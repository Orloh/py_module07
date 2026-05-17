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
from ex2.strategies import (
    BattleStrategy,
    NormalStrategy,
    DefensiveStrategy,
    AggressiveStrategy,
    InvalidStrategyError
)


def single_battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

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

    except InvalidStrategyError as e:
        print(
            "Battle error, aborting torunament: "
            f"{e}"
        )


def main() -> None:
    flame_fact = FlameFactory()
    aqua_fact = AquaFactory()
    heal_fact = HealingCreatureFactory()
    trans_fact = TransformCreatureFactory()

    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    aggressive = AggressiveStrategy()

    print("Tournament 0 (basic)")
    opp_basic =[(flame_fact, normal), (heal_fact, defensive)]


if __name__ == "__main__":
    main()
