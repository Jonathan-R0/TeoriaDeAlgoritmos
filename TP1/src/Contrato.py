class Contrato:

    def __init__(self, t_inicio, t_final):
        if not (isinstance(t_inicio, int) or isinstance(t_inicio, float)):
            raise Exception(
                f"t_inicio has to be of type 'int' or 'float', not {type(t_inicio)}.")
        if not (isinstance(t_final, int) or isinstance(t_final, float)):
            raise Exception(
                f"t_final has to be of type 'int' or 'float', not {type(t_final)}.")
        if t_inicio > t_final:
            raise Exception("t_final value has to be greater than t_inicio.")
        if t_inicio < 0:
            raise Exception("t_inicio value has to be greater or equal to 0.")
        self.t_inicio = t_inicio
        self.t_final = t_final

    def __str__(self):
        return f'Contrato desde {self.t_inicio} hasta {self.t_final}.'
