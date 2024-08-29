from turtledemo.penrose import start

import requests

# pip install requests

url = 'http://api.open-notify.org/astros.json'

response = requests.get(url)
print(response)  # <Response [200]>
# 2.. - ok
# 3.. - ostrzeżenia, przekierowania
# 4.. 404 - błąd, brak zasobu, 400 Bad Request - błedne zapytanie
# 5.. 500 wewnętrzny bład serwera

print(response.text)  # odczytanie jsona z odpowiedzi
response_data = response.json()
print(response_data)
# {'people': [{'craft': 'ISS', 'name': 'Oleg Kononenko'}, {'craft': 'ISS', 'name': 'Nikolai Chub'},
#             {'craft': 'ISS', 'name': 'Tracy Caldwell Dyson'}, {'craft': 'ISS', 'name': 'Matthew Dominick'},
#             {'craft': 'ISS', 'name': 'Michael Barratt'}, {'craft': 'ISS', 'name': 'Jeanette Epps'},
#             {'craft': 'ISS', 'name': 'Alexander Grebenkin'}, {'craft': 'ISS', 'name': 'Butch Wilmore'},
#             {'craft': 'ISS', 'name': 'Sunita Williams'}, {'craft': 'Tiangong', 'name': 'Li Guangsu'},
#             {'craft': 'Tiangong', 'name': 'Li Cong'}, {'craft': 'Tiangong', 'name': 'Ye Guangfu'}],
#  'number': 12,
#  'message': 'success'}
print(type(response_data))  # <class 'dict'>
print(response_data.keys())  # dict_keys(['people', 'number', 'message'])

print(response_data['people'])
print(response_data['people'][0])  # {'craft': 'ISS', 'name': 'Oleg Kononenko'}
print(response_data['people'][0]['name'])  # Oleg Kononenko

for i, p in enumerate(response_data['people'], start=1):
    print(i,p['craft'], p['name'])
# 1 ISS Oleg Kononenko
# 2 ISS Nikolai Chub
# 3 ISS Tracy Caldwell Dyson
# 4 ISS Matthew Dominick
# 5 ISS Michael Barratt
# 6 ISS Jeanette Epps
# 7 ISS Alexander Grebenkin
# 8 ISS Butch Wilmore
# 9 ISS Sunita Williams
# 10 Tiangong Li Guangsu
# 11 Tiangong Li Cong
# 12 Tiangong Ye Guangfu
