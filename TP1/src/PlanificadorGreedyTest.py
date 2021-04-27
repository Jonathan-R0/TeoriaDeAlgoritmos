import pytest
import unittest
from PlanificadorGreedy import PlanificadorGreedy
from Contrato import Contrato

# cC


class PlanificadorGreedyTest(unittest.TestCase):

    def testInicializoUnPlanificadorSinListaDeContratosYVerificoQueEsteVacia(self):
        p = PlanificadorGreedy()
        assert not p.listaDeContratos

    def testInicializoUnPlanificadorConUnaListaDeDosContratosYVerificoQueTengaLongitudDos(self):
        contratos = [
            Contrato(t_inicio=2, t_final=7),
            Contrato(t_inicio=4, t_final=6)
        ]
        p = PlanificadorGreedy(contratos)
        assert len(p.listaDeContratos) == 2

    def testAgregoDosContratosAlPlanificadorYVerificoLaCantidadDeContratos(self):
        p = PlanificadorGreedy([])
        p.agregarContrato(Contrato(t_inicio=2, t_final=11))
        p.agregarContrato(Contrato(t_inicio=11, t_final=17))
        assert len(p.listaDeContratos) == 2

    def testCreoUnPlanificadorConUnContratoLeAgregoDosMasYVerificoLaCantidadDeContratos(self):
        contratos = [
            Contrato(t_inicio=2, t_final=9)
        ]
        p = PlanificadorGreedy(contratos)
        p.agregarContrato(Contrato(3, 4))
        p.agregarContrato(Contrato(11, 14))
        assert len(p.listaDeContratos) == 3

    def test1PlanificacionCorrecta(self):
        p = PlanificadorGreedy()
        cronograma = p.obtenerCronogramaConMayorCantidadDeContratos()
        assert not cronograma

    def test2PlanificacionCorrecta(self):
        c1 = Contrato(2, 5)
        c2 = Contrato(0, 3)
        c3 = Contrato(4, 11)
        p = PlanificadorGreedy([c1, c2, c3])
        cronograma = p.obtenerCronogramaConMayorCantidadDeContratos()
        assert cronograma == [c2, c3]

    def test3PlanificacionCorrecta(self):
        c1 = Contrato(0, 3)
        c2 = Contrato(0, 7)
        c3 = Contrato(4, 9)
        c4 = Contrato(8, 9)
        c5 = Contrato(10, 14)
        p = PlanificadorGreedy([c1, c2, c3, c4, c5])
        cronogrma = p.obtenerCronogramaConMayorCantidadDeContratos()
        assert cronogrma == [c1, c3, c5]

    def testInicializoUnPlanificadorConUnaListaQueNoContieneSoloContratosYVerificoQueSeLanceUnaExcepcion(self):
        with pytest.raises(Exception, match="La lista solo puede contener objetos de tipo Contrato, no de tipo <class 'str'>."):
            c1 = Contrato(t_inicio=2, t_final=7)
            c2 = "no soy un contrato"
            c3 = Contrato(t_inicio=4, t_final=9)
            p = PlanificadorGreedy([c1, c2, c3])

    def testIntentoAgregarUnObjetoQueNoEsDeTipoContratoYVerificoQueSeLanceUnaExcepcion(self):
        with pytest.raises(Exception, match="Solo se pueden agregar objetos de tipo Contrato, no de tipo <class 'str'>."):
            p = PlanificadorGreedy()
            p.agregarContrato("no soy un contrato")
