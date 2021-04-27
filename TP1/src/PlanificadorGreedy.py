from Contrato import Contrato


class PlanificadorGreedy:

    def __init__(self, listaDeContratos=[]):
        for c in listaDeContratos:
            if not isinstance(c, Contrato):
                raise Exception(
                    f"La lista solo puede contener objetos de tipo Contrato, no de tipo {type(c)}.")
        self.listaDeContratos = listaDeContratos

    def agregarContrato(self, contrato):
        if not isinstance(contrato, Contrato):
            raise Exception("Solo se pueden agregar objetos de tipo Contrato.")
        self.listaDeContratos.append(contrato)

    def obtenerCronogramaConMayorCantidadDeContratos(self):
        cronograma = []
        if not self.listaDeContratos:
            return cronograma

        self.listaDeContratos.sort(key=lambda c: c.t_final)
        cronograma.append(self.listaDeContratos[0])
        finalizacion = self.listaDeContratos[0].t_final

        for contrato in self.listaDeContratos:
            if contrato.t_inicio > finalizacion:
                cronograma.append(contrato)
                finalizacion = contrato.t_final

        return cronograma
