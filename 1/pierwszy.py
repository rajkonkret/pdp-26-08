import sys

print()  # wypisz/wydrukuj

print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się RadekRadek")
# Nazywam się Radek
# ctrl /  -komentarz automatyczny
# ctrl d - powielanie linii
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się RadekRadek
print('NAzywam się Radek')  # NAzywam się Radek
# print("Nazywam się radek')
#   File "C:\Users\CSComarch\PycharmProjects\pdp-26-08\1\pierwszy.py", line 25
#     print("Nazywam się radek')
#           ^
# SyntaxError: unterminated string literal (detected at line 25)
print("Nazywam się 'Radek'")  # Nazywam się 'Radek'
# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'> dane typu tekstowego
print("39")
print(type("39"))  # <class 'str'>
print("39" + "39")  # konkatenacja, łaczenie str 3939

print(39)
print(type(39))  # <class 'int'>, liczba całkowita
print(39 + 39)  # 78
print(sys.int_info)
# sys.int_info(
#     bits_per_digit=30,
#     sizeof_digit=4,
#     default_max_str_digits=4300,  # ilość znaków (cyfr)
#     str_digits_check_threshold=640)
# print("39" + 39)
# Process finished with exit code 1 oznacza, że mamy błąd
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdp-26-08\1\pierwszy.py", line 48, in <module>
#     print("39" + 39)
#           ~~~~~^~~~
# TypeError: can only concatenate str (not "int") to str
# silne typowanie - nie zmienia sam typów podczas operacji

print(int("39") + 39)  # int() - rzutowanie (zamiana) na liczbe int (całkowitą), 78
print("39" + str(39))  # str() = rzutowanie na str, 3939 (łączenie)

# odmienne operacje
print(8 + 8 + 8)  # 24 - matematyczne dodawanie
print('8' + '8' + '8')  # 888 - konkatenacja, łaczenie stringów

print(5 * "4")  # 44444

# zmienna - pudełko na dane
# przechowuje jedną wartość
# w dowolnym momencie moge do udełka wrzucić dowolną daną
# typowanie dynamiczne

# snake_case - konwencja nazewnicza dla zmienych
# nazwa zmiennej powiina wskazywacna to co przechowuje
liczba = 39
print(liczba)  # wypisanie wartości zmiennej, 39
print(type(liczba))  # <class 'int'>

print("5" * liczba)  # 55555555555555555555555555555555555555

liczba = "39"
print(type(liczba))  # <class 'str'>

name = "Radek"
print(type(name))
print(name + "Kowalski")  # RadekKowalski

name = 90
# print(name + "Kowalski")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# ctrl alt l - formatowanie kodu wg PEP8

# podpowiedz typów (nie jest to ustawianie typu!!!)
name: str = "Radek"
print(name)  # Radek
name = 90
print(name)  # 90

age = 56
print(age)
print(type(age))
