from Contrato import Contrato


class PlanificadorGreedy:

    def __init__(self, listaDeContratos=[]):
        """ 
            Crea el planificador. Si se pasa una lista con objetos que no sean contratos levanta una excepcion.
        """
        for c in listaDeContratos:
            if not isinstance(c, Contrato):
                raise Exception(
                    f"La lista solo puede contener objetos de tipo Contrato, no de tipo {type(c)}.")
        self.listaDeContratos = listaDeContratos

    def agregarContrato(self, contrato):
        """ 
            Agrega un contrato a la lista. Si se pasa una instancia que no sea de contrato, levanta una excepcion.
        """
        if not isinstance(contrato, Contrato):
            raise Exception(
                f"Solo se pueden agregar objetos de tipo Contrato, no de tipo {type(contrato)}.")
        self.listaDeContratos.append(contrato)

    def obtenerCronogramaConMayorCantidadDeContratos(self):
        """ 
            Devuelve el cronograma optimo siguiendo el algoritmo de task-scheduling.
        """
        cronograma = []
        if not self.listaDeContratos:
            return cronograma

        self.listaDeContratos.sort(key=lambda c: c.t_final)
        cronograma.append(self.listaDeContratos[0])
        finalizacion = self.listaDeContratos[0].t_final

        for contrato in self.listaDeContratos[1:]:
            if not contrato.superponeCon(finalizacion):
                cronograma.append(contrato)
                finalizacion = contrato.t_final

        return cronograma

    
