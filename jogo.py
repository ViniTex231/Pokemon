import time
from random import choice
from random import randint
from pokedex import Grass, Water, Fire

# PLANTAS
bulbasaur = Grass("Bulbasaur", 11, 45, 45, 40)

# AGUA
squirtle = Water("Squirtle", 10, 44, 46, 30)

# FOGO
charmander = Fire("Charmander", 9, 39, 65, 40)


def choosepokemon():
    print("-=" * 30)
    print("Welcome to Pokemon Battle ⚔️")
    print("You have to choose a Pokemon and the computer will choose a other Pokemon")
    print(" ")
    print("[1] - Bulbasaur")
    print("[2] - Squirtle")
    print("[3] - Charmander")
    while True:
        option = input("Choose your Pokemon: ")

        if option == "1":
            return bulbasaur
        elif option == "2":
            return squirtle
        elif option == "3":
            return charmander
        else:
            print("Incorrect option")


def randompc():
    print("You choosed your Pokemon, now I choose my player")
    pokemons = [bulbasaur, squirtle, charmander]
    x = choice(pokemons)
    return x


def battle():
    p = choosepokemon()
    x = randompc()
    pc_name = x.name
    pc_attack = x.attack
    pc_hp = x.hp
    pc_speed = x.speed
    if x.name == "Bulbasaur":
        pc_special = x.specialwater
    elif x.name == "Squirtle":
        pc_special = x.specialfire
    else:
        pc_special = x.specialgrass
    # print(x.name)
    time.sleep(1)
    print(f"My pokemon is {x.name}")
    time.sleep(1)

    pokemon_name = p.name
    pokemon_attack = p.attack
    pokemon_hp = p.hp
    pokemon_speed = p.speed
    if p.name == "Bulbasaur":
        pokemon_special = p.specialwater
    elif p.name == "Squirtle":
        pokemon_special = p.specialfire
    else:
        pokemon_special = p.specialgrass

    if pokemon_speed > pc_speed:
        print("Your pokemon have a overspeed, so you will start")
        time.sleep(1)
        print(" ")
        print(f"Your life is {pokemon_hp}")
        print(" ")
        print(f"My life is {pc_hp}")
        print(" ")

        while True:
            attack = input("Type 1 for attack: ")
            if attack == "1":
                print("Attacking...")
                print(" ")
                time.sleep(2)
                pc_hp = pc_hp - pokemon_attack
                print(f"My life is {pc_hp}")
                if pc_hp <= 0:
                    time.sleep(1)
                    print(f"My life is {pc_hp}, you win!")
                    break
                print("I will attack you!!")
                print("Attacking...")
                print(" ")
                time.sleep(2)
                pokemon_hp = pokemon_hp - pc_attack
                print(f"Your life is {pokemon_hp}")
                if pokemon_hp <= 0:
                    time.sleep(1)
                    print(f"Your life is {pokemon_hp}, I win!")
                    break

    elif pokemon_speed == pc_speed:
        print("Our pokemons have the same speed, so I will choose who is start")
        print(" ")
        time.sleep(1)
        choose = randint(0, 1)
        while True:
            if choose == 0:
                print("You start!")

                attack = input("Type 1 for attack: ")
                if attack == "1":
                    print("Attacking...")
                    print(" ")
                    time.sleep(1)
                    pc_hp = pc_hp - pokemon_attack
                    print(f"My life is {pc_hp}")
                    if pc_hp <= 0:
                        time.sleep(1)
                        print(f"My life is {pc_hp}, you win!")
                        break
                    print("I will attack you!!")
                    print("Attacking...")
                    print(" ")
                    time.sleep(1)
                    pokemon_hp = pokemon_hp - pc_attack
                    print(f"Your life is {pokemon_hp}")
                    if pokemon_hp <= 0:
                        time.sleep(1)
                        print(f"Your life is {pokemon_hp}, I win!")
                        break
                else:
                    print(" ")
            else:
                print("I will start!")
                time.sleep(1)
                print("Attacking...")
                print(" ")
                time.sleep(1)
                pokemon_hp = pokemon_hp - pc_attack
                print(f"Your life is {pokemon_hp}")
                if pokemon_hp <= 0:
                    time.sleep(1)
                    print(f"Your life is {pokemon_hp}, I win!")
                    break
                attack = input("Type 1 for attack: ")
                if attack == "1":
                    print("Attacking...")
                    print(" ")
                    time.sleep(1)
                    pc_hp = pc_hp - pokemon_attack
                    print(f"My life is {pc_hp}")
                    if pc_hp <= 0:
                        time.sleep(1)
                        print(f"My life is {pc_hp}, you win!")
                        break
                else:
                    print(" ")
    elif pokemon_speed < pc_speed:
        print("My pokemon have a overspeed, so I will start")
        print(" ")
        time.sleep(1)
        print(f"Your life is {pokemon_hp}")
        print(" ")
        print(f"My life is {pc_hp}")
        print(" ")
        while True:
            print("Attacking...")
            print(" ")
            time.sleep(1)
            pokemon_hp = pokemon_hp - pc_attack
            print(f"Your life is {pokemon_hp}")
            if pokemon_hp <= 0:
                time.sleep(1)
                print(f"Your life is {pokemon_hp}, I win!")
                break
            attack = input("Type 1 for attack: ")
            if attack == "1":
                print("Attacking...")
                print(" ")
                time.sleep(1)
                pc_hp = pc_hp - pokemon_attack
                print(f"My life is {pc_hp}")
                if pc_hp <= 0:
                    time.sleep(1)
                    print(f"My life is {pc_hp}, you win!")
                    break
            else:
                print(" ")
