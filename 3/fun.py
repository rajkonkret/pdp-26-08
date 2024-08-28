# funkcje - wydzielony fragment kodu, można go wywłać wielokrotnie w dowolnym momenecie
# funkcja musi być najpierw zadeklarowana
# w miejscu deklaracji funkcja się nie wykona
# zeby funkcj się wykonałą trzeba ją uruchomic

a = 6
b = 8


# te funkcje nie zwracją wyniku
# deklaracja funkcji
# PEP8 -wymaga by deklaracja funkcji była oddzielona dwoma linijkami pustymi od reszty programu
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):  # posiada dwa obowiązkowe argumenty
    print(a + b)


def odejmij(a, b, c=0):  # c=0 argument o wartości domyslnej
    print(a - b - c)


# uruchoienie funkcji
# nazwa_funkcji i nawiasy ()
dodaj()  # 14
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(54, 89)  # 143
odejmij(5, 8)  # -3
odejmij(5, 8, 10)  # -13

# po nazwie
odejmij(c=9, b=8, a=5)
dodaj2(b=9, a=4)

# mieszane
odejmij(1, c=8, b=5)
odejmij(1, 5, c=9)
# pozycyjne muszą byc pierwsze, po nich nazwane
# odejmij(a=1, 2, 3)  # SyntaxError: positional argument follows keyword argument
print(dodaj())  # None

# print(dodaj() + dodaj2(6, 9))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
