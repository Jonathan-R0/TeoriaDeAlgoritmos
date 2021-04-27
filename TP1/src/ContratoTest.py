import pytest
import unittest
from Contrato import Contrato


class ContratoTest(unittest.TestCase):

    def testCreoUnContratoYVerificoLosTiemposInicialesYFinales(self):
        c = Contrato(t_inicio=2, t_final=7)
        assert c.t_inicio == 2
        assert c.t_final == 7

    def testCreoDosContratosYVerificoLosTiemposInicialesYFinales(self):
        c1 = Contrato(t_inicio=4, t_final=9)
        c2 = Contrato(t_inicio=1, t_final=11)
        assert c1.t_inicio == 4
        assert c1.t_final == 9
        assert c2.t_inicio == 1
        assert c2.t_final == 11

    def testCreoUnContratoConTiempoInicialInvalidoYVerificoQueLanceUnaExcepcion(self):
        with pytest.raises(Exception, match="t_inicio has to be of type 'int' or 'float', not <class 'str'>."):
            c = Contrato("a", 4)

    def testCreoUnContratoConTiempoFinalInvalidoYVerificoQueLanceUnaExcepcion(self):
        with pytest.raises(Exception, match="t_final has to be of type 'int' or 'float', not <class 'NoneType'>."):
            c = Contrato(5, None)

    def testCreoUnContratoConTiempoFinalMenorATiempoInicialYVerificoQueLanceUnaExcepcion(self):
        with pytest.raises(Exception, match="t_final value has to be greater than t_inicio."):
            c = Contrato(t_inicio=5, t_final=3)

    def testCreoUnContratoConTiempoInicialInvalidoYVerificoQueLanceUnaExcepcion(self):
        with pytest.raises(Exception, match="t_inicio value has to be greater or equal to 0."):
            c = Contrato(t_inicio=-1, t_final=3)
