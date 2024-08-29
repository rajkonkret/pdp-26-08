# napisac program kalkulator z wykorzystaniem pętli while True
# menu z dostępnymi opcjami
# pobrac wybraną opcje z menu
# pobrac liczby do obliczen
# wyswwietlic wynik dziłlania
# obsłużyc wyjątki
# dodać opcję wyjscia z programu

while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec""")

    odp = input("Podaj opcje z menu")
    if odp == 5:
        break
    try:
        a = float(input("Podaj pierwszą liczbę"))
        b = float(input("Podaj drugą liczbę"))

        if odp == "1":
            print(f"Wynik dodawania {a} + {b} = {a + b}")
        elif odp == "2":
            print(f"Wynik odejmowanie {a} - {b} = {a - b}")
        elif odp == "3":
            print(f"Wynik mnożenia {a} * {b} = {a * b}")
        elif odp == "4":
            print(f"Wynik dzielenia {a} / {b} = {a / b}")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except Exception as e:
        print("Bład", e)
    else:
        print("Obliczenia zostały wykonane poprawnie")
    finally:
        print("Działam dalej")


wyr = "5*7-9+10"
print(eval(wyr))
print(eval("10+15*8"))  # 130
