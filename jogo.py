import time
import inquirer
from random import choice
from random import randint
from pokedex import Grass, Water, Fire
from colors import cores, bg, fx
limpar = '\33[m'


# PLANTAS
bulbasaur = Grass("Bulbasaur", 11, 45, 45, 40)
ivysaur = Grass("Ivysaur", 8, 47, 48, 40)

# AGUA
squirtle = Water("Squirtle", 10, 44, 46, 30)
wartortle = Water("Wartortle", 11, 42, 45, 30)

# FOGO
charmander = Fire("Charmander", 9, 39, 65, 40)
charizard = Fire("Charizard", 11, 42, 65, 40)


def choosepokemon():
    print("-=" * 30)
    print(f"    {cores['preto']}{bg['vermelho']}Welcome to Pokemon Battle ⚔️{limpar}")
    questions = [
        inquirer.List('size',
                      message=f"{cores['branco']}{fx['sublinhado']}You have to choose a Pokemon and the computer will choose a other Pokemon{limpar}",
                      choices=[bulbasaur.name, ivysaur.name, charmander.name, charizard.name, squirtle.name, wartortle.name],
                      ),
    ]
    answers = inquirer.prompt(questions)
    option = answers['size']
    while True:
        if option == bulbasaur.name:
            return bulbasaur
        elif option == ivysaur.name:
            return ivysaur
        elif option == squirtle.name:
            return squirtle
        elif option == wartortle.name:
            return wartortle
        elif option == charmander.name:
            return charmander
        elif option == charizard.name:
            return charizard


def randompc():
    print(f"{fx['sublinhado']}You choosed your Pokemon, now I choose my player...{limpar}")
    time.sleep(1)
    print(" ")
    pokemons = [bulbasaur, squirtle, charmander, charizard, wartortle, ivysaur]
    x = choice(pokemons)
    return x


def battle():
    p = choosepokemon()
    x = randompc()
    pc_name = x.name
    pc_attack = x.attack
    pc_hp = x.hp
    pc_speed = x.speed

    time.sleep(1)
    print(f"{fx['sublinhado']}My pokemon is {bg['amarelo']}{cores['preto']}{x.name}{limpar}")
    print(" ")
    time.sleep(1)

    pokemon_name = p.name
    pokemon_attack = p.attack
    pokemon_hp = p.hp
    pokemon_speed = p.speed

    if pokemon_speed > pc_speed:
        print(f"{fx['sublinhado']}Your pokemon have a overspeed, so you will start{limpar}")
        time.sleep(1)
        print(" ")
        print("-=" * 30)
        print(" ")
        print(f"Your life is {bg['vermelho']}{cores['preto']}{pokemon_hp}{limpar}")
        print(" ")
        print(f"My life is {bg['vermelho']}{cores['preto']}{pc_hp}{limpar}")
        print(" ")
        print("-=" * 30)
        print(" ")

        while True:
            attack = input("Type 1 for attack: ")
            if attack == "1":
                print("Attacking...")
                print(" ")
                time.sleep(2)
                pc_hp = pc_hp - pokemon_attack
                print(f"My life is {bg['vermelho']}{cores['preto']}{pc_hp}{limpar}")
                if pc_hp <= 0:
                    time.sleep(1)
                    print(f"My life is {bg['vermelho']}{cores['preto']}{pc_hp}{limpar}, {bg['verde']}{cores['preto']}you win!{limpar}")
                    break
                print("I will attack you!!")
                print("Attacking...")
                print(" ")
                time.sleep(2)
                pokemon_hp = pokemon_hp - pc_attack
                print(f"Your life is {bg['vermelho']}{cores['preto']}{pokemon_hp}{limpar}")
                if pokemon_hp <= 0:
                    time.sleep(1)
                    print(f"Your life is {bg['vermelho']}{cores['preto']}{pokemon_hp}, I win!{limpar}")
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
                    print(f"My life is {bg['vermelho']}{cores['preto']}{pc_hp}{limpar}")
                    if pc_hp <= 0:
                        time.sleep(1)
                        print(f"My life is {bg['vermelho']}{cores['preto']}{pc_hp}{limpar}, {bg['verde']}{cores['preto']}you win!{limpar}")
                        break
                    print("I will attack you!!")
                    print("Attacking...")
                    print(" ")
                    time.sleep(1)
                    pokemon_hp = pokemon_hp - pc_attack
                    print(f"Your life is {bg['vermelho']}{cores['preto']}{pokemon_hp}{limpar}")
                    if pokemon_hp <= 0:
                        time.sleep(1)
                        print(f"Your life is {bg['vermelho']}{cores['preto']}{pokemon_hp}, I win!{limpar}")
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
                print(f"Your life is {bg['vermelho']}{cores['preto']}{pokemon_hp}{limpar}")
                if pokemon_hp <= 0:
                    time.sleep(1)
                    print(f"Your life is {bg['vermelho']}{cores['preto']}{pokemon_hp}, I win!{limpar}")
                    break
                attack = input("Type 1 for attack: ")
                if attack == "1":
                    print("Attacking...")
                    print(" ")
                    time.sleep(1)
                    pc_hp = pc_hp - pokemon_attack
                    print(f"My life is {bg['vermelho']}{cores['preto']}{pc_hp}{limpar}")
                    if pc_hp <= 0:
                        time.sleep(1)
                        print(f"My life is {bg['vermelho']}{cores['preto']}{pc_hp}{limpar}, {bg['verde']}{cores['preto']}you win!{limpar}")
                        break
                else:
                    print(" ")
    elif pokemon_speed < pc_speed:
        print("My pokemon have a overspeed, so I will start")
        print(" ")
        time.sleep(1)
        print(f"Your life is {bg['vermelho']}{cores['preto']}{pokemon_hp}{limpar}")
        print(" ")
        print(f"My life is {bg['vermelho']}{cores['preto']}{pc_hp}{limpar}")
        print(" ")
        while True:
            print("Attacking...")
            print(" ")
            time.sleep(1)
            pokemon_hp = pokemon_hp - pc_attack
            print(f"Your life is {bg['vermelho']}{cores['preto']}{pokemon_hp}{limpar}")
            if pokemon_hp <= 0:
                time.sleep(1)
                print(f"Your life is {bg['vermelho']}{cores['preto']}{pokemon_hp}, I win!{limpar}")
                break
            attack = input("Type 1 for attack: ")
            if attack == "1":
                print("Attacking...")
                print(" ")
                time.sleep(1)
                pc_hp = pc_hp - pokemon_attack
                print(f"My life is {bg['vermelho']}{cores['preto']}{pc_hp}{limpar}")
                if pc_hp <= 0:
                    time.sleep(1)
                    print(f"My life is {bg['vermelho']}{cores['preto']}{pc_hp}{limpar}, {bg['verde']}{cores['preto']}you win!{limpar}")
                    break
            else:
                print(" ")
