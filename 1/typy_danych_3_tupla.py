# krotka (tupla) - kolekcja niemutowalna
# pozwala efektywniej zarządzac pamięcią
# krotka jedoelementowa - stała - zmienna

tupla = ("Radek")
print(type(tupla))  # <class 'str'>

tupla_2 = "Radek",
print(type(tupla_2))  # <class 'tuple'>

# PEP8 zalecy by krotkę jedoelemntowa umiesczac w nawiasach
tupla_3 = ("Radek",)
print(type(tupla_3))  # <class 'tuple'>
print(tupla_3)  # ('Radek',)

tupla_liczby = 43, 55, 22.34, 11, 200
# tupla_liczby = (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

# tupla jest niemutowalna
# tupla_liczby[2] = 123  # TypeError: 'tuple' object does not support item assignment

# można usunąć całą tuple
# del tupla_liczby
# print(tupla_liczby)  # NameError: name 'tupla_liczby' is not defined

tupla_imiona = "Radek", "Tomek", "Zenek", "Olek", 'Robert', 'Michał'
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Olek', 'Robert', 'Michał')
print(type(tupla_imiona))  # <class 'tuple'>

print(tupla_imiona.index("Radek"))  # indeks 0
print(tupla_imiona.count("Olek"))  # występuje 1 raz w tupli
