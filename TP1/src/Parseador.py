from Contrato import Contrato
import sys

class Parseador():

    def __init__(self, filepath):
        if not filepath:
            raise Exception("Es necesario proveer la ruta a un archivo")
        
        try:
            self.file = open(filepath, "r")
        except FileNotFoundError:
            print("El archivo no existe")
            raise

    def getProximoContrato(self):
        linea = self.file.readline()
        if not linea:
            raise EOFError

        tokens = linea.split(",")
        nombre = tokens[0]
        t_inicio = int(tokens[1])
        t_final = int(tokens[2])

        if (t_final - t_inicio) > 168:
            print("Los contratos no pueden exceder la duracion de una semana, omitiendo...", file = sys.stderr)
            return None


        return Contrato(t_inicio, t_final, nombre)

    def getTodosLosContratos(self):
        contratos = []

        while True:
            try:
                contrato = self.getProximoContrato()
            except EOFError:
                break

            if contrato is not None:
                contratos.append(contrato)

        return contratos




    def __del__(self):
        if self.file:
            self.file.close()


