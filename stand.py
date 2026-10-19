class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self._codice = codice
        self._superficie = float(superficie)
        self._padiglione = int(padiglione)
        self._prezzo_base = float(prezzo_base)
        self._espositore=None

    @property
    def codice(self):
        return self._codice

    @property
    def superficie(self):
        return self._superficie

    @property
    def padiglione(self):
        return self._padiglione

    @property
    def prezzo_base(self):
        return self._prezzo_base

    @property
    def espositore(self):
        return self._espositore

    @espositore.setter
    def espositore(self, espositore):
        self._espositore = espositore

    @property
    def disponibile(self):
        return self._espositore is None

    def calcola_prezzo(self):
        return self._prezzo_base #perchè negli stand standard il prezzo finale coincide con il prezzo base

    def __lt__(self, other):  #permette di stabilire quando un oggetto è minore di un altro
        if self.calcola_prezzo() < other.calcola_prezzo():
            return True
        else:
            return False

    def __eq__(self, other):
        if self._codice == other.codice:
            return True
        else:
            return False

    def __str__(self):
        if self._espositore is None:
            stato="Disponibile"
        else:
            stato=f"Stand occupato da {self._espositore.codice}"
        return f"{self._codice} - {self._superficie}mq - Padiglione n. {self._padiglione} - Prezzo: {self.calcola_prezzo()} - Stato: {stato}"