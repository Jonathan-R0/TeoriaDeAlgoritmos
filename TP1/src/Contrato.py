class Contrato:

    def __init__(self, t_inicio, t_final):
        self.t_inicio = t_inicio
        self.t_final = t_final

    def __str__(self):
        return f'Contrato desde {self.t_inicio} hasta {self.t_final}.'
