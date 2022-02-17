from plansza import Plansza
from gra import Gra
## ^^ żeby nie pisać plansza.Plansza(). Teraz mozna po prostu Plansza(). Przy import Plansza trzeba by pisać plansza.Plansza

if __name__ == '__main__':
    gra = Gra()
    while not gra.koniec:
        gra.wykonaj_ture()














    exit()
    plansza = Plansza()

    result = plansza.zajmij_pole(0, 0, "x")
    if result is None:
        print("OK")
    else:
        print(f"error: {result}")
    plansza.print()
    print(f'Czy wygral: {plansza.czy_wygral("x")}')

    result = plansza.zajmij_pole(0, 1, "o")
    if result is None:
        print("OK")
    else:
        print(f"error: {result}")
    plansza.print()
    print(f'Czy wygral: {plansza.czy_wygral("o")}')

    result = plansza.zajmij_pole(1, 1, "x")
    if result is None:
        print("OK")
    else:
        print(f"error: {result}")
    plansza.print()
    print(f'Czy wygral: {plansza.czy_wygral("x")}')

    result = plansza.zajmij_pole(0, 2, "o")
    if result is None:
        print("OK")
    else:
        print(f"error: {result}")
    plansza.print()
    print(f'Czy wygral: {plansza.czy_wygral("o")}')

    result = plansza.zajmij_pole(2, 2, "x")
    if result is None:
        print("OK")
    else:
        print(f"error: {result}")
    plansza.print()
    print(f'Czy wygral: {plansza.czy_wygral("x")}')