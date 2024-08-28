import chardet

# pip install chardet

with open('test.log', "r") as f:
    raw_data = f.read()

print(raw_data)
# Nadpisane
# Dopisane
# Dopisane
# Dopisane
# DoĹ›dane

# rb - odczyt bajtowy
with open('test.log', 'rb') as f:
    raw_data = f.read()

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1254', 'confidence': 0.6609905800215763, 'language': 'Turkish'}
# po zwiększeniu liczby polskich znaków w pliku działą poprawnie
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
encoding = result['encoding']
confidence = result['confidence']
print("Kodowanie:", encoding)
print("Trafność:", confidence)
# Kodowanie: utf-8
# Trafność: 0.99
print(raw_data.decode(encoding=encoding))
# Nadpisane
# Dopisane
# Dopisane
# Dopisane
# Dośdane
# Dośćąźdane
