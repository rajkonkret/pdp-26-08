dictionary = {'imie': 'Radek', 'nazwisko': "Kowalski"}
print(type(dictionary))  # <class 'dict'>

# wyswietli klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for k in dictionary.keys():
    print(k)
# imie
# nazwisko

# wyswietli wartości
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
#  sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>Kowalski
for k, v in dictionary.items():
    print(k, v, end="<=>")  # imie Radek<=>nazwisko Kowalski<=>

pol_ang = {'kot': 'cat', 'pies': 'dog'}
ang_pol = {}  # pusty słownik
for k, v in pol_ang.items():
    ang_pol[v] = k
print(ang_pol)  # {'cat': 'kot', 'dog': 'pies'}

print({value: key for key, value in pol_ang.items()})
# {'cat': 'kot', 'dog': 'pies'}
