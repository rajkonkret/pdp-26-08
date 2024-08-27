# słownik - para klucz-wartość
# {'user': "Radek",'wiek':78}
# słownik jest odpowiednikiem jsona w pythonie -> {"name":"John", "age":30, "car":null}
# klucze nie mogą sie powtórzyc

# pusty słownik
dictionary = dict()
print(type(dictionary))  # <class 'dict'>
print(dictionary)  # {}

dictionary_1 = {}
print(type(dictionary_1))  # <class 'dict'>

# dodawanie elementów do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 38
print(dictionary)  # {'imie': 'Radek', 'wiek': 38}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 38])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 38)])

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 38}

# wypisanie elementów
print(dictionary['imie'])  # Tomek
# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary.get("Imie"))  # None, nie ma klucza w słowniku
print(dictionary.get("Imie", "Domyślna"))  # Domyślna

dictionary.update({'data': '12-12-2024'})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 38, 'data': '12-12-2024'}

dict_string = {'name': "Radek", 'surname': "Kowalski"}
print(dict_string)  # {'name': 'Radek', 'surname': 'Kowalski'}

dict_small = {'x': 2}
dict_small.update([('y', 3), ('z', 5)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 5}
dict_small.update([("k", 8)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 5, 'k': 8}

# # input() # pobiera dane od użytkownika
# tekst = input("Podaj imie")
# print(tekst)
# print(type(tekst))  # <class 'str'> - input zawsze zwraca stringa

# napisac aplikacje kalkulator
# pobrac dwie liczby - input x 2
# wyświetlic wynik (+) - print
# a = input("Podaj pierwszą liczbę")
# b = input("Podaj drugą liczbę")
# # b = float(input("Podaj drugą liczbę"))
# print(int(a) + float(b))
# # 10.0

# napisac aplikacje słownik pol-ang
# słownik zawierający pary
# wypisac klucze
# pobrac słowko od uzytkownika
# wypisac tłumaczennie słowka
pol_ang = {'kot': 'cat', 'pies': 'dog'}
print('Znam takie słowko do przetłumaczenia')
odp = input("Podaj słowko jakie chcesz przetłumaczyć")
print(pol_ang[odp.lower().replace(" ", "")])
print(pol_ang.get(odp, "nie mo"))
