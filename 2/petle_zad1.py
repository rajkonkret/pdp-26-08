# petle - dają nam możliwość wykonania wielokrotnie tegao samego kodu
# for - pętla iteracyjna
import random
from itertools import zip_longest

for i in range(5):  # 0..4
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):
    print("Test podłoga")
    # print(_)
# Test podłoga
# Test podłoga
# Test podłoga
# Test podłoga
# Test podłoga
# Test podłoga
# Test podłoga
# Test podłoga
# Test podłoga
# Test podłoga
# Test podłoga
# 8
# Test podłoga
# 9

for i in range(20):
    print(i * 2)

# przerobić lotto na pętle
# dodac liste wylosowanych kul
lista_kule = list(range(1, 50))
lista_wyn = []
for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    lista_wyn.append(wyn)
    print(wyn)

print(lista_wyn)  # [46, 12, 26, 22, 28, 24]

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# list comprehension
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

print(lista_wyn)  # [11, 29, 42, 34, 21, 47]
for c in lista_wyn:
    if c > 10:
        print("Większe od 10", c)
    else:
        print("Mniejsze od 10", c)
# Większe od 10 11
# Większe od 10 29
# Większe od 10 42
# Większe od 10 34
# Większe od 10 21
# Większe od 10 47

for i in range(0, 10, 2):  # start,stop,krok
    print(i)
# 0
# 2
# 4
# 6
# 8
for i in range(10, 0, -2):  # ujemny krok
    print(i)
# 10
# 8
# 6
# 4
# 2
for i in range(-10, 0):
    print(i)
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1

for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
        print(c)
    print("Przy każdym elemencie pętli", c)
# Przy każdym elemencie pętli 0
# 3
# Przy każdym elemencie pętli 3
# Przy każdym elemencie pętli 4
# Przy każdym elemencie pętli 6
# Przy każdym elemencie pętli 8

imiona = ["Radek", "Tomek", 'Zenek', "Ania"]
print(imiona)  # ['Radek', 'Tomek', 'Zenek', 'Ania']
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Ania

# wypisać elementy z tej listy z indeksem: 0 Radek
for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for i in range(len(imiona)):  # range(4) -> 0123
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate()
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Ania')  -> 3 Ania

for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

ludzie = ['Radek', 'Tomek', 'Zenek', 'Magda']
wiek = [44, 55, 32, 27]
# wypisac to tak: Radek 44
for i in ludzie:
    print(i, wiek[ludzie.index(i)])
# Radek 44
# Tomek 55
# Zenek 32
# Magda 27
# IndexError: list index out of range
# # dla list o różnych długościach nastąpi błąd
ludzie = ['Radek', 'Tomek', 'Zenek', 'Magda', "Aldona"]
wiek = [44, 55, 32, 27]
# for i in ludzie:
#     print(i, wiek[ludzie.index(i)])
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdp-26-08\2\petle_zad1.py", line 172, in <module>
#     print(i, wiek[ludzie.index(i)])
#              ~~~~^^^^^^^^^^^^^^^^^
# IndexError: list index out of range
# 0
# zip() - łaczy elementy kolekcji
for i in zip(ludzie, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Magda', 27)
for i, w in zip(ludzie, wiek):
    print(i, w)
# Radek 44
# Tomek 55
# Zenek 32
# Magda 27

# 0 Radek 44
for i in enumerate(zip(ludzie, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Tomek', 55))
# (2, ('Zenek', 32))
# (3, ('Magda', 27))
a, b = (1, ('Tomek', 55))
print(a, b)  # 1 ('Tomek', 55)
c, d = ('Tomek', 55)
print(c, d)
print(a, c, d)  # 1 Tomek 55
a, (c, d) = (3, ('Magda', 27))
print(a, c, d)
for i, (l, w) in enumerate(zip(ludzie, wiek)):
    print(i, l, w)

# 0 Radek 44
# 1 Tomek 55
# 2 Zenek 32
# 3 Magda 27

zip_list = zip_longest(ludzie, wiek, fillvalue=None)
print(zip_list)  # <itertools.zip_longest object at 0x00000195AA353E20>, iterator, zwraca elementy po kolei
zipeed = list(zip_list)  # rozpakowanie elemntów z iteratora do listy
# for i in zip_list:
for i in zipeed:
    print(i)
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Magda', 27)
# ('Aldona', None)# iterator po przejsciu przez dane kończy działanie
print("--------")
# for l, w in zip_list:
for l, w in zipeed:
    print(l, w)
# Radek 44
# Tomek 55
# Zenek 32
# Magda 27
# Aldona None
