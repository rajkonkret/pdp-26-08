import csv

fields = []
rows = []

# filename = 'records_dict.csv'
filename = 'records3.csv'

with open(filename, "r") as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    print(dialect.delimiter)  # ;
    # StopIteration - odczytał 1024 znki, ustawił na 1025, my musimy wznowic odczyt od miejsca 0
    f.seek(0)  # ustawienie na początek pliku
    csvreader = csv.reader(f, delimiter=dialect.delimiter)
    # csvreader = csv.reader(f, delimiter=";")

    print(csvreader)  # <_csv.reader object at 0x000001FAD54B5840>
    fields = next(csvreader)  # odczyta pierwszy element (wiersz) usatwi odczyt na nstępny
    # print("Fields:", fields)  # Fields: ['name', 'branch', 'year', 'cgpa']
    for row in csvreader:
        # print(row)  # ['Radek', 'Coe', '3', '9.1']
        rows.append(row)

print(rows)
print(fields)
# [['Radek', 'Coe', '3', '9.1'], ['Tomek', 'Coe', '3', '9.1'], ['Zenek', 'Coe', '3', '9.1'], ['Magda', 'Coe', '3', '9.1'], ['Ania', 'Coe', '3', '9.1']]
# ['name', 'branch', 'year', 'cgpa']
# dla ;
# [['Radek;Coe;3;9.1'], ['Tomek;Coe;3;9.1'], ['Zenek;Coe;3;9.1'], ['Magda;Coe;3;9.1'], ['Ania;Coe;3;9.1']]
# ['name;branch;year;cgpa']
