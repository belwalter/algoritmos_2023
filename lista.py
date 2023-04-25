

class Lista():

    def __init__(self):
        self.__elements = []

    def insert(self, value):
        if len(self.__elements) == 0:
            self.__elements.append(value)
        elif value < self.__elements[0]:
            self.__elements.insert(0, value)
        elif value >= self.__elements[-1]:
            self.__elements.append(value)
        else:
            index = 1
            while value >= self.__elements[index]:
                index += 1
            self.__elements.insert(index, value)

    def search(self, search_value):
        position = None
        for index, value in enumerate(self.__elements):
            if search_value == value:
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

    def get_element_by_value(self, value):
        return_value = None
        pos = self.search(value)
        
        if pos is not None:
            return_value = self.__elements[pos]
        return return_value

    def get_element_by_index(self, index):
        return_value = None
        if index >= 0 and index < self.size():
            return_value = self.__elements[index]
        return return_value


# lista_prueba = Lista()

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

# lista_prueba.barrido()
# print()
# print(lista_prueba.search(4))

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
