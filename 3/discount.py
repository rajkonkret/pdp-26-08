from datetime import date, datetime, timedelta

today = date.today()
print(today)  # 2024-08-28
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print("Aktualny czas", time)  # Aktualny czas 2024-08-28 09:31:17.146830

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days = 0, seconds = 0, microseconds = 0,
# milliseconds = 0, minutes = 0, hours = 0, weeks = 0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2024-08-29

print(time.time())  # 09:35:19.819555
print(today.day)  # 28

formatted_date = datetime.now().strftime("%d/%m/%Y")
print(formatted_date)  # 28/08/2024

formatted_time = datetime.now().strftime('%H:%M')
print(formatted_time)  # 09:37

data_object = datetime.strptime("28/08/2024", "%d/%m/%Y")
print(data_object)  # 2024-08-28 00:00:00
print(type(data_object))  # <class 'datetime.datetime'>

# praca domowa
# wyświetlić date w formacie 12h

products = [
    {'sku': 1, 'exp_date': today, 'price': 200},
    {'sku': 2, 'exp_date': today, 'price': 100},
    {'sku': 3, 'exp_date': tomorrow, 'price': 50.55},
    {'sku': 4, 'exp_date': today, 'price': 190.99},
]

print(products)
for p in products:
    # print(p)
    # print(type(p))  # <class 'dict'>
    # exp_date =  p['exp_date']
    # print(exp_date)
    if p['exp_date'] != today:
        continue  # wraca na początek pętli, bierze kolejny element
    p['price'] *= 0.8  # p = p * 0.8
    print(f"""Price for sku {p['sku']}
is now {p['price']}""")
# Price for sku 1
# is now 160.0
# Price for sku 2
# is now 80.0
# Price for sku 4
# is now 152.792
