#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    capacitor.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/10 22:21:22 by orhernan         #+#    #+#              #
#    Updated: 2026/04/10 22:25:44 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_factory(factory) -> None:
    print("Testing Creature with healing capability")

    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal(None))

    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal(None))


def test_transform_factory(factory) -> None:
    print("\nTesting Creature with transform capability")

    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main() -> None:
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing_factory(heal_factory)
    test_transform_factory(transform_factory)


if __name__ == "__main__":
    main()
