class Plansza:
    def __init__(self):
        print("Witam Plansza jestem")
        self.puste_pole = "_"
        self.reset()

    def reset(self):
        print("reset")
        self.pola = [
            [self.puste_pole, self.puste_pole, self.puste_pole],
            [self.puste_pole, self.puste_pole, self.puste_pole],
            [self.puste_pole, self.puste_pole, self.puste_pole]
        ]
        self.print()

    def print(self):
        print(" |0|1|2|y")
        for poziom in range(3):
            print(f"{poziom}|{self.pola[poziom][0]}|{self.pola[poziom][1]}|{self.pola[poziom][2]}|")
        print("x\n")

    # Funkcja zwraca None jeśli zajmie pole lub stringa z błędem
    def zajmij_pole(self, x, y, znak):
        if x > 2 or x < 0:
            return "x jest niepoprawny"

        if y > 2 or y < 0:
            return "y jest niepoprawny"

        if self.pola[x][y] != self.puste_pole:
            return "pole jest zajete"

        self.pola[x][y] = znak
        return None

    def czy_wygral(self, znak):
        if self.pola[0][0] == znak and self.pola[1][1] == znak and self.pola[2][2] == znak:
            return True

        if self.pola[2][0] == znak and self.pola[1][1] == znak and self.pola[0][2] == znak:
            return True

        for x in range(2):
            if self.pola[x][0] == znak and self.pola[x][1] == znak and self.pola[x][2] == znak:
                return True

        for y in range(2):
            if self.pola[0][y] == znak and self.pola[1][y] == znak and self.pola[2][y] == znak:
                return True

        return False

