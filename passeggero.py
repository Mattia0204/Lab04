class Passeggero:
    def __init__(self, codPas, nome, cognome):
        self._codPas = codPas
        self._nome = nome
        self._cognome = cognome

    @property
    def codPas(self):
        return self._codPas

    @codPas.setter
    def codPas(self, codPas):
        self._codPas = codPas

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cognome(self):
        return self._cognome

    @cognome.setter
    def cognome(self, cognome):
        self._cognome = cognome

    def __str__(self):
        return f'{self.codPas} {self.nome} {self.cognome}'
