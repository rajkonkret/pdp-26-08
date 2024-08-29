from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    # dekorator
    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):  # Kura dziedziczy po Ptaku
    """
    klasa Kura
    """

    def __init__(self, gatunek):
        # obowiązkowo musimy wywołać konstruktor z klasy wyższej -> super
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def wydaj_odglos(self):
        print("Ko ko ko ko ko")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")


class Orzel(Ptak):
    """
    Klasa Orzeł, dziedziczy po klasie Ptak
    """

    def wydaj_odglos(self):
        print("kier kier kir")

    def polowanie(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")


class Sowa(Ptak):
    """
    Klasa Sowa
    """


# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# # nie możemy utworzyc obiektu klasy Ptak bo zawiera metode abstrakcyjną
# or1 = Ptak("Orzel", 45)
# or1.latam()  # Tu Orzel Lecę z szybkością 45
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0

kur2 = Kura("Kura domowa")
kur2.latam()
print(kur2.gatunek)
# Tu Kura domowa Ja nie latam.
# Kura domowa
# kur1.wydaj_odglos()
# or1.wydaj_odglos()
kur2.wydaj_odglos()
# Kura domowa
# Ko ko ko ko ko
or2 = Orzel("Orzel bielik", 50)
or2.wydaj_odglos()
# kier kier kir

# polimorfizm - wykorzystanie wspolnych dziedziczonych cech przez obiekty róznych klas
lista = [kur2, or2]
for i in lista:
    i.wydaj_odglos()
# Ko ko ko ko ko
# kier kier kir

# te metody  nie są juz polimorficzne
kur2.dziobanie()
or2.polowanie()
# Tu Kura domowa Idę sobie podziobać
# Tu Orzel bielik Rozpoczynam polowanie

# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
# sowa = Sowa("Sowa", 10)
