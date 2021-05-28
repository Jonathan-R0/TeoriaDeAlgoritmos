from Contrato import Contrato


class PlanificadorGreedy:

    def __init__(self, listaDeContratos=[]):
        """ 
            Crea el planificador. Si se pasa una lista con objetos que no sean contratos levanta una excepcion.
        """

        self.listaDeContratos = []
        self.listaDeRestricciones = [None]

        for c in listaDeContratos:
            if not isinstance(c, Contrato):
                raise Exception(f"La lista solo puede contener objetos de tipo Contrato, no de tipo {type(c)}.")

            if c.t_final < c.t_inicio:
                self.listaDeRestricciones.append(c)
            else:
                self.listaDeContratos.append(c)

    def agregarContrato(self, contrato):
        """ 
            Agrega un contrato a la lista. Si se pasa una instancia que no sea de contrato, levanta una excepcion.
        """
        if not isinstance(contrato, Contrato):
            raise Exception(f"Solo se pueden agregar objetos de tipo Contrato, no de tipo {type(contrato)}.")

        if contrato.t_inicio < contrato.t_final:
            self.listaDeContratos.append(contrato)
        else:
            self.listaDeRestricciones.append(contrato)

    def intervalScheduling(self, restrict = None):
        """
            Genera un interval scheduling con la restriccion de que restrict pertenezca al conjunto.
        """

        cronograma = []
        
        if restrict:
            cronograma.append(restrict)

        tiempoFinalizacion = None
        for tarea in self.listaDeContratos:
            if restrict is not None:
                if restrict.superponeCon(tarea):
                    continue
            
            if tiempoFinalizacion is None or tarea.t_inicio >= tiempoFinalizacion:
                tiempoFinalizacion = tarea.t_final
                cronograma.append(tarea)
                

        return cronograma

    def obtenerCronogramaConMayorCantidadDeContratos(self):
        """ 
            Devuelve el cronograma optimo siguiendo el algoritmo de task-scheduling.
        """
        
        bestCronograma = []
        if (len(self.listaDeRestricciones) == 1) and (not self.listaDeContratos):
            return bestCronograma

        self.listaDeContratos.sort(key=lambda c: c.t_final)

        for restriccion in self.listaDeRestricciones:
            cronograma = self.intervalScheduling(restrict=restriccion)
            if len(bestCronograma) < len(cronograma):
                bestCronograma = cronograma
        
        return bestCronograma

    
