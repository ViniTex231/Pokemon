class Pokemon:
    def __init__(self, attack, hp, speed):
        self._attack = attack
        self._hp = hp
        self._speed = speed

        # GETTERS

    @property
    def attack(self):
        return self._attack

    @property
    def hp(self):
        return self._hp

    @property
    def speed(self):
        return self._speed


class Water(Pokemon):
    def __init__(self, attack, hp, speed, specialFire):
        super().__init__(attack, hp, speed)
        self._specialFire = specialFire

    @property
    def specialfire(self):
        return self._specialFire


class Grass(Pokemon):
    def __init__(self, attack, hp, speed, specialWater):
        super().__init__(attack, hp, speed)
        self._specialWater = specialWater

    @property
    def specialwater(self):
        return self._specialWater


class Fire(Pokemon):
    def __init__(self, attack, hp, speed, specialGrass):
        super().__init__(attack, hp, speed)
        self._specialGrass = specialGrass

    @property
    def specialgrass(self):
        return self._specialGrass


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

print(bulbasaur.hp)



