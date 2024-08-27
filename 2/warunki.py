# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# w zalezności od warunku(True lub False) wykona jeden blok programu lub drugi
# warunek musi zwracac bool
# if
odp = True
print(bool(odp))  # True
odp = False
if odp:
    # blok wykonywany gdy warunek True
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza częśc programu")

odp = "Radek"
if odp:
    print("Radek")

if odp == "Radek":
    print("Nadal Radek")
# True
# Dalsza częśc programu
# Radek
# Nadal Radek

if odp == "Tomek":
    print("To jest Tomek")
else:  # w przeciwnym wypadku
    print("To  nie jest Tomek")

odp = "Tomek"
if odp == "Tomek":
    print("Tomek")

# walrus operator, operator morsa
if odp := "Radek":  # podstawia do zmiennej wartos i sprawdza
    print(f"Twoje imie to {odp}")

a = "Radek"
if (n := len(a)) > 3:
    print(n)  # 5

# podatek = 0
# zarobki = int(input("Podaj zarobki"))
# if zarobki < 10000:
#     podatek = 0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.9

# print(f"Podatek wynosi {podatek * zarobki}")
# dodac podatek 0.2 dla przedziału od 10000 do 29999

suma_zam = 150
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabat wyosi {rabacik}")
# Rabat wyosi 25

rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wyosi {rabat}")  # Rabat wyosi 25

