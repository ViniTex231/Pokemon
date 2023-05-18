class Pokemon:
    def __init__(self, name, attack, hp, speed):
        self._name = name
        self._attack = attack
        self._hp = hp
        self._speed = speed

        # GETTERS

    @property
    def name(self):
        return self._name

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
    def __init__(self, name, attack, hp, speed, specialFire):
        super().__init__(name, attack, hp, speed)
        self._specialFire = specialFire

    @property
    def specialfire(self):
        return self._specialFire


class Grass(Pokemon):
    def __init__(self, name, attack, hp, speed, specialWater):
        super().__init__(name, attack, hp, speed)
        self._specialWater = specialWater

    @property
    def specialwater(self):
        return self._specialWater


class Fire(Pokemon):
    def __init__(self, name, attack, hp, speed, specialGrass):
        super().__init__(name, attack, hp, speed)
        self._specialGrass = specialGrass

    @property
    def specialgrass(self):
        return self._specialGrass
