import os
from pojisteny import Pojisteny

class Evidence:
    def __init__(self):
        self.pojisteni = []
        # Načte data o pojistných ze souboru, pokud existuje
        if os.path.exists('seznam_pojistencu.txt'):
            with open('seznam_pojistencu.txt', 'r') as f:
                for line in f:
                    self.pojisteni.append(Pojisteny.from_string(line.strip()))
    
    def save(self):
        # Ukládá seznam pojistných do souboru
        with open('seznam_pojistencu.txt', 'w') as f:
            for pojisteny in self.pojisteni:
                f.write(str(pojisteny) + '\n')

    def vytvor_pojisteneho(self, jmeno, prijmeni, vek, telefon):
        # Vytváří nového pojistného a přidává ho do evidence
        self.pojisteni.append(Pojisteny(jmeno, prijmeni, vek, telefon))
        # Ukládá aktuální seznam pojistných
        self.save()

    def zobraz_pojistene(self):
        # Zobrazuje všechny pojistné v evidenci
        for pojisteny in self.pojisteni:
            print(pojisteny)

    def najdi_pojisteneho(self, jmeno, prijmeni):
        # Hledá pojistného podle jména a příjmení
        for pojisteny in self.pojisteni:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                return pojisteny
        return None

    def odstran_pojisteneho(self, jmeno, prijmeni):
        # Odstraňuje pojistného podle jména a příjmení
        pojisteny = self.najdi_pojisteneho(jmeno, prijmeni)
        if pojisteny:
            self.pojisteni.remove(pojisteny)
            # Ukládá aktuální seznam pojistných
            self.save()
            return True
        return False

    def uprav_pojisteneho(self, jmeno, prijmeni, new_jmeno, new_prijmeni, new_vek, new_telefon):
        # Upravuje údaje pojistného podle jména a příjmení
        pojisteny = self.najdi_pojisteneho(jmeno, prijmeni)
        if pojisteny:
            pojisteny.jmeno = new_jmeno
            pojisteny.prijmeni = new_prijmeni
            pojisteny.vek = new_vek
            pojisteny.telefon = new_telefon
            # Ukládá aktuální seznam pojistných
            self.save()
            return True
        return False
