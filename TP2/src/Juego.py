class JuegoCartas:
    def __init__(self, cartas: list):

        self.iteraciones = 0

        self.cartas = cartas
        self.l = len(cartas)
        self.mejores = [[0 for _ in range(self.l)] for _ in range(self.l)]
        self._maxPick()
        self._misJugadas = self._generarMisJugadas()
        self.opponents_plays = [p for p in cartas if p not in self._misJugadas]

    def _maxPick(self):

        for resto in range(self.l):
            for f in range(resto, self.l):
                i = f - resto

                a = self.mejores[i + 2][f] if (i + 2) <= f else 0
                b = self.mejores[i + 1][f - 1] if (i + 1) <= (f - 1) else 0
                c = self.mejores[i][f - 2] if i <= (f - 2) else 0

                self.mejores[i][f] = max(self.cartas[i] + min(a, b),
                                         self.cartas[f] + min(b, c))
                self.iteraciones += 1

    def getMaxPick(self) -> int:
        return self.mejores[0][-1]

    def _generarMisJugadas(self) -> list:
        i = 0
        f = self.l - 1
        picks = []
        while f - i >= 2:
            self.iteraciones += 1
            seleccionInicial = self.cartas[i] + \
                min(self.mejores[i + 2][f], self.mejores[i + 1][f - 1])
            seleccionFinal = self.cartas[f] + \
                min(self.mejores[i + 1][f - 1], self.mejores[i][f - 2])
            picks.append(i if seleccionInicial > seleccionFinal else f)
            if seleccionInicial > seleccionFinal:
                if self.mejores[i + 2][f] < self.mejores[i + 1][f - 1]:
                    i += 1
                else:
                    f -= 1
                i += 1
            else:
                if self.mejores[i + 1][f - 1] < self.mejores[i][f - 2]:
                    i += 1
                else:
                    f -= 1
                f -= 1
        if f - i == 1:
            picks.append(i if self.cartas[i] > self.cartas[f] else f)
        else:
            picks.append(i)

        return [self.cartas[i] for i in picks]

    def __str__(self) -> str:

        return "Jugador 1: \nCartas elegidas: " + \
               ",".join([str(p) for p in self._misJugadas]) + "\n" + \
               "Puntos sumados: " + str(self.getMaxPick()) + "\n\n" + \
               "Jugador 2: \nCartas elegidas: " + \
               ",".join([str(p) for p in self.opponents_plays]) + "\n" + \
               "Puntos sumados: " + str(sum(self.opponents_plays))
