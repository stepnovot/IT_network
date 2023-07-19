from evidence import Evidence

def validace_veku(vek):
    # Kontroluje, zda je věk platné číslo a zda je v rozumném rozmezí
    return vek.isdigit() and 1 <= int(vek) <= 120

def validace_telefonu(telefon):
    # Kontroluje, zda je telefonní číslo platné (v tomto případě jen zda obsahuje jen číslice)
    return telefon.isdigit()

def main():
    evidence = Evidence()
    while True:
        print("1: Vytvořit pojistného")
        print("2: Zobrazit pojistné")
        print("3: Najít pojistného")
        print("4: Upravit pojistného")
        print("5: Odstranit pojistného")
        print("6: Konec")
        volba = input("Zadejte vaši volbu: ")
        if volba == '1':
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            vek = input("Zadejte věk: ")
            while not validace_veku(vek):
                print("Neplatný věk. Zadejte prosím platný věk.")
                vek = input("Zadejte věk: ")
            vek = int(vek)
            telefon = input("Zadejte telefonní číslo: ")
            while not validace_telefonu(telefon):
                print("Neplatné telefonní číslo. Zadejte prosím platné telefonní číslo.")
                telefon = input("Zadejte telefonní číslo: ")
            evidence.vytvor_pojisteneho(jmeno, prijmeni, vek, telefon)
        elif volba == '2':
            evidence.zobraz_pojistene()
        elif volba == '3':
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            pojisteny = evidence.najdi_pojisteneho(jmeno, prijmeni)
            if pojisteny:
                print(pojisteny)
            else:
                print("Pojistný nenalezen")
        elif volba == '4':
            jmeno = input("Zadejte jméno pojistného, kterého chcete upravit: ")
            prijmeni = input("Zadejte příjmení pojistného, kterého chcete upravit: ")
            new_jmeno = input("Zadejte nové jméno: ")
            new_prijmeni = input("Zadejte nové příjmení: ")
            new_vek = input("Zadejte nový věk: ")
            while not validace_veku(new_vek):
                print("Neplatný věk. Zadejte prosím platný věk.")
                new_vek = input("Zadejte nový věk: ")
            new_vek = int(new_vek)
            new_telefon = input("Zadejte nové telefonní číslo: ")
            while not validace_telefonu(new_telefon):
                print("Neplatné telefonní číslo. Zadejte prosím platné telefonní číslo.")
                new_telefon = input("Zadejte nové telefonní číslo: ")
            if evidence.uprav_pojisteneho(jmeno, prijmeni, new_jmeno, new_prijmeni, new_vek, new_telefon):
                print("Pojistný úspěšně upraven")
            else:
                print("Pojistný nebyl nalezen a tedy nebyl upraven")
        elif volba == '5':
            jmeno = input("Zadejte jméno pojistného, kterého chcete odstranit: ")
            prijmeni = input("Zadejte příjmení pojistného, kterého chcete odstranit: ")
            if evidence.odstran_pojisteneho(jmeno, prijmeni):
                print("Pojistný úspěšně odstraněn")
            else:
                print("Pojistný nebyl nalezen a tedy nebyl odstraněn")
        elif volba == '6':
            break
        else:
            print("Neplatná volba")

if __name__ == "__main__":
    main()
