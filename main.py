from datos.lista import Lista
from agenda import Agenda

class Main:
    def __init__(self):
        self.contactos = Lista()
        self.imprimirMenu()

    def imprimirMenu(self):
        while True:
            print('''
    ===================== Bienvenido a ContactosApp =====================
    Escoge una de las siguientes opciones:
        1. Ingresar nuevo contacto
        2. Buscar contacto
        3. Visualizar Agenda
        4. Salir
            ''')
            opcion = input()
            if opcion == '1':
                self.ingresarNuevoContacto()
            elif opcion == '2':
                self.buscarContacto()
            elif opcion == '3':
                self.visualizarAgenda()
            elif opcion == '4':
                self.contactos.listar()
                '''print('Adios')
                break'''
            else:
                print('Debe ingresar una opción valida')


    def ingresarNuevoContacto(self):
        print('Nombre del contacto: ')
        nombre = input()
        print('Apellido del contacto: ')
        apellido = input()
        print('Numero del contacto: ')
        numero = input()
        if not self.contactos.vacia():
            existente = False
            aux = self.contactos.primero
            for x in range(self.contactos.cuenta):
                if numero == aux.numero:
                    existente = True
                aux = aux.siguiente
            if existente:
                print('Este numero ya esta registrado')
            else:
                self.contactos.agregar(nombre, apellido, numero)
        else:
            self.contactos.agregar(nombre, apellido, numero)

    def buscarContacto(self):
        print('Ingrese el numero del contacto que desea buscar: ')
        num = input()
        aux = self.contactos.primero
        encontrado = False
        for x in range(self.contactos.cuenta):
            if num == aux.numero:
                print('{} {} - {}'.format(aux.nombre, aux.apellido, aux.numero))
                encontrado = True
            aux = aux.siguiente
        if not encontrado:
            print('No se han encontrado resultados. ¿Desea agregar nuevo contacto? (s/n)')
            while True:
                op = input()
                if op in ('s', 'S'):
                    print('Nombre del contacto: ')
                    nom = input()
                    print('Apellido del contacto: ')
                    ape = input()
                    self.contactos.agregar(nom, ape, num)
                    break
                elif op in ('n', 'N'):
                    break

    def visualizarAgenda(self):
        agenda = Agenda(self.contactos)

m = Main()