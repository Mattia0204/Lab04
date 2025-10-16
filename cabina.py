class Cabina:
    def __init__(self, codCab, numLetti, ponte, prezzo):
        self._codCab = codCab
        self._numLetti = numLetti
        self._ponte = ponte
        self._prezzo = prezzo

    @property
    def codCab(self):
        return self._codCab

    @codCab.setter
    def codCab(self, codCab):
        self._codCab = codCab

    @property
    def numLetti(self):
        return self._numLetti

    @numLetti.setter
    def numLetti(self, numLetti):
        self._numLetti = numLetti

    @property
    def ponte(self):
        return self._ponte

    @ponte.setter
    def ponte(self, ponte):
        self._ponte = ponte

    @property
    def prezzo(self):
        return self._prezzo

    @prezzo.setter
    def prezzo(self, prezzo):
        self._prezzo = prezzo

    def __str__(self):
        return f"{self._codCab}: Standard | {self.numLetti} letti - Ponte {self.ponte} - Prezzo {self.prezzo}€ - Disponibile"



