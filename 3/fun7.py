def connect(**opcje):  # ** dane słownikowe, dowolna ilosc argumentów nazwanych
    print(opcje)  # {'a': 5}
    dictionary = {'name': "Radek"}
    dictionary['pwd'] = opcje
    print(dictionary)


# a=5 klucz a, wartość 5

connect(a=5)
connect(a=5, b=90)
connect(a=5, c=89)
connect(a=5, name="Radek")


# {'a': 5}
# {'name': 'Radek', 'pwd': {'a': 5}}
# {'a': 5, 'b': 90}
# {'name': 'Radek', 'pwd': {'a': 5, 'b': 90}}
# {'a': 5, 'c': 89}
# {'name': 'Radek', 'pwd': {'a': 5, 'c': 89}}
# {'a': 5, 'name': 'Radek'}
# {'name': 'Radek', 'pwd': {'a': 5, 'name': 'Radek'}}

def all_params(*args, **kwargs):
    print(args, kwargs)


all_params(1, 2, 3, 4, 5, 6)
all_params(a=9, b=9, c=87, eee="Tom")
# (1, 2, 3, 4, 5, 6) {}
# () {'a': 9, 'b': 9, 'c': 87, 'eee': 'Tom'}
all_params(1, 2, 3, 4, a=9, b=89)
all_params()  # () {}
