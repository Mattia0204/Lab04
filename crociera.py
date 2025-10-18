import csv
import operator


from passeggero import Passeggero
from cabina import Cabina
from cabina_animali import Cabina_animali
from cabina_deluxe import Cabina_deluxe

class Crociera:                             # Definisce la classe Crociera
    def __init__(self, nome):               # Costruttore della classe Crociera
        self._nome = nome
        self.lista_cabine = []
        self.lista_passeggeri = []
        self.cabine_occupate = {}

    @property
    def nome(self):                         # Getter per l'attributo nome
        return self._nome                   # Restituisce il nome della crociera

    @nome.setter
    def nome(self, nome):                   # Setter per l'attributo nome
        self._nome = nome                   # Assegna il nuovo valore al nome della crociera

    def carica_file_dati(self, file_path):  # Metodo per caricare dati da un file CSV
        try:
            with open(file_path, "r", encoding="utf-8") as file:  # Apre il file in modalità lettura con codifica UTF-8
                reader = csv.reader(file)                         # Crea un oggetto reader CSV per leggere il file
                for line in reader:
                    if len(line) == 3:                            # Se la riga ha 3 elementi (passeggero)
                        codice, nome, cognome = line
                        passeggero = Passeggero(codice, nome, cognome)      # Crea un oggetto Passeggero
                        self.lista_passeggeri.append(passeggero)            # Aggiungi il passeggero alla lista
                    elif len(line) == 4:                          # Se la riga ha 4 elementi (cabina standard)
                        codice, letti, ponte, prezzo = line
                        cabina = Cabina(codice, int(letti), int(ponte), int(prezzo))        # Crea una cabina standard
                        self.lista_cabine.append(cabina)                                    # Aggiungi la cabina alla lista
                    elif len(line) == 5:                          # Se la riga ha 5 elementi (cabina deluxe o animali)
                        codice, letti, ponte, prezzo, tipo = line
                        numero = ''.join(filter(str.isdigit, tipo))     # Estrai eventuali numeri dal tipo della cabina
                        if numero == '':                                # Se non ci sono numeri (è una cabina deluxe)
                            cabina = Cabina_deluxe(codice, int(letti), int(ponte), int(prezzo), tipo)           # Crea una cabina deluxe
                            cabina.aumenta_prezzo()                     # Aumenta il prezzo della cabina deluxe
                            self.lista_cabine.append(cabina)            # Aggiungi la cabina deluxe alla lista
                        else:                                           # Se ci sono numeri (è una cabina per animali)
                            numero = int(numero)
                            cabina = Cabina_animali(codice, int(letti), int(ponte), int(prezzo), int(numero))   # Crea una cabina per animali
                            cabina.aumenta_prezzo()                     # Aumenta il prezzo della cabina per animali
                            self.lista_cabine.append(cabina)            # Aggiungi la cabina per animali alla lista
                    else:
                        print("Riga fuori formato")                     # Se la riga ha un numero di colonne non previsto, segnala un errore
            print(f'File "{file_path}" caricato correttamente \n')      # Messaggio di conferma file caricato
        except FileNotFoundError:                                       # Gestisce l'errore se il file non viene trovato
            raise                                                       # Rilancia l'eccezione per essere gestita altrove (nel main)

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):        # Assegna un passeggero a una cabina
        passeggeri = [passeggero.codPas for passeggero in self.lista_passeggeri]    # Crea una lista con i codici dei passeggeri
        prenotata = True                                                # Flag per verificare se la cabina è già prenotata
        if codice_passeggero not in passeggeri:                         # Controlla se il codice del passeggero non esiste
            raise ValueError("Passeggero non esistente")
        cabine = [cabina.codCab for cabina in self.lista_cabine]        # Crea una lista con i codici delle cabine
        if codice_cabina not in cabine:                                 # Controlla se il codice della cabina non esiste
            raise ValueError("Cabina non esistente")
        for passeggeri_occupanti, cabine_occupate in self.cabine_occupate.items():      # Scorre le cabine occupate
            if codice_cabina in cabine_occupate:                        # Controlla se la cabina è già occupata
                prenotata = False                                       # Imposta il flag come False
                raise ValueError("Cabina già prenotata")
            if codice_passeggero in passeggeri_occupanti:               # Controlla se il passeggero ha già una cabina
                prenotata = False                                       # Imposta il flag come False
                raise ValueError("Il passeggero ha già una cabina prenotata")
        self.cabine_occupate[codice_passeggero] = codice_cabina         # Assegna il passeggero alla cabina
        return print(f"Il passeggero {codice_passeggero} è stato assegnato alla cabina {codice_cabina}")    # Stampa conferma

    def cabine_ordinate_per_prezzo(self):                               # Ordina le cabine per prezzo
        cabine_ordinate = sorted(self.lista_cabine, key=operator.attrgetter('prezzo'))          # Ordina la lista di cabine per il campo 'prezzo'
        return cabine_ordinate                                          # Restituisce la lista di cabine ordinate

    def elenca_passeggeri(self):                                        # Elenca tutti i passeggeri e le cabine a loro assegnate
        for p in self.lista_passeggeri:                                 # Scorre la lista dei passeggeri
            cabina_corrispondente = ""                                  # Variabile per memorizzare la cabina assegnata
            for passeggieri_occupanti, cabine_occupate in self.cabine_occupate.items():     # Scorre le cabine occupate
                if passeggieri_occupanti == p.codPas:                   # Controlla se il codice del passeggero corrisponde
                    cabina_corrispondente = cabine_occupate             # Assegna la cabina al passeggero
            if cabina_corrispondente == "":                             # Se il passeggero non ha una cabina assegnata
                print(p, " non ha cabina assegnata")                    # Stampa un messaggio
            else:                                                       # Se il passeggero ha una cabina assegnata
                for c in self.lista_cabine:                             # Scorre la lista delle cabine
                    if cabina_corrispondente == c.codCab:               # Se il codice della cabina corrisponde
                        print(p, " ha come cabina assegnata: ", c)      # Stampa il passeggero e la sua cabina formato standard già nelle classi con il metodo __str__




