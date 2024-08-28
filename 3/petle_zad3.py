# while - petla sterowana warunkiem

# pętla nieskonczona
# while True:
#     print("Komunikat1 !")

licznik = 0
while True:
    licznik += 1
    print('Komunikat 2 !!')
    if licznik > 10:
        break  # przrywa pętle
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!

print(licznik)  # 11
licznik = 0

while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
#
# password = input("Podaj hasło")
# while password != 'secret':
#     password = input("Błędne hasło, podaj ponownie")
# print("Hasło prawidłowe")
# Błędne hasło, podaj ponownieewrew
# Błędne hasło, podaj ponownieeefrwe
# Błędne hasło, podaj ponownieasafdf
# Błędne hasło, podaj ponowniesecret
# Hasło prawidłowe


# lista = []
# lista_int = []
# while True:
#     wej = input("Podaj liczbę")
#     if not wej.isnumeric():
#         break
#     lista.append(wej)
#     lista_int.append(int(wej))
#
# print(lista)
# print(lista_int)
# # ['1', '3', '5', '7']
# # [1, 3, 5, 7]

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
element_to_remove = 5
while element_to_remove in my_list:
    my_list.remove(element_to_remove)

print(my_list)  # [1, 2, 3, 4, 6]
