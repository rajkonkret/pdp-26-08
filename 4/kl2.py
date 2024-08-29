class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    # stworzyc metody wypisz_wiek, wypisz_wzrost
    def wypisz_wiek(self):
        print(f"Mam teraz {self.wiek} lat")

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu.")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


# cz1 = Human()  # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Ania", 28, 168)
print(cz1.imie)
print(cz1.wiek)
print(cz1.wzrost)
print(cz1.plec)
# Ania
# 28
# 168
# k
cz1.powitanie()
# Nazywam się Ania
cz1.wypisz_wiek()
cz1.wypisz_wzrost()
# Nazywam się Ania
# Mam teraz 28 lat
# Mam 168 cm wzrostu.
cz1.ruszaj()  # Ruszyłam w drogę
cz2 = Human("Radek", 50, 190, "m")
cz2.ruszaj()
# Ruszyłam w drogę
# Ruszyłem w drogę
