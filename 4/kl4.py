# hermetyzacja
class Car:
    """
    klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        # pole jest prywatne
        self.__predkosc = 0

    # enkapsulacja - dodanie metod do odczytu lub zapisu pól prywatnych
    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10


car = Car("Fiat", 2024)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# pole prywatne nie jest widoczne poza klasą
# print(car.__predkosc)  # 50
car.licznik()  # Prędkość wynosi 50 km/h
# car.__predkosc = 0
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()
# Prędkość wynosi 50 km/h
# Prędkość wynosi 0 km/h

# car.__predkosc = 50 # to jest pole o zasiegu publicznym, przypadkowo o tej samej nazwie
car.licznik()  # Prędkość wynosi 0 km/h
