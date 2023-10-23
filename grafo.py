from lista import Lista as ListaArista
from cola import Cola

class Arista:

    def __init__(self, vertice, peso):
        self.vertice = vertice
        self.peso = peso

    def __str__(self):
        return f"{self.vertice} {self.peso}"

def criterio_comparacion(value, criterio):
    if isinstance(value, (int, str, bool)):
        return value
    else:
        dic_atributos = value.__dict__
        if criterio in dic_atributos:
            return dic_atributos[criterio]
        else:
            print('no se puede ordenar por este criterio')


class Grafo():

    def __init__(self, dirigido=True):
        self.__elements = []
        self.dirigido = dirigido

    def insert_vertice(self, value, criterio=None):
        if len(self.__elements) == 0 or criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[-1][0], criterio):
            self.__elements.append([value, ListaArista(), False])
        elif criterio_comparacion(value, criterio) < criterio_comparacion(self.__elements[0][0], criterio):
            self.__elements.insert(0, [value, ListaArista(), False])
        else:
            index = 1
            while criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[index][0], criterio):
                index += 1
            self.__elements.insert(index, [value, ListaArista(), False])

    def insert_arist(self, value, vertice_ori, vertice_des, criterio_vertice=None, criterio_arista=None):
        from copy import copy
        origen = self.search_vertice(vertice_ori, criterio_vertice)
        destino = self.search_vertice(vertice_des, criterio_vertice)
        if origen is not None and destino is not None:
            self.get_element_by_index(origen)[1].insert(value, criterio_arista)
            if not self.dirigido:
                new_arista = copy(value)
                new_arista.vertice = vertice_ori
                self.get_element_by_index(destino)[1].insert(new_arista, criterio_arista)

    def search_vertice(self, search_value, criterio=None):
        position = None
        first = 0
        last = self.size() - 1
        while (first <= last and position == None):
            middle = (first + last) // 2
            if search_value == criterio_comparacion(self.__elements[middle][0], criterio):
                position = middle
            elif search_value > criterio_comparacion(self.__elements[middle][0], criterio):
                first = middle + 1
            else:
                last = middle - 1
        return position

    def delete_vertice(self, value, criterio=None):
        return_value = None
        pos = self.search_vertice(value, criterio)
        if pos is not None:
            return_value = self.__elements.pop(pos)
            for vertice in self.__elements:
                vertice[1].delete(value, 'vertice')

        return return_value

    def delete_arista(self, origen, destino):
        pos_origen = mi_grafo.search_vertice(origen)
        if pos_origen is not None:
            ver_origen = mi_grafo.get_element_by_index(pos_origen)
            delete = ver_origen[1].delete(destino, 'vertice')
            if not self.dirigido:
                pos_destino = mi_grafo.search_vertice(destino)
                if pos_destino is not None:
                    ver_destino = mi_grafo.get_element_by_index(pos_destino)
                    ver_destino[1].delete(origen, 'vertice')
            return delete

    def size(self):
        return len(self.__elements)

    def barrido(self):
        for value in self.__elements:
            print(value[0])
            print('Arsitas --------------------')
            value[1].barrido()
            print()

    # def order_by(self, criterio=None, reverse=False):
    #     dic_atributos = self.__elements[0][0].__dict__
    #     if criterio in dic_atributos:
    #         def func_criterio(valor):
    #             return valor.__dict__[criterio]

    #         self.__elements.sort(key=func_criterio, reverse=reverse)
    #     else:
    #         print('no se puede ordenar por este criterio')

    def get_element_by_index(self, index):
        return_value = None
        if index >= 0 and index < self.size():
            return_value = self.__elements[index]
        return return_value

    def is_adyacent(self, origen, destino):
        result = False
        pos_origen = mi_grafo.search_vertice(origen)
        if pos_origen is not None:
            ver_origen = mi_grafo.get_element_by_index(pos_origen)
            arista = ver_origen[1].search(destino, 'vertice')
            result = True if arista is not None else False
        return result

    def adyacents(self, origen):
        pos_origen = mi_grafo.search_vertice(origen)
        if pos_origen is not None:
            ver_origen = mi_grafo.get_element_by_index(pos_origen)
            ver_origen[1].barrido()

    def mark_as_not_visited(self):
        for vertice in self.__elements:
            vertice[2] = False

    def deep_list(self, poscion=0):
        origen = self.get_element_by_index(poscion)
        if origen is not None:
            if not origen[2]:
                origen[2] = True
                print(origen[0])
                adjacentes = origen[1]
                for index in range(adjacentes.size()):
                    arista = adjacentes.get_element_by_index(index).vertice
                    vertice_adjacente = self.search_vertice(arista)
                    if vertice_adjacente is not None:
                        adjacente = self.get_element_by_index(vertice_adjacente)
                        if not adjacente[2]:
                            self.deep_list(poscion=vertice_adjacente)
                
    def amplitude_list(self, posicion=0):
        origen = self.get_element_by_index(posicion)
        if origen is not None:
            cola_pendientes = Cola()
            cola_pendientes.arrive(origen)
            while not cola_pendientes.size() == 0:
                vertice = cola_pendientes.atention()
                if not vertice[2]:
                    vertice[2] = True
                    print(vertice[0])
                    adjacentes = vertice[1]
                    for index in range(adjacentes.size()):
                        arista = adjacentes.get_element_by_index(index).vertice
                        vertice_adjacente = self.search_vertice(arista)
                        if vertice_adjacente is not None:
                            adjacente = self.get_element_by_index(vertice_adjacente)
                            if not adjacente[2]:
                                cola_pendientes.arrive(adjacente)
            
    def has_path(self, origen, destino):
        result = False
        origen = self.search_vertice(origen)
        if origen is not None:
            vertice_origen = self.get_element_by_index(origen)
            if not vertice_origen[2]:
                vertice_origen[2] = True
                print(vertice_origen[0])
                adjacentes = vertice_origen[1]
                pos_destino = adjacentes.search(destino, 'vertice')
                if pos_destino is not None:
                    result = True
                    return result
                for index in range(adjacentes.size()):
                    arista = adjacentes.get_element_by_index(index).vertice
                    vertice_adjacente = self.search_vertice(arista)
                    if vertice_adjacente is not None:
                        adjacente = self.get_element_by_index(vertice_adjacente)
                        if not adjacente[2]:
                            result = self.has_path(adjacente[0], destino)
        return result

from random import randint

mi_grafo = Grafo(dirigido=False)

mi_grafo.insert_vertice('A')
mi_grafo.insert_vertice('B')
mi_grafo.insert_vertice('F')
mi_grafo.insert_vertice('Z')
mi_grafo.insert_vertice('W')
mi_grafo.insert_vertice('J')

mi_grafo.insert_arist(Arista('B', 14), 'A', 'B', criterio_arista='vertice')
mi_grafo.insert_arist(Arista('Z', 144), 'A', 'Z', criterio_arista='vertice')
mi_grafo.insert_arist(Arista('J', 4), 'A', 'J', criterio_arista='vertice')
mi_grafo.insert_arist(Arista('B', 4), 'J', 'B', criterio_arista='vertice')
mi_grafo.insert_arist(Arista('J', 33), 'Z', 'J', criterio_arista='vertice')
mi_grafo.insert_arist(Arista('W', 133), 'F', 'W', criterio_arista='vertice')
mi_grafo.insert_arist(Arista('W', 22), 'A', 'W', criterio_arista='vertice')

mi_grafo.barrido()

origen = 'A'
destino = 'Z'

pos_origen = mi_grafo.search_vertice(origen)
if pos_origen is not None:
    ver_origen = mi_grafo.get_element_by_index(pos_origen)
    pos_arista = ver_origen[1].search(destino, 'vertice')
    if pos_arista is not None:
        arista = ver_origen[1].get_element_by_index(pos_arista)
        print(f'datos de la arista origen {origen} destino {arista.vertice} peso {arista.peso}')


# print(mi_grafo.delete_arista('A', 'B'))
# print(mi_grafo.delete_vertice('B'))
print(mi_grafo.is_adyacent('A', 'F'))
print()
mi_grafo.adyacents('A')

mi_grafo.barrido()
print()
# mi_grafo.deep_list(poscion=2)
# print()
# mi_grafo.deep_list()
# mi_grafo.mark_as_not_visited()
# print()
# mi_grafo.amplitude_list()


print(mi_grafo.has_path('A', 'F'))