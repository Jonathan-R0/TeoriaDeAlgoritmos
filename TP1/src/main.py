from Contrato import Contrato
from PlanificadorGreedy import PlanificadorGreedy


def main():
    print("Ejemplo 1:\n\n")
    ejemplo1()
    print("\n\nEjemplo 2:\n\n")
    ejemplo2()
    print("\n\nEjemplo que demuestra que elegir primero los contratos mas cortos no es optimo:\n\n")
    ejemploExtraQueDemuestraQueElegirAquelDeMenorDuracionPrimeroNoFunciona()


def ejemplo1():

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


def ejemplo2():

    contratos = []
    c1 = Contrato(t_inicio=0, t_final=12)
    c2 = Contrato(t_inicio=1, t_final=4)
    c3 = Contrato(t_inicio=6, t_final=8)
    c4 = Contrato(t_inicio=11, t_final=16)
    contratos.append(c1)
    contratos.append(c2)
    contratos.append(c3)
    contratos.append(c4)

    planificador = PlanificadorGreedy(contratos)
    cronograma = planificador.obtenerCronogramaConMayorCantidadDeContratos()

    for c in cronograma:
        print(c)


def ejemploExtraQueDemuestraQueElegirAquelDeMenorDuracionPrimeroNoFunciona():

    contratos = []
    c1 = Contrato(t_inicio=7, t_final=10)
    c2 = Contrato(t_inicio=3, t_final=8)
    c3 = Contrato(t_inicio=9, t_final=18)
    contratos.append(c1)
    contratos.append(c2)
    contratos.append(c3)

    planificador = PlanificadorGreedy(contratos)
    cronograma = planificador.obtenerCronogramaConMayorCantidadDeContratos()

    for c in cronograma:
        print(c)


main()
