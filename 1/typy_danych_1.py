import sys

wiek = 47
rok = 2024
temp = 36.6  # float

print(temp)  # 36.6
print(type(temp))  # <class 'float'>

print(wiek + rok)  # 2071
print(wiek - rok)  # -1977
print(wiek * rok)  # 95128
print(wiek / rok)  # 0.023221343873517788 -> float

print(rok // wiek)  # częśc całkowita z dzielenia 43  2024/ 47  = 43,.......
print(rok % wiek)  # reszta z dzielenia (modulo) -> 3
print(5 % 2)  # reszta

print(wiek ** rok)  # potegowanie
# len() długosc zbioru
print(len(str(wiek ** rok)))  # 3385
# print(len(str(wiek ** rok ** 2)))  # 3385
# ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

# w przypadku liczb float występuje problem zaokrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345
# 1.3 x 10 ^ 3 -> 1.3 x 2 ^ 4
# decimal - typ do liczenia pieniedzy
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(f"Sprawdzenie zmiennej {temp} {wiek}")  # Sprawdzenie zmiennej 36.6 47

print(f"""
{wiek}
    {temp}""")
# '47
#     36.6'
