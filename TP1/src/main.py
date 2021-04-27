from Contrato import Contrato
from PlanificadorGreedy import PlanificadorGreedy


def main():

    contratos = []
    c1 = Contrato(t_inicio=0, t_final=12)
    c2 = Contrato(t_inicio=3, t_final=9)
    c3 = Contrato(t_inicio=7, t_final=8)
    c4 = Contrato(t_inicio=14, t_final=15)
    contratos.append(c1)
    contratos.append(c2)
    contratos.append(c3)
    contratos.append(c4)

    planificador = PlanificadorGreedy(contratos)

    planificador.agregarContrato(Contrato(17, 21))
    planificador.agregarContrato(Contrato(18, 25))
    planificador.agregarContrato(Contrato(19, 22))
    planificador.agregarContrato(Contrato(23, 25))

    cronograma = planificador.obtenerCronogramaConMayorCantidadDeContratos()

    for c in cronograma:
        print(c)


main()
