# kolekcje - wiele danych w jedym pudełku
# lista - przechowuje wiele danych, róznego typu na raz
# zachowuje kolejnosc przy dodawaniu elementów

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(type(pusta_lista))  # <class 'list'>
print(pusta_lista)  # []

# append()
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Marek")
lista.append("Magda")
lista.append("Ania")
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Marek', 'Magda', 'Ania']
# ['Radek', 'Tomek', 'Zenek', 'Marek', 'Magda', 'Ania']
#     0,        1,      2,      3,        4,       5
#     (-6),    (-5),   (-4),  (-3),   (-2),      (-1)
print(lista[0])  # Radek
print(lista[2])  # Zenek
print(lista[4])  # Magda
# print(lista[6])  # IndexError: list index out of range
print(len(lista))  # 6
print(lista[len(lista) - 1])  # Ania
print(lista[-1])  # ostatni element z listy
print(lista[-2])
print(lista[-3])
# Ania
# Magda
# Marek

# wyświetlanie frgmentu listy (slicowanie)
print(lista[0:3])  # start:stop -> ['Radek', 'Tomek', 'Zenek'], indeksy 012
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']
print(lista[2:])  # ['Zenek', 'Marek', 'Magda', 'Ania']
print(lista[2:5])  # ['Zenek', 'Marek', 'Magda']
print(lista[:])  # ['Radek', 'Tomek', 'Zenek', 'Marek', 'Magda', 'Ania']

print(lista[-2:0])  # [] -> [4:0]
print(lista[0:-2])  # ['Radek', 'Tomek', 'Zenek', 'Marek'] -> [0:4]
print(lista[2:3])  # ['Zenek']
print(lista[2:10])  # ['Zenek', 'Marek', 'Magda', 'Ania']
print(lista[10:29])  # []

lista_15 = list(range(15))  # 0 ..14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[0:15:2])  # [start:stop:krok] [0, 2, 4, 6, 8, 10, 12, 14]
print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14]
print(lista_15[-10])  # 5

# nadpisanie elementu na liscie, na wskazanym indeksie
lista[3] = 'Mikołaj'
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Mikołaj', 'Magda', 'Ania']

# insert() - wstawienie w mieje o podanym indeksie
lista.insert(1, "Karol")
print(lista)  # ['Radek', 'Karol', 'Tomek', 'Zenek', 'Mikołaj', 'Magda', 'Ania']

# sprawdzenie indeksu na którym element się znajduje
print(lista.index("Mikołaj"))  # indeks numer 4

# usunięcie po elemencie
lista.remove("Mikołaj")
print(lista)  # ['Radek', 'Karol', 'Tomek', 'Zenek', 'Magda', 'Ania']

# usunięcie po indeksie
# zwraca usunięty elemnty
print(lista.pop(5))  # Ania
print(lista)
print(lista.pop(-2))  # Zenek
print(lista.pop())  # usunie ostatni element z listy, Magda

a = 1
b = 3
a = b
print(a, b)  # 3 3
b = 7
print(a, b)  # 3 7

lista_2 = lista  # a = b, kopiuje referencje (adres w pamieci)
lista_copy = lista.copy()  # kopia elementów listy
lista.clear()  # b = 7, clear() - czyszczenie listy
print(lista_2, lista)  # [] [], zmienione obie listy
print(lista_copy)  # ['Radek', 'Karol', 'Tomek']
print(id(lista_2))  # 2895633060224
print(id(lista))  # 2895633060224
print(id(lista_copy))  # 2895636446976
print(type(lista))

liczby = [54, 999, 34, 22, 12.34, 687]
print(liczby)  # [54, 999, 34, 22, 12.34, 687]
print(type(liczby))  # <class 'list'>

liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 687, 999]

liczby = [54, 999, 34, 22, 12.34, 687, "A"]
print(ord("A"))  # kod znaku (ascii) 65
# liczby.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'

lista_osob = ['radek', "ola", "lena", "agata"]
lista_osob.sort()
print(lista_osob)  # ['agata', 'lena', 'ola', 'radek']

lista_osob.sort(reverse=True)
print(lista_osob)  # ['radek', 'ola', 'lena', 'agata']

lista_osob.reverse()  # odwracanie elemntow listy bez sortowania
print(lista_osob)  # ['agata', 'lena', 'ola', 'radek']

liczby[3] = 666
print(liczby[0:3])
print(liczby[-2])
print(liczby)  # [54, 999, 34, 666, 12.34, 687, 'A']

del liczby  # usunie listę z pamięci
# print(liczby)  # NameError: name 'liczby' is not defined

tekst = "Pyth on."
lista1 = list(tekst)  # rozpakowanie sekwencji
print(lista1)  # ['P', 'y', 't', 'h', ' ', 'o', 'n', '.']

lista2 = [tekst]
print(lista2)  # ['Pyth on.']

krotka = tuple(lista_copy)  # tuple() - rzytowanie na krotke (tuple)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # ('Radek', 'Karol', 'Tomek')
