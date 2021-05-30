import sys
from Juego import JuegoCartas

if __name__ == "__main__":

    file = open(sys.argv[1], "r")
    linea = file.readline().split(',')
    file.close()

    cartas = [int(x) for x in linea]
    juego = JuegoCartas(cartas)
    print(juego)
