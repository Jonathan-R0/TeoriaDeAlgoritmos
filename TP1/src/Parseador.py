from Contrato import Contrato
import sys


class Parseador():

    def __init__(self, filepath):
        """
            Construye el objeto parseador. Requiere de una ruta a un archivo.
            Si no encuentra el archivo, o no se provee uno, levanta una excepcion
        """
        if not filepath:
            raise Exception("Es necesario proveer la ruta a un archivo")

        try:
            self.file = open(filepath, "r")
        except FileNotFoundError:
            print("El archivo no existe")
            raise

    def getProximoContrato(self):
        """
            Devuelve una instancia de un nuevo contrato. Si el contrato tiene una duracion de una semana lo omite y devuelve None.
            Si no puede leer del archivo, levanta un EOFError.
        """
        linea = self.file.readline()
        if not linea:
            raise EOFError

        tokens = linea.split(",")
        nombre = tokens[0]
        t_inicio = int(tokens[1])
        t_final = int(tokens[2])

        if (t_final - t_inicio) > 168:
            print(
                "Los contratos no pueden exceder la duracion de una semana, omitiendo...", file=sys.stderr)
            return None

        return Contrato(t_inicio, t_final, nombre)

    def getTodosLosContratos(self):
        """ 
            Devuelve una lista con todos los contratos validos que se encuentren en el archivo.
        """
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
        """ 
            Destruye el objeto y, si hay un archivo abierto, lo cierra.
        """
        if self.file:
            self.file.close()
