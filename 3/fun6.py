# stworzyc funkcję obliczającą średnia
def liczby(name=None, *cyfry):  # * dowolna ilosc argumentów pozycyjnych
    print(cyfry)
    count = len(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Średnia dla ucznia {name} wynosi {avg}")
    finally:
        print("Następne obliczenie")


liczby()
liczby(1, 2, 3, 4, 5)
liczby(1, 2, 3, 4, 5, 5, 4, 3, 4, 5)
liczby("Tomek", 1, 2, 3, 4, 5, 5, 4, 3, 4, 5)
# ()
# (1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5, 5, 4, 3, 4, 5)
# ()
# Bład division by zero
# (1, 2, 3, 4, 5)
# Średnia wynosi 3.0
# (1, 2, 3, 4, 5, 5, 4, 3, 4, 5)
# Średnia wynosi 3.6
# ()
# Bład division by zero
# Następne obliczenie
# (1, 2, 3, 4, 5)
# Średnia wynosi 3.0
# Następne obliczenie
# (1, 2, 3, 4, 5, 5, 4, 3, 4, 5)
# Średnia wynosi 3.6
# Następne obliczenie
# (1, 2, 3, 4, 5, 5, 4, 3, 4, 5)
# Średnia dla ucznia Tomek wynosi 3.6
# Następne obliczenie
