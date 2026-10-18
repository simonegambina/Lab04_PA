from selectors import SelectSelector


class Stand:

    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.codice = codice
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo_base = prezzo_base

        self.disponibile = True
        self.espositore = None

    def calcola_prezzo(self):
        return self.prezzo_base

    def __lt__(self, other):
        return self.calcola_prezzo() < other.calcola_prezzo()

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Occupato"

        return (f"{self.codice}: Standard | "
                f"{self.superficie} mq - "
                f"Padiglione {self.padiglione} - "
                f"Prezzo {self.calcola_prezzo():.2f}€ - "
                f"{stato}")

# POLIMORFISMO: lo stesso metodo si comporta diversamente a seconda del tipo di oggetto.

class StandPreseExtra(Stand):

    def __init__(self, codice, superficie, padiglione, prezzo_base, numero_prese):

        super().__init__(codice, superficie, padiglione, prezzo_base) #riprende gli attributi della classe padre
        self.numero_prese = numero_prese

    def calcola_prezzo(self):
        return self.prezzo_base * (1 + 0.07 * self.numero_prese)

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Occupato"

        return (f"{self.codice}: Prese Extra | "
                f"{self.superficie} mq - "
                f"Padiglione {self.padiglione} - "
                f"Prezzo {self.calcola_prezzo():.2f}€ - "
                f"Prese aggiuntive: {self.numero_prese} - "
                f"{stato}")

class StandPremium(Stand):

    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):

        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.posizione = posizione

    def calcola_prezzo(self):
        return self.prezzo_base * 1.30

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Occupato"

        return (f"{self.codice}: Premium | "
                f"{self.superficie} mq - "
                f"Padiglione {self.padiglione} - "
                f"Prezzo {self.calcola_prezzo():.2f}€ - "
                f"Posizione: {self.posizione} - "
                f"{stato}")