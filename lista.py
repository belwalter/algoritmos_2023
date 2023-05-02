


def criterio_comparacion(value, criterio):
    if isinstance(value, (int, str, bool)):
        # print('es un primitivo')
        return value
    else:
        # print('no es un dato primitivo')
        dic_atributos = value.__dict__
        if criterio in dic_atributos:
            return dic_atributos[criterio]
        else:
            print('no se puede ordenar por este criterio')


class Lista():

    def __init__(self):
        self.__elements = []

    def insert(self, value, criterio=None):
        # print('criterio de insercion', criterio)
        if len(self.__elements) == 0 or criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[-1], criterio):
            self.__elements.append(value)
        elif criterio_comparacion(value, criterio) < criterio_comparacion(self.__elements[0], criterio):
            self.__elements.insert(0, value)
        else:
            index = 1
            while criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[index], criterio):
                index += 1
            self.__elements.insert(index, value)

    def search(self, search_value, criterio=None):
        #! modificra metodo hacer busqueda binaria
        position = None
        for index, value in enumerate(self.__elements):
            if search_value == criterio_comparacion(value, criterio):
                position = index
                break
        return position

    def delete(self, value):
        return_value = None
        pos = self.search(value)
        if pos is not None:
            return_value = self.__elements.pop(pos)
        return return_value

    def size(self):
        return len(self.__elements)

    def barrido(self):
        for value in self.__elements:
            print(value)

    # def get_element_by_value(self, value):
    #     return_value = None
    #     pos = self.search(value)

    #     if pos is not None:
    #         return_value = self.__elements[pos]
    #     return return_value

    def get_element_by_index(self, index):
        return_value = None
        if index >= 0 and index < self.size():
            return_value = self.__elements[index]
        return return_value

    def set_value(self, value, new_value):
        pos = self.search(value)
        if pos is not None:
            value = self.delete(value)
            self.insert(new_value)


class Persona():

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido

    def __str__(self):
        return f'{self.nombre} - {self.apellido}'

class Producto():
    
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo

    def __str__(self):
        return f'{self.id} - {self.tipo}'


persona1 = Persona('Juana', 'Gomez', 34)
persona2 = Persona('Mario', 'Impini', 47)
persona3 = Persona('Laurato', 'Perez', 19)

prod1 = Producto(3, 'abc')
prod2 = Producto(1, 'zxs')
# persona1.
# print(criterio_comparacion(persona1, 'apellido'))

# print(persona1.__dict__)

lista_prueba = Lista()

# lista_prueba.insert(prod1, 'id')
# lista_prueba.insert(prod2, 'id')
lista_prueba.insert(persona1, 'edad')
lista_prueba.insert(persona2, 'edad')
lista_prueba.insert(persona3, 'edad')

lista_prueba.barrido()
# lista_prueba.insert(5)
# lista_prueba.insert(3)
# lista_prueba.insert(1)
# lista_prueba.insert(8)
# lista_prueba.insert(4)
# lista_prueba.insert(6)
# lista_prueba.insert(2)
# lista_prueba.insert(3)
# lista_prueba.insert(7)
# lista_prueba.insert(1)

# lista_prueba.set_value(5, 9)

# lista_prueba.barrido()
# print()
print(lista_prueba.search(34, 'edad'))

# print(lista_prueba.delete(1))
# print()
# lista_prueba.barrido()
# print(lista_prueba.__elements)
# # print(lista_prueba.delete(4))
# # print(lista_prueba.__elements)
# print(lista_prueba.delete(3))
# print(lista_prueba.__elements)


# lista_prueba.barrido()

# print(lista_prueba.get_element_by_value(4))
# print(lista_prueba.get_element_by_value(10))

# print(lista_prueba.get_element_by_index(4))
# print(lista_prueba.get_element_by_index(100))

# lista_value = ['a', 'h', 'z', 'd', 'f']

# for index, value in enumerate(lista_value):
#     if value == 'c':
#         print(f'lo encontre en la posicion {index}')
#     print(index, value)
