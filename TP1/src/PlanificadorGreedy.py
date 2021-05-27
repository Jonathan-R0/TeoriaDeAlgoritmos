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

    def intervalScheduling(self, restrict = None):
        """
            Genera un interval scheduling con la restriccion de que restrict pertenezca al conjunto.
        """

        cronograma = []
        cronograma.append(restrict)
        ultimaTarea = None
        for tarea in self.listaDeContratos:
            if not restrict.superponeCon(tarea) and tarea != restrict:
                if not tarea.superponeCon(ultimaTarea):
                    cronograma.append(tarea)
                    ultimaTarea = tarea

        return cronograma

    def obtenerCronogramaConMayorCantidadDeContratos(self):
        """ 
            Devuelve el cronograma optimo siguiendo el algoritmo de task-scheduling.
        """
        bestCronograma = []
        if not self.listaDeContratos:
            return bestCronograma

        self.listaDeContratos.sort(key=lambda c: c.t_final)
        
        for tarea in self.listaDeContratos:
            cronograma = self.intervalScheduling(restrict = tarea)
            if(len(cronograma) > len(bestCronograma)):
                bestCronograma = cronograma 

        return bestCronograma

    
