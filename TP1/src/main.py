import sys
from Contrato import Contrato
from PlanificadorGreedy import PlanificadorGreedy
from Parseador import Parseador
from StressTester import Tester


def main():

    parseador = Parseador(sys.argv[1])
    contratos = parseador.getTodosLosContratos()

    planificador = PlanificadorGreedy(contratos)
    schedule = planificador.obtenerCronogramaConMayorCantidadDeContratos()

    for contrato in schedule:
        print(contrato)


def timeTest(iterations):
    tester = StressTester(iterations)
    tester.run()


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "t":
        timeTest(sys.argv[2])
    else:
        main()
