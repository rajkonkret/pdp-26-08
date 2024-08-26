user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # <class 'float'> - liczby zmiennoprzecinkowe
print(type(wersja))  # <class 'float'>
liczba = 123456789123  # int
print(type(liczba))  # <class 'int'>

print("Witaj %s, masz teraz %d lat." % (user, wiek))  # Witaj Tomek, masz teraz 39 lat.
# ten typ formatowania sprawdza typy
# print("Witaj %s, masz teraz %d lat." % (wiek, user))  # TypeError: %d format: a real number is required, not str
# %s - str
# %d - digit - liczba
print("Witaj %(user)s, masz teraz %(wiek)d lat" % {'user': user, 'wiek': wiek})  # Witaj Tomek, masz teraz 39 lat
print("Witaj %(user)s, masz teraz %(age)d lat" % {'user': user, 'age': wiek})  # Witaj Tomek, masz teraz 39 lat

print("Witaj {}, masz teraz {}".format(user, wiek))  # Witaj Tomek, masz teraz 39
print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.
# f - fstring, sformatowany string

print("Uzywamy wersji Pythona %i" % 3)  # Uzywamy wersji Pythona 3
print("Uzywamy wersji Pythona %f" % 3)  # Uzywamy wersji Pythona 3.000000
print("Uzywamy wersji Pythona %f" % 3.9)  # Uzywamy wersji Pythona 3.900000
print("Uzywamy wersji Pythona %.2f" % 3.9)  # Uzywamy wersji Pythona 3.90
print("Uzywamy wersji Pythona %.1f" % 3.9)  # Uzywamy wersji Pythona 3.9
print("Uzywamy wersji Pythona %.0f" % 3.9)  # Uzywamy wersji Pythona 4
print("Uzywamy wersji Pythona %.f" % 3.9)  # Uzywamy wersji Pythona 4
# zaokrągla przy wyświetlaniu
print("Wynik = %.2f" % 3.8765)  # Wynik = 3.88
x = 3.14
print("Zero miejsc po przecinku %.f" % x)  # Zero miejsc po przecinku 3
print("X nadal się nie zmieniło", x)  # X nadal się nie zmieniło 3.14

# zaokrągla liczbę
y = round(x)
print("y=", y, "x=", x)  # y= 3 x= 3.14

x = 3.1415
print(round(x, 2))  # 3.14

print(f"Uzywamy wersji pythona {wersja}")
print(f"Uzywamy wersji pythona {wersja:.1f}")
print(f"Uzywamy wersji pythona {wersja:.2f}")
print(f"Uzywamy wersji pythona {wersja:.0f}")
# Uzywamy wersji pythona 3.900001
# Uzywamy wersji pythona 3.9
# Uzywamy wersji pythona 3.90
# Uzywamy wersji pythona 4

print(f"{user:>10}")  # "     Tomek"
print(f"{user:<20}")  # "Tomek            "
print(f"{user:^25}")  # "          Tomek          "

print(liczba)  # 123456789123
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 123,456,789,123
print(f"Nasza duża liczba {liczba:_}")  # Nasza duża liczba 123_456_789_123
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))  # Nasza duża liczba 123 456 789 123
print(f"Nasza duża liczba {liczba:,}".replace(",", "`"))  # Nasza duża liczba 123`456`789`123
print(f"Nasza duża liczba {liczba:,}".replace(",", "."))  # Nasza duża liczba 123.456.789.123

# liczba_2 = 15000000
liczba_2 = 15_000_000
print(type(liczba_2))  # <class 'int'>
print(liczba_2)  # 15000000
