# funkcja lambda skrócony zapis funkcji
# zwraca wynik, domyślnie return
# funkcja anonimowa, możliwośc deklaracji w miejscu wykonanani
from functools import reduce


def odejmij(a, b):
    return a - b


print(odejmij(5, 7))  # -2
odejmij2 = lambda a, b: a - b
print(odejmij2(6, 19))  # -13

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(10000))  # 12300.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

# mapowanie danych
lista_wyn = []
lista = [1, 2, 3, 10, 20, 30, 50, 70, 200, 250]
for i in lista:
    lista_wyn.append(i * 2)

print(lista_wyn)  # [2, 4, 6, 20, 40, 60, 100, 140, 400, 500]

print([i * 2 for i in lista])  # [2, 4, 6, 20, 40, 60, 100, 140, 400, 500]


def zmien(x):
    return x * 2


lista_wyn_2 = []
for i in lista:
    lista_wyn_2.append(zmien(i))

print(lista_wyn_2)  # [2, 4, 6, 20, 40, 60, 100, 140, 400, 500]

# funkcje wyzszego rzędu
# map() - pobiera elemnt, wykonuje działanie zadane funkcja
print(f"Zastosowanie map() {list(map(zmien, lista))}")
# Zastosowanie map() [2, 4, 6, 20, 40, 60, 100, 140, 400, 500]

# zastosowanie lambdy jako funkcji anonimowej
print(f"Zastosowanie map() {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map() [2, 4, 6, 20, 40, 60, 100, 140, 400, 500]
print(f"Zastosowanie map() {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x * 6, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x * 12, lista))}")
# Zastosowanie map() [2, 4, 6, 20, 40, 60, 100, 140, 400, 500]
# Zastosowanie map() [4, 8, 12, 40, 80, 120, 200, 280, 800, 1000]
# Zastosowanie map() [6, 12, 18, 60, 120, 180, 300, 420, 1200, 1500]
# Zastosowanie map() [12, 24, 36, 120, 240, 360, 600, 840, 2400, 3000]


# filtrowanie danych
print(lista)
l3 = []
for i in lista:
    if i < 20:
        l3.append(i)

print(l3)  # [1, 2, 3, 10]

# filter()
print(f"Zastosowanie filter: {list(filter(lambda x: x < 20, lista))}")
# Zastosowanie filter: [1, 2, 3, 10]
print(f"Zastosowanie filter: {list(filter(lambda x: x > 100, lista))}")
# Zastosowanie filter: [200, 250]
print(f"Zastosowanie filter: {list(filter(lambda x: x > 10 and x < 300, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: 10 < x < 300, lista))}")
# Zastosowanie filter: [20, 30, 50, 70, 200, 250]
# Zastosowanie filter: [20, 30, 50, 70, 200, 250]

# reduce()
# For
# example, reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
# calculates
# ((((1 + 2) + 3) + 4) + 5).
lista_reduce = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a + b, lista_reduce))  # 15
print(reduce(lambda a, b: a * b, lista_reduce))  # 120 silnia

print(sum(lista_reduce))  # 15
