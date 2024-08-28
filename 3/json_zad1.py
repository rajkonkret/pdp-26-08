# json - '{"name":"John", "age":30, "car":null}'
# dane typu klucz-wartosc
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))

# {"name": "Radek", "age": 40, "czy_pali": null}
with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f)

# upiększenie
with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# sortownaie po kluczu
with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open('nasze_dane.json', 'r') as f:
    data = json.load(f)

print(data)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(data))  # <class 'dict'>
print(data['name'])  # Radek

# zmaiana słownika na jsona
json_text = json.dumps(data)
print(type(json_text))  # <class 'str'>
print(json_text)  # {"age": 40, "czy_pali": null, "name": "Radek"}

dict_json = json.loads(json_text)
print(dict_json)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(dict_json))  # <class 'dict'>
