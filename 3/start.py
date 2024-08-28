import pakiet
from pakiet import fun  # import konkretnego pliku
import pakiet.fun as pk

print(pakiet)
# <module 'pakiet' from 'C:\\Users\\CSComarch\\PycharmProjects\\pdp-26-08\\pakiet\\__init__.py'>

pakiet.powitanie()  # Dzień dobry
# pakiet.info()  # AttributeError: module 'pakiet' has no attribute 'info'
fun.powitanie()
fun.info()
# Dzień dobry
# Jestem pakietem

pk.info()
pk.powitanie()
# Jestem pakietem
# Dzień dobry
