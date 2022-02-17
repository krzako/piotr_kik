from plansza import Plansza


class Gra:
    def __init__(self):
        print("Gra")
        self.koniec = False
        self.aktualny_gracz = "x"
        self.plansza = Plansza()

    def pobierz_wspolrzedne(self):
        return 5, 3

    def czy_wygral(self):
        return False

    def czy_remis(self):
        return False

    def print(self):
        print("printuje gre")

    def zmien_gracza(self):
        pass

    def wykonaj_ture(self):
        print(f"tura {self.aktualny_gracz}. podaj x y ")
        x, y = self.pobierz_wspolrzedne()
        self.plansza.zajmij_pole(x, y, self.aktualny_gracz)

        self.print()

        if self.czy_wygral():
            print(f"Wygral gracz {self.aktualny_gracz}")
            self.koniec == True

        if self.czy_remis():
            print(f"Remis")
            self.koniec == True

        self.zmien_gracza()