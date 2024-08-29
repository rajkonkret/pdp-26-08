import requests as re

# url = 'https://api.nbp.pl/api/exchangerates/rates/A/USD/'
url = 'https://api.nbp.pl/api/exchangerates/rates/A/EUR/'
response = re.get(url)
print(response)

print(response.text)
# {"table": "A", "currency": "dolar amerykański", "code": "USD",
#  "rates": [{"no": "168/A/NBP/2024", "effectiveDate": "2024-08-29", "mid": 3.8670}]}

resp_data = response.json()
waluta = resp_data['currency']
kod = resp_data['code']
kurs = resp_data['rates'][0]['mid']

print(kod, waluta, kurs)
# USD dolar amerykański 3.867
# EUR euro 4.2862
# fuzzbuzz
