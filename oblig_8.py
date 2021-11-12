class Flervalg:
    def __init__(self, spmtekst, a, b, c, d, riktigsvar):
        self.spmtekst = spmtekst
        self.svaralt = {a: 1, b: 2, c: 3, d: 4}
        self.riktigsvar = int(riktigsvar)

    def sjekk_svar(self):
        svaret = int(input("Hvilket alternativ velger du? "))
        while svaret != self.riktigsvar:
            if svaret > 4:
                print(f"Svaralternativ {svaret} finnes ikke. Velg mellom svaralternativ 1, 2, 3 eller 4.")
                svaret = int(input("Hvilket alternativ velger du? "))
            else:
                print("Feil svar, prøv igjen!")
                svaret = int(input("Hvilket alternativ velger du? "))
        return print(f"Riktig! Svaret var {self.riktigsvar}")

    def __str__(self):
        streng = f"{self.spmtekst} \n"
        for key, value in self.svaralt.items():
            streng += f"{value}) {key}\n"
        return streng

