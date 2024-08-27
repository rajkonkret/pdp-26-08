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

# zasymulujemy system zbierania logów
# zmienne będą przechowywaac dane, które przyszły z zewnętrznego systemu
# email, console, inny
# dla console wypiszemy: "Stało się coś strasznego"
# dla email: "System email"
# jesli system bedzie "email" to typ błedu nalezy przetłumaczyc komunikatem i wpisac do listy błedów
# error, medium, inny
alert_system = 'email'
error = 'medium'
lista_b = []

if alert_system == 'console':
    print("Stało się coś strasznego")
elif alert_system == 'email':
    print("System email")
    if error == 'error':
        lista_b.append("Bład krytyczny")
    elif error == 'medium':
        lista_b.append('Ostrzeżenie')
    else:
        lista_b.append("inny")
else:
    print("Inny system")

print(lista_b)
# System email
# ['Ostrzeżenie']
a = 10
assert a > 5
# assert a > 15  # AssertionError
assert 'Ostrzeżenie' in lista_b
# assert 'Krytyczny' in lista_b  # AssertionError

# napisac test z.....
# zadac pytanie
# pobrac odpowiedź
# sprawdzic odpowiedź
# wypisac włsciwy komunikat
punkty = 0
odp = input("Podaj datę Chrztu Polski")
if odp == '966':
    print("Brawo")
    punkty += 1  # punkty = punkty + 1
else:
    print("Błąd")
print(punkty)
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
