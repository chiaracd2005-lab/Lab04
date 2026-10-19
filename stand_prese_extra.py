from stand import Stand

class StandPreseExtra(Stand): #classe figlia della classe padre Stand
    def __init__(self, codice, superficie, padiglione, prezzo_base, numero_prese):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self._numero_prese = int(numero_prese)

    @property
    def numero_prese(self):
        return self._numero_prese

    def calcola_prezzo(self):
        return self._prezzo_base * (1 + 0.07 * self._numero_prese)

    def __str__(self):
        return f"{ super().__str__()} - Prese aggiuntive: {self._numero_prese}"