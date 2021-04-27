class Contrato:

    def __init__(self, t_inicio, t_final, nombre = " "):
        """ 
            Crea un contrato. Comprueba que los parametros sean instancias de clases esperadas.
        """
        if not (isinstance(t_inicio, int) or isinstance(t_inicio, float)):
            raise Exception(
                f"t_inicio has to be of type 'int' or 'float', not {type(t_inicio)}.")
        if not (isinstance(t_final, int) or isinstance(t_final, float)):
            raise Exception(
                f"t_final has to be of type 'int' or 'float', not {type(t_final)}.")
        if t_inicio < 0:
            raise Exception("t_inicio value has to be greater or equal to 0.")
        self.t_inicio = t_inicio
        self.t_final = t_final
        self.nombre = nombre

    def __str__(self):
        """ 
            Representacion string del contrato.
        """
        return f'Contrato desde {self.t_inicio} hasta {self.t_final} a nombre de {self.nombre}.'

    def superponeCon(self, finalizacion):
        """ 
            Devuelve true si el contrato se superpone con otro dado el tiempo de finalización del ultimo.
        """
        if self.t_final < 168:
            return self.t_inicio < finalizacion
        else:
            return (self.t_final - 168) < finalizacion
