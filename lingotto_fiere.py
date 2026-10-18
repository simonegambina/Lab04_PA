import csv

from stand import Stand, StandPreseExtra, StandPremium
from espostiore import Espositore

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.stands = {}
        self.espositori = {}

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""

        with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.reader(file)

            nuovi_stands = {}
            nuovi_espositori = {}

            for dati in reader:
                if not dati:
                    continue

                codice = dati[0].rstrip()

                if codice.startswith("ST"):
                    superficie = int(dati[1])
                    padiglione = int(dati[2])
                    prezzo_base = float(dati[3])

                    if len(dati) == 4:
                        stand = Stand(
                            codice, superficie, padiglione, prezzo_base)

                    elif dati[4].isdigit():
                        stand = StandPreseExtra(
                            codice, superficie, padiglione, prezzo_base, int(dati[4]))

                    else:
                        stand = StandPremium(
                            codice, superficie, padiglione, prezzo_base, dati[4].strip())

                    nuovi_stands[codice] = stand

                elif codice.startswith("ES"):
                    nome = dati[1].strip()
                    cognome = dati[2].strip()

                    espositore = Espositore(codice, nome, cognome)

                    nuovi_espositori[codice] = espositore

        self.stands = nuovi_stands
        self.espositori = nuovi_espositori

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""

        # Controllo esistenza stand
        if codice_stand not in self.stands:
            raise ValueError("Stand inesistente")

        # Controllo esistenza espositore
        if codice_espositore not in self.espositori:
            raise ValueError("Espositore inesistente")

        stand = self.stands[codice_stand]
        espositore = self.espositori[codice_espositore]

        # Controllo disponibilità stand
        if not stand.disponibile:
            raise ValueError("Stand già occupato")

        # Controllo assegnazione espositore
        if espositore.stand is not None:
            raise ValueError("Espositore già associato a uno stand")

        # Assegnazione
        stand.espositore = espositore
        stand.disponibile = False
        espositore.stand = stand

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """

        for espositore in self.espositori.values():

            if espositore.stand is not None:
                print(f"{espositore} - Stand assegnato: {espositore.stand.codice}")

            else:
                print(f"{espositore} - Nessuno stand assegnato")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""

        lista_stand = list(self.stands.values())

        return sorted(lista_stand)
