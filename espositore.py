class Espositore:
    def __init__(self  , codice, nome, cognome):
        self._codice = codice
        self._nome = nome
        self._cognome = cognome
        self._stand=None

    @property
    def codice(self):
        return self._codice

    @property
    def nome(self):
        return self._nome

    @property
    def cognome(self):
        return self._cognome

    @property
    def stand(self):
        return self._stand

    @stand.setter
    def stand(self, stand):
        self._stand = stand

    def __eq__(self, other): #permette di stabilire quando due istanze devono essere considerate uguali, ad esempio in base a un codice identificativo
        if self._codice == other.codice:
            return True
        else:
            return False

    def __str__(self):
        stringa= f"{self._codice} - {self._nome} - {self._cognome}"
        if self._stand is None:
            stringa=stringa+"Nessuno stand assegnato a questo espositore"
        else:
            stringa=stringa+f"Espositore assegnato allo stand: {self._stand.codice}"

        return stringa