# klasa - element programowania obiektowe
# klasa - przepis, szablon
# wskazuje minimum cech
# obiekt (instancja) jest zbudowany qg przepisu
# Definicja klasy nie uruchamia klasy
# budowanie obiektu uruchamia elemnty klasy
# paradygmaty programowania obiektowy
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja
# pola (stan obiektu -> zmienne)
# metody (funkcje)

# deklaracja klasy
# PEP8 zalec by nazwy kal były z dużej litery CamelCase
# komentarz wielolinijkowy w kalsie jest traktowany jak dokumentacja
class Human:
    """
    Klasa Human opisująca człowiek w pythonie
    """
    imie = ""
    wiek = None
    plec = "k"


cz1 = Human()
print(cz1)  # <__main__.Human object at 0x000001ECE103DBE0>
print(Human.__doc__)  # Klasa Human opisująca człowiek w pythonie
print(print.__doc__)
# pydoc -b uruchomienie serwera z dokumentacją projektu
# pydoc -w kl1 - generowanie html z dokumentacja dla danego pliku
print(cz1.plec)
print(cz1.imie)
print(cz1.wiek)
# k
#
# None

cz1.imie = "Ania"
cz1.wiek = 36
print(cz1.plec)
print(cz1.imie)
print(cz1.wiek)
# k
# Ania
# 36
cz2 = Human()
cz2.imie = "Radek"
cz2.wiek = 45
cz2.plec = "m"
print(cz2.plec)
print(cz2.imie)
print(cz2.wiek)
# m
# Radek
# 45
