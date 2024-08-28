# funkcja wewnętrzna, zagnieżdzona
# uzywane w dekoratorach

def fun1():
    print("To jest fun1")

    # deklaracja funkcji
    def fun2():
        print("To jest fun2")

    return fun2  # zwrócenie adresu funkcji 9referencji)


fun1()
xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x000002AFD16C8B80>
print(type(xFun))
# nazwa_funkcji(zienna przechowująca adres funkcji) i nawiasy ()
xFun()
# To jest fun1
# To jest fun1
# <function fun1.<locals>.fun2 at 0x000001CFDFBFC220>
# <class 'function'>
# To jest fun2
