import csv
import operator

from cabina import Cabina

class Crociera:
    def __init__(self, nome):
        self._nome = nome
        self.lista_cabine = []
        self.lista_passeggeri = []

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
                    lettera = ''.join(filter(str.isalpha, line[0])) # estrae la parte alfabetica del codice
                    if lettera == "CAB":
                        if len(line)==4:
                            cabina = cabina(codCab=line[0], numLetti=line[1],ponte=line[2], prezzo=line[3])
                            self.lista_cabine.append(cabina)
                        elif len(line)==5:
                            numero = ''.join(filter(str.isdigit, line[4]))
                            if numero == '':
                                cabina = cabina_deluxe(codCab=line[0], numLetti=line[1], ponte=line[2], prezzo=line[3], tipo=line[4])
                                self.lista_cabine.append(cabina)
                            else:
                                cabina = cabina_animali(codCab=line[0], numLetti=line[1], ponte=line[2], prezzo=line[3], numAnimali=line[4])
                                self.lista_cabine.append(cabina)
                        else:
                            print("Riga fuori formato")
                    elif lettera == "P":




                        pass




            print(f'File "{file_path}" caricato correttamente \n')
        except FileNotFoundError:
            print(f"Errore: il file {file_path} non esiste.")
            return None                     # Se il file non esiste, restituisce None per indicare errore

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        cabine_ordinate = sorted(self.lista_cabine, key=operator.attrgetter('prezzo'))        # ordina per attributo marca
        return cabine_ordinate


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

