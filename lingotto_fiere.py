from csv import *
from espositore import Espositore
from stand import Stand
from stand_prese_extra import StandPreseExtra
from stand_premium import StandPremium

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self._stand={} #dizionari per stand ed espositori con i codici come chiavi
        self._espositori={}

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            with open(file_path,"r", encoding="utf-8") as file:
                csv_reader = reader(file)
                for riga in csv_reader:
                    campi=[campo.strip() for campo in riga if campo.strip()!=""] #per non considerare i campi vuoti inutili
                    codice=campi[0]

                    if codice.startswith("ES"): #capire se è un espositore o uno stand
                        nome=campi[1]
                        cognome = campi[2]
                        self._espositori[codice] = Espositore(codice, nome, cognome) #aggiungo questo espositore al dizionario degli espositori

                    elif codice.startswith("ST"):
                        superficie = float(campi[1])
                        padiglione = int(campi[2])
                        prezzo_base = float(campi[3])

                        if len(campi) == 4: #è uno stand standard
                            self._stand[codice] = Stand(codice, superficie, padiglione, prezzo_base)
                        elif len(campi) >= 5:
                            valore_extra = campi[4]
                            if valore_extra.isdigit(): #è uno stand con presa extra
                                self._stand[codice] = StandPreseExtra(codice, superficie, padiglione, prezzo_base, int(valore_extra))
                            else: #è uno stand premium
                                self._stand[codice] = StandPremium(codice, superficie, padiglione, prezzo_base, valore_extra)
        except FileNotFoundError:
            raise FileNotFoundError("File non trovato")

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        if codice_stand not in self._stand:
            raise KeyError(f"Lo stand con codice '{codice_stand}' non esiste.")
        if codice_espositore not in self._espositori:
            raise KeyError(f"L'espositore con codice '{codice_espositore}' non esiste.")

        stand = self._stand[codice_stand]
        espositore = self._espositori[codice_espositore]

        if stand.espositore is not None: #controllo se lo stand è già occupato
            raise Exception(f"Lo stand '{codice_stand}' è già occupato.")
        if espositore.stand is not None: #controllo se l'espositore ha già uno stand
            raise Exception(f"L'espositore '{codice_espositore}' è già associato a un altro stand ({espositore.stand.codice}).")

        stand.espositore = espositore
        espositore.stand = stand

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for espositore in self._espositori.values():
            if espositore.stand is not None:
                print(f"{espositore.codice}: {espositore.nome} {espositore.cognome} - Stand assegnato: {espositore.stand.codice}")
            else:
                print(f"{espositore.codice}: {espositore.nome} {espositore.cognome} - Nessun stand assegnato")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self._stand.values())#uso sorted sfruttando il metodo __lt__ implementato nella classe Stand
