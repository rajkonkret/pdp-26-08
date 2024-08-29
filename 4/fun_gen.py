# generator zwraca kolejny wyniki dziłania
# nie przechowuje poprzednich wynikó
# efektywnie zarządza pamięciu
# leneiwe generowanie - dane dostarczane są wtedy kiedy są potrzzebne

def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


# 0
# 1
# 4
# 9
# 16

def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # wykonuje operacje, zwraca wynik, zapamiętuje element


kwa = kwadrat2(5)
print(type(kwa))  # <class 'generator'>
print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))
print("Zrób cokolwiek")
lista = []
lista.append("67890987")
print(lista)
print(next(kwa))
# 9
# Zrób cokolwiek
# ['67890987']
# 16
# gdy skonczy sie generator rzuci wyjątek
# StopIteration
try:
    print(next(kwa))  # StopIteration
except StopIteration:
    print("Generator zakończył działanie")
# Generator zakończył działanie
