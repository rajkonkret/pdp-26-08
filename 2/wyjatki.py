# wyjątki -
# błedy podczas wykonywania programu
# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdp-26-08\2\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
try:
    # print(5 / 0)
    # print("A" + 9)
    # print(int("A"))
    # raise KeyError("Brak klucza")  # rzucenie błedu
    wynik = 90 / 33
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Błąd typu")
except ValueError:
    print("Bład wartości")
except Exception as e:
    print("Bład", e)
else:  # gdy nie ma błędu
    print("Wynik", wynik)
finally:  # wykona się zawsze
    print("Wykonałem obliczenia")

print("Dalsza część programu")
# Nie dziel przez zero
# Dalsza część programu
# Błąd typu
# Dalsza część programu
# Bład wartości
# Dalsza część programu
# Bład 'Brak klucza'
# Dalsza część programu
# Wynik 2.727272727272727
# Dalsza część programu

# try-except [else-finally]
