# od Pythona 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programowania")

match lang.lower().strip():
    case "python":
        lista.append("Znam Python")
    case "java":
        lista.append("Znam Javę")
    case _:  # wartość domyslna, else
        print("Nie znam takiego języka")

print(lista)
