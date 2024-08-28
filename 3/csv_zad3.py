import pandas

# pip install pandas

data = pandas.read_csv('records3.csv', delimiter=";")
print(data)
#     name branch  year  cgpa
# 0  Radek    Coe     3   9.1
# 1  Tomek    Coe     3   9.1
# 2  Zenek    Coe     3   9.1
# 3  Magda    Coe     3   9.1
# 4   Ania    Coe     3   9.1
print(data.columns)
# Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
# print(data.items)
# # <bound method DataFrame.items of     name branch  year  cgpa
# # 0  Radek    Coe     3   9.1
# # 1  Tomek    Coe     3   9.1
# # 2  Zenek    Coe     3   9.1
# # 3  Magda    Coe     3   9.1
# # 4   Ania    Coe     3   9.1>
print(data.values)
# [['Radek' 'Coe' 3 9.1]
#  ['Tomek' 'Coe' 3 9.1]
#  ['Zenek' 'Coe' 3 9.1]
#  ['Magda' 'Coe' 3 9.1]
#  ['Ania' 'Coe' 3 9.1]]
