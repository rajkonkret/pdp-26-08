# petle - dają nam możliwość wykonania wielokrotnie tegao samego kodu
# for - pętla iteracyjna
import random

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
