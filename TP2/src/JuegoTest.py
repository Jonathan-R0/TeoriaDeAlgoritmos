import pytest
import unittest
from Juego import JuegoCartas


class JuegoTest(unittest.TestCase):

    def testSeisCartas(self):
        juego = JuegoCartas([3, 8, 11, 1, 19, 12])
        assert juego.getMaxPick() == 33

    def testDosCartas(self):
        juego = JuegoCartas([1, 7])
        assert juego.getMaxPick() == 7

    def testCuatroCartas(self):
        juego = JuegoCartas([11, 12, 13, 14])
        assert juego.getMaxPick() == 26

    def testCincoCartas(self):
        juego = JuegoCartas([2, 23, 20, 7, 2])
        assert juego.getMaxPick() == 24
        # En este caso el jugador pierde inevitablemente.
