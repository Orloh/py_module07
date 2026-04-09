# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    battle.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/09 21:52:18 by orhernan         #+#    #+#              #
#    Updated: 2026/04/09 22:04:00 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from ex0 import CreatureFactory, AquaFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing Factory")
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())
    pyrodon = factory.create_evolved()
    print(pyrodon.describe())
    print(pyrodon.attack())
    print()


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    base1 = factory1.create_base()
    base2 = factory2.create_base()
    print(base1.describe())
    print("  vs")
    print(base2.describe())
    print("fight!")
    print(base1.attack())
    print(base2.attack())


def main() -> None:
    flame_fact = FlameFactory()
    aqua_fact = AquaFactory()

    test_factory(flame_fact)
    test_factory(aqua_fact)
    test_battle(flame_fact, aqua_fact)


if __name__ == "__main__":
    main()
