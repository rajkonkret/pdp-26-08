# funkcje zwracające wynik
# kończy się komendą return
# gdy napotka na return wychodzi z funkcji

def dodaj(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(6, 9))  # 15
wynik = dodaj(45, 90)
print(wynik)  # 135

print(odejmij(100, 45, 7))
print(odejmij())  # 0

print(oblicz_vat(1000))
print(oblicz_vat(1000, 15))
print(oblicz_vat(vat=8, cena=1000, ))
# 1230.0
# 1150.0
# 1080.0

zm = oblicz_vat(1000)
print(zm)  # 1230.0

if zm == 1230:
    print("ok")

print(oblicz_vat(1000) + dodaj(7, 9))  # 1246.0
