from cabina import Cabina

class Cabina_animali(Cabina):
    def __init__(self, codCab, numLetti, ponte, prezzo, numAnimali):
        super().__init__(codCab, numLetti, ponte, prezzo)
        self._numAnimali = numAnimali

    def __str__(self):
        return f"{super().__str__()}, {self._numAnimali}"

    def aumenta_prezzo(self):
        self._prezzo = self._prezzo * (1 + (0.1 * self._numAnimali))