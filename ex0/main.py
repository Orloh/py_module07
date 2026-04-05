# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    main.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/05 23:34:53 by orhernan         #+#    #+#              #
#    Updated: 2026/04/05 23:39:59 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:")
    print(dragon.get_card_info())
    print()

    mana = 6
    print(f"Playing Fire Dragon with {mana} mana available:")
    playable = dragon.is_playable(mana)
    print(f"Playable: {playable}")

    if playable:
        print(f"Play result: {dragon.play({})}")
    print()

    print("Fire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {dragon.attack_target('Goblin Warrior')}")
    print()

    mana_low = 3
    print(f"Testing insufficient mana ({mana_low} available):")
    print(f"Playable: {dragon.is_playable(mana_low)}")
    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
