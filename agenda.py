from graphviz import Digraph

class Agenda:
    def __init__(self, lista):
        self.lista = lista
        self.visualizarAgenda()

    def visualizarAgenda(self):
        d = Digraph(comment='Agenda', format='png')
        aux = self.lista.primero
        for x in range(self.lista.cuenta):
            d.node(str(x) ,aux.nombre + '\n' + aux.apellido + '\n' + aux.numero, shape='folder')
            if x != 0:
                d.edge(str(x-1), str(x))
                d.edge(str(x), str(x-1))

            aux = aux.siguiente
        d.view()
