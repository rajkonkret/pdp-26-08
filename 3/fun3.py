a = 10
b = 10


def dodaj():
    a = 7  # to są zmienne o zasięgu lokalnym
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)  # uzyje wartości globalnych


def doda3():
    global a  # użyj globalną wartość a
    a = 9  # nadpisuje globalne a
    b = 34
    print(a + b)


print(f"Wartość a globalna {a=}")  # Wartość a globalna a=10
dodaj()  # 15
print(f"Wartość a globalna {a=}")  # Wartość a globalna a=10
dodaj2()  # 20
print(f"Wartość a globalna {a=}")  # Wartość a globalna a=10
doda3()  # 43
print(f"Wartość a globalna {a=}")  # Wartość a globalna a=9
dodaj2()  # 19
