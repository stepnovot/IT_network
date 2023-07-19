class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        # Inicializace pojistného s danými hodnotami
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        # Převede informace o pojistném na řetězec pro výstup
        return f"{self.jmeno},{self.prijmeni},{self.vek},{self.telefon}"
    
    @classmethod
    def from_string(cls, pojisteny_str):
        # Tato funkce umožňuje vytvořit instanci pojistného ze vstupního řetězce
        jmeno, prijmeni, vek, telefon = pojisteny_str.split(',')
        return cls(jmeno, prijmeni, int(vek), telefon)
