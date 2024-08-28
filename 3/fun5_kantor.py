# stworzyc aplikacje kantor(funkcja)
# ma posiadac dwie funkcje wew eur i usd
# w zaleznosci od parametru zwracamy daną funkcję (adres funkcji)
# mozliwosc przekazania dowolnej kwoty do wymiany
def kantor(waluta):
    def usd(kwota=0):
        print(f"Wymieniam dolary {kwota}", kwota * 4.01)

    def eur(kwota=0):
        print(f"Wymieniam euro {kwota}", kwota * 4.30)

    if waluta == "eur":
        return eur
    else:
        return usd  # zwracamy adres


kantor_usd = kantor('usd')
kantor_usd(1000)

kantor_eur = kantor('eur')
kantor_eur(200)
# Wymieniam dolary 1000 4010.0
# Wymieniam euro 200 860.0
