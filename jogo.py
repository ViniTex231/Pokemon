import time
from random import choice
from random import randint
from pokedex import Grass, Water, Fire


    #PLANTAS
bulbasaur = Grass("Bulbasaur", 11, 45, 45, 40)

    #AGUA
squirtle = Water("Squirtle", 10, 44, 46, 30)

    #FOGO
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
    pcName = x.name
    pcAttack = x.attack
    pcHp = x.hp
    pcSpeed = x.speed
    if x.name == "Bulbasaur":
        pcSpecial = x.specialwater
    elif x.name == "Squirtle":
        pcSpecial = x.specialfire
    else:
        pcSpecial = x.specialgrass
    # print(x.name)
    time.sleep(1)
    print(f"My pokemon is {x.name}")
    time.sleep(1)

    pokemonName = p.name
    pokemonAttack = p.attack
    pokemonHp = p.hp
    pokemonSpeed = p.speed
    if p.name == "Bulbasaur":
        pokemonSpecial = p.specialwater
    elif p.name == "Squirtle":
        pokemonSpecial = p.specialfire
    else:
        pokemonSpecial = p.specialgrass

    # print(f'{pokemonName}')

    if pokemonSpeed > pcSpeed:
        print("Your pokemon have a overspeed, so you will start")
        time.sleep(1)
        print(" ")
        print(f"Your life is {pokemonHp}")
        print(" ")
        print(f"My life is {pcHp}")
        print(" ")
        i = 0
        while i == 0:
            i = 0
            attack = input("Type 1 for attack: ")
            if attack == "1":
                print("Attacking...")
                time.sleep(1)
                pcHp = pcHp - pokemonAttack
                print(f"My life is {pcHp}")
                if pcHp <= 0:
                    time.sleep(1)
                    print("My life is 0, you win!")
                    break
                print("I will attack you!!")
                print("Attacking...")
                time.sleep(1)
                pokemonHp = pokemonHp - pcAttack
                print(f"Your life is {pokemonHp}")
                if pokemonHp <= 0:
                    time.sleep(1)
                    print("Your life is 0, I win!")
                    break
            else:
                print(" ")
                i = 1
    elif pokemonSpeed == pcSpeed:
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
                    time.sleep(1)
                    pcHp = pcHp - pokemonAttack
                    print(f"My life is {pcHp}")
                    if pcHp <= 0:
                        time.sleep(1)
                        print("My life is 0, you win!")
                        break
                    print("I will attack you!!")
                    print("Attacking...")
                    time.sleep(1)
                    pokemonHp = pokemonHp - pcAttack
                    print(f"Your life is {pokemonHp}")
                    if pokemonHp <= 0:
                        time.sleep(1)
                        print("Your life is 0, I win!")
                        break
                else:
                    print(" ")
            else:
                print("I will start!")
                time.sleep(1)
                print("Attacking...")
                time.sleep(1)
                pokemonHp = pokemonHp - pcAttack
                print(f"Your life is {pokemonHp}")
                if pokemonHp <= 0:
                    time.sleep(1)
                    print("Your life is 0, I win!")
                    break
                attack = input("Type 1 for attack: ")
                if attack == "1":
                    print("Attacking...")
                    time.sleep(1)
                    pcHp = pcHp - pokemonAttack
                    print(f"My life is {pcHp}")
                    if pcHp <= 0:
                        time.sleep(1)
                        print("My life is 0, you win!")
                        break
                else:
                    print(" ")
    elif pokemonSpeed < pcSpeed:
        print("My pokemon have a overspeed, so I will start")
        print(" ")
        time.sleep(1)
        print(f"Your life is {pokemonHp}")
        print(" ")
        print(f"My life is {pcHp}")
        print(" ")
        while True:
            print("Attacking...")
            time.sleep(1)
            pokemonHp = pokemonHp - pcAttack
            print(f"Your life is {pokemonHp}")
            if pokemonHp <= 0:
                time.sleep(1)
                print("Your life is 0, I win!")
                break
            attack = input("Type 1 for attack: ")
            if attack == "1":
                print("Attacking...")
                time.sleep(1)
                pcHp = pcHp - pokemonAttack
                print(f"My life is {pcHp}")
                if pcHp <= 0:
                    time.sleep(1)
                    print("My life is 0, you win!")
                    break
            else:
                print(" ")


battle()
