from cabina import Cabina

class Cabina_deluxe(Cabina):
    def __init__(self, codCab, numLetti, ponte, prezzo, tipo):
        super().__init__(codCab, numLetti, ponte, prezzo)
        self._tipo = tipo

    def __str__(self):
        return f"{super().__str__()}, {self._tipo}"

    def aumenta_prezzo(self):
        self._prezzo = self._prezzo * (1.2)