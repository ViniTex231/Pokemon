class Pokemon:
    def __init__(self, forca, vida, agilidade):
        self._forca = forca
        self._vida = vida
        self._agilidade = agilidade


class Agua(Pokemon):
    def __init__(self, forca, vida, agilidade, extraFogo):
        super().__init__(forca, vida, agilidade)
        self.extraFogo = extraFogo


class Planta(Pokemon):
    def __init__(self, forca, vida, agilidade, extraAgua):
        super().__init__(forca, vida, agilidade)
        self.extraAgua = extraAgua


class Fogo(Pokemon):
    def __init__(self, forca, vida, agilidade, extraPlanta):
        super().__init__(forca, vida, agilidade)
        self.extraPlanta = extraPlanta
