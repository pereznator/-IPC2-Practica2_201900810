from .contacto import Contacto

class Lista:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.cuenta = 0

    def vacia(self):
        return self.primero == None

    def agregar(self, nombre, apellido, numero):
        if self.vacia():
            self.primero = self.ultimo = Contacto(nombre, apellido, numero)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Contacto(nombre, apellido, numero)
            self.ultimo.anterior = aux
        self.cuenta += 1

    def listar(self):
        aux = self.primero
        for x in range(self.cuenta):
            print(aux.nombre, aux.apellido, aux.numero)
            aux = aux.siguiente
