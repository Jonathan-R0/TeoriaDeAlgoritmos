import pytest
import unittest
from Parseador import Parseador

class ParseadorTest(unittest.TestCase):

    def testParseadorDevuelveContratoEsperado(self):

        parser = Parseador("TestCases/Test1.txt")
        contrato = parser.getProximoContrato()

        assert contrato is not None
        assert contrato.t_inicio == 1
        assert contrato.t_final == 3
        assert contrato.nombre == "Test"

    def testParseadorOmiteContratoInvalido(self):

        parser = Parseador("TestCases/Test2.txt")
        contrato = parser.getProximoContrato()

        assert contrato is None

    def testParseadorObtenerTodosLosContratos(self):

        parser = Parseador("TestCases/Test3.txt")
        contratos = parser.getTodosLosContratos()

        assert len(contratos) == 2
        assert contratos[0].t_inicio == 1
        assert contratos[0].t_final == 3
        assert contratos[1].t_inicio == 4
        assert contratos[1].t_final == 5
