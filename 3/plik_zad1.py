# działania z plikami
# context manager
# with - context manager w pythonie
# open() - praca pliku, zwraca filehandler
# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', 'w', encoding='utf-8') as fh:  # fh - filehandler - rura do pliku
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Kolejne\n")

# x - sprawdza, czy plik istnieje
# with open("test.log", "x") as f:
#     f.write("Cokolwiek")
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdp-26-08\3\plik_zad1.py", line 21, in <module>
#     with open("test.log", "x") as f:
#          ^^^^^^^^^^^^^^^^^^^^^
# FileExistsError: [Errno 17] File exists: 'test.log'

# w - kasuje plik, jeśli istniał wcześniej !!!
with open('test.log', 'w', encoding='utf-8') as file:
    file.write('Nadpisane\n')

with open('test.log', 'a', encoding='utf-8') as f:
    f.write("Dopisane\n")
    f.write("Dopisane\n")
    f.write("Dopisane\n")
    f.write("Dośdane\n")
    f.write("Dośćąźdane\n")

with open('test.log', 'r', encoding='utf-8') as f:
    lines = f.read()

print(lines)
# encoding='utf-8' - zapisanie w kodowaniu utf-8
