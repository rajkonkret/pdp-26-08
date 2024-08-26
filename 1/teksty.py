tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# Witaj Świecie
# <class 'str'>

# teksty są niemutowalne
tekst.upper()  # zmienna tekst nie zostanie zmieniona, nadal przechowuje oryginalną wartość
print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst)  # Witaj Świecie
# zapamiętanie wyniku metody w zmiennej
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE

# zamaiana na małe litery
tekst_lower = tekst.lower()
print(tekst_lower)  # witaj świecie
print(tekst.lower())  # witaj świecie
print(tekst)  # Witaj Świecie

# Witaj Świecie
# 0123456789...   indeksy numerowane od 0
print(tekst.index("j"))  # indeks numer 4 (pozycja 5)
print(tekst.count("i"))  # występuje 3 razy
print(tekst.count("j", 0, 4))  # 0123, z prawej zbiór otwarty, czyli występuje 0 razy

# hints settings - podpowiedzi parametrów
print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

tekst_zamiana = "Witaj dobry Świecie"
print(tekst_zamiana.replace('dobry', ""))  # "Witaj  Świecie"
print(tekst.removesuffix("Świecie").strip())  # "Witaj" - strip() - usunie białe znaki, spacje na początku i końcu

print(tekst[4])  # "j" - litera na indeksie 4 (pozycja 5)

# kodowanie znaków
encode_s = tekst.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie', b - typ bajtowy
# \xc5\x9a -. \x liczby w sytemie szesnastkowym
# \xc5 - 197 dziesiętnie
print(type(encode_s))  # <class 'bytes'>
print(encode_s.decode('utf-8'))  # Witaj Świecie
