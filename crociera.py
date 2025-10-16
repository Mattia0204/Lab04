import csv
import operator

from passeggero import Passeggero
from cabina import Cabina
from cabina_animali import Cabina_animali
from cabina_deluxe import Cabina_deluxe

class Crociera:
    def __init__(self, nome):
        self._nome = nome
        self.lista_cabine = []
        self.lista_passeggeri = []
        self.cabine_occupate = {}

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


    def carica_file_dati(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:    # Apre il file in modalità lettura con codifica UTF-8
                reader = csv.reader(file)                           # crea il reader CSV
                for line in reader:                                 # Scorre ogni riga del file
                    if len(line) == 3:
                        codice, nome, cognome = line
                        passeggero = Passeggero(codice, nome, cognome)
                        self.lista_passeggeri.append(passeggero)
                    elif len(line) == 4:
                        codice, letti, ponte, prezzo = line
                        cabina = Cabina(codice, int(letti), int(ponte), int(prezzo))
                        self.lista_cabine.append(cabina)
                    elif len(line) == 5:
                        codice, letti, ponte, prezzo, tipo = line
                        numero = ''.join(filter(str.isdigit, tipo))
                        if numero == '':
                            cabina = Cabina_deluxe(codice, int(letti), int(ponte), int(prezzo), tipo)
                            cabina.aumenta_prezzo()
                            self.lista_cabine.append(cabina)
                        else:
                            numero = int(numero)
                            cabina = Cabina_animali(codice, int(letti), int(ponte), int(prezzo), int(numero))
                            cabina.aumenta_prezzo()
                            self.lista_cabine.append(cabina)
                    else:
                        print("Riga fuori formato")
            print(f'File "{file_path}" caricato correttamente \n')
        except FileNotFoundError:
            print(f"Errore: il file {file_path} non esiste.")
            return None                     # Se il file non esiste, restituisce None per indicare errore

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        #passeggeri = []
        #passeggeri = [passeggero.codPas for passeggero in self.lista_passeggeri]
        if codice_passeggero not in self.lista_passeggeri:
            return print("Passeggero non esistente")
        #cabine = []
        #cabine = [cabina.codCab for cabina in self.lista_cabine]
        if codice_cabina not in self.lista_cabine:
            return print("Cabina non esistente")
        if codice_cabina in self.cabine_occupate:
            return print("Cabina già prenotata")
        else:
            self.cabine_occupate.append(codice_cabina, codice_passeggero)
            return print(f"Il passeggero {codice_passeggero} è stato assegnato alla cabina {codice_cabina}")

    def cabine_ordinate_per_prezzo(self):
        cabine_ordinate = sorted(self.lista_cabine, key=operator.attrgetter('prezzo'))        # ordina per attributo marca
        return cabine_ordinate


    def elenca_passeggeri(self):
        for p in self.lista_passeggeri:
            if p.codPas not in self.cabine_occupate:
                print(p)
            else:
                codice_corrispondente = self.cabine_occupate[p.codPas]
                print(p, "ha come cabina assegnata: ", codice_corrispondente)




