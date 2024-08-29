# przykłąd użycia Decimal
from decimal import Decimal

import decimal
from sys import base_prefix

kwota1 = Decimal('10.25')
kwota2 = Decimal('5.50')
precyzja = Decimal('0.00')

suma = kwota2 + kwota1
print("Suma wynosi:", suma)  # Suma wynosi: 15.75

roznica = kwota1 - kwota2
print("Róznica wynosi", roznica)  # Róznica wynosi 4.75
print("Różnica wynosi (zaokrąglone): ", roznica.quantize(precyzja))  # Różnica wynosi (zaokrąglone):  4.75

podatek = Decimal('0.23')
kwota_z_podatkiem = kwota1 * (1 + podatek)
print("Kwota z podatkiem", kwota_z_podatkiem)  # Kwota z podatkiem 12.6075
print("Kwota z podatkiem (zaokrąglone)", kwota_z_podatkiem.quantize(precyzja))  # Kwota z podatkiem (zaokrąglone) 12.61

a = Decimal('1.2345')
b = Decimal('2.3456')
precyzja2 = Decimal('0.001')
c = a + b
print("Wynik", c)
print("Wynik zaokrąglony", c.quantize(precyzja2))
print("Wynik zaokrąglony", c.quantize(precyzja))
# Wynik 3.5801
# Wynik zaokrąglony 3.580
# Wynik zaokrąglony 3.58

decimal.getcontext().prec = 2
a = Decimal('1.2345')
b = Decimal('2.3456')
c = a + b
print(c)  # 3.6
