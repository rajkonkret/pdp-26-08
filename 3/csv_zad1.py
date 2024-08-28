# pliki csv - pliki w których dane oddzielone są znakiem podziału
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce
# ,;tab

import csv

row = ['Radek', 'Coe', 3, '9.1']  # lista
fields = ['name', 'branch', 'year', 'cgpa']
filename = 'records.csv'

dictionary = dict(zip(fields, row))
print(type(dictionary))
print(dictionary)  # {'name': 'Radek', 'branch': 'Coe', 'year': 3, 'cgpa': '9.1'}

# newline="" - ominięcie problemu pustych linii
with open(filename, 'w', newline="") as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

filename_dict = "records_dict.csv"
with open(filename_dict, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerow(dictionary)  # zapisanie słownika jako csv

dict_list = [
    {'name': 'Radek', 'branch': 'Coe', 'year': 3, 'cgpa': '9.1'},
    {'name': 'Tomek', 'branch': 'Coe', 'year': 3, 'cgpa': '9.1'},
    {'name': 'Zenek', 'branch': 'Coe', 'year': 3, 'cgpa': '9.1'},
    {'name': 'Magda', 'branch': 'Coe', 'year': 3, 'cgpa': '9.1'},
    {'name': 'Ania', 'branch': 'Coe', 'year': 3, 'cgpa': '9.1'},
]

filename_dict_list = 'records3.csv'
with open(filename_dict_list, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(dict_list)  # zapisanie listy słowników jako csv

# delimiter=";" - znak podziału