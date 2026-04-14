class AgenciaDeNoticias:
    def __init__(self):
        self.subscriptores = []

    def adjuntar(self, subscriptor):
        self.subscriptores.append(subscriptor)

    def notificar(self, mensaje):
        for sub in self.subscriptores:
            sub.actualizar(mensaje)

class Newssubscriptor:
    def actualizar(self, mensaje):
        print(f"subscriptor reicibio noticia: {mensaje}")
