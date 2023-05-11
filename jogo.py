from pokedex import Grass, Water, Fire

    #PLANTAS
bulbasaur = Grass(30, 30, 30, 40)
ivysaur = Grass(40, 40, 40, 50)
venusaur = Grass(50, 50, 50, 60)

    #AGUA
squirtle = Water(30, 30, 30, 30)
wartortle = Water(40, 40, 40, 40)
blastoise = Water(50, 50, 50, 50)

    #FOGO
charmander = Fire(40, 30, 40, 40)
charmeleon = Fire(40, 40, 50, 50)
charizard = Fire(50, 50, 60, 70)

pokemonName = []
pokemonAttack = []
pokemonHp = []
pokemonSpeed = []
pokemonSpecial = []


def choosepokemon():
    print("-=" * 30)
    print("Welcome to Pokemon Battle ⚔️")
    print("You have to choose a Pokemon and the computer will choose a other Pokemon")
    print(" ")
    print("[1] - Bulbasaur",
          "[2] - Ivysaur",
          "[3] - Venusaur",
          "[4] - Squirtle",
          "[5] - Wartortle",
          "[6] - Blastoise",
          "[7] - Charmander",
          "[8] - Charmeleon",
          "[9] - Charizard")
    option = int(input("Choose your Pokemon: "))
    if option == 1:
        pokemonName.append("Bulbasaur")
        pokemonAttack.append(bulbasaur.attack)
        pokemonHp.append(bulbasaur.hp)
        pokemonSpeed.append(bulbasaur.speed)
        pokemonSpecial.append(bulbasaur.specialwater)
    elif option == 2:
        pokemonName.append("Ivysaur")
        pokemonAttack.append(ivysaur.attack)
        pokemonHp.append(ivysaur.hp)
        pokemonSpeed.append(ivysaur.speed)
        pokemonSpecial.append(ivysaur.specialwater)
    elif option == 3:
        pokemonName.append("Venusaur")
        pokemonAttack.append(venusaur.attack)
        pokemonHp.append(venusaur.hp)
        pokemonSpeed.append(venusaur.speed)
        pokemonSpecial.append(venusaur.specialwater)
    elif option == 4:
        pokemonName.append("Squirtle")
        pokemonAttack.append(squirtle.attack)
        pokemonHp.append(squirtle.hp)
        pokemonSpeed.append(squirtle.speed)
        pokemonSpecial.append(squirtle.specialfire)
    elif option == 5:
        pokemonName.append("Wartortle")
        pokemonAttack.append(wartortle.attack)
        pokemonHp.append(wartortle.hp)
        pokemonSpeed.append(wartortle.speed)
        pokemonSpecial.append(wartortle.specialfire)
    elif option == 6:
        pokemonName.append("Blastoise")
        pokemonAttack.append(blastoise.attack)
        pokemonHp.append(blastoise.hp)
        pokemonSpeed.append(blastoise.speed)
        pokemonSpecial.append(blastoise.specialfire)
    elif option == 7:
        pokemonName.append("Charmander")
        pokemonAttack.append(charmander.attack)
        pokemonHp.append(charmander.hp)
        pokemonSpeed.append(charmander.speed)
        pokemonSpecial.append(charmander.specialgrass)
    elif option == 8:
        pokemonName.append("Charmeleon")
        pokemonAttack.append(charmeleon.attack)
        pokemonHp.append(charmeleon.hp)
        pokemonSpeed.append(charmeleon.speed)
        pokemonSpecial.append(charmeleon.specialgrass)
    elif option == 9:
        pokemonName.append("Charizard")
        pokemonAttack.append(charizard.attack)
        pokemonHp.append(charizard.hp)
        pokemonSpeed.append(charizard.speed)
        pokemonSpecial.append(charizard.specialgrass)

    print(f"{pokemonName},{pokemonHp},{pokemonAttack},{pokemonSpeed},{pokemonSpecial}")


choosepokemon()
