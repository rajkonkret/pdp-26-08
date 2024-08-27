import random

print(random)
# <module 'random' from 'C:\\Users\\CSComarch\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\random.py'>

# do działań na liczbach pseudolosowych

print(random.randint(1, 100))  # 100, int od 1 do 100
print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(5))  # int od 0 do 4
print(random.random())  # float, 0.23573589334267786 od 0 do 0.9999999
print(random.random() * 10)  # float 4.7235659662787945, od 0 do 9.999999

lista = [67, 45, 32, 68, 89, 90, 42]
print(random.choice(lista))  # liczba 32

lista_kule = list(range(1, 50))
# print(lista_kule)

# print(random.choice(lista))
# print(random.choice(lista))
# print(random.choice(lista))
# print(random.choice(lista))
# print(random.choice(lista))
# print(random.choice(lista))

# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)

print(random.choices(lista_kule, k=6))  # losuje z powtórzeniami [27, 34, 6, 13, 38, 13]
print(random.sample(lista_kule, k=6))  # [48, 12, 40, 5, 20, 30]
print(random.sample(lista_kule, 6))  # [13, 33, 47, 10, 45, 2]
