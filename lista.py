

class Lista():

    def __init__(self):
        self.elements = []

    def insertr(self, value):
        if len(self.elements) == 0:
            self.elements.append(value)
        elif value < self.elements[0]:
            self.elements.insert(0, value)
        elif value >= self.elements[-1]:
            self.elements.append(value)
        else:
            index = 1
            while value >= self.elements[index]:
                index += 1
            self.elements.insert(index, value)

    def search(self, search_value):
        position = None
        for index, value in enumerate(self.elements):
            if search_value == value:
                position = index
                break
        return position

    def delete(self, value):
        return_value = None
        pos = self.search(value)
        if pos:
            return_value = self.elements.pop(pos)
        return return_value

    def size(self):
        return len(self.elements)

    def barrido(self):
        for value in self.elements:
            print(value)

    def get_element_by_value(self, value):
        return_value = None
        pos = self.search(value)
        if pos:
            return_value = self.elements[pos]
        return return_value

    def get_element_by_index(self, index):
        return_value = None
        if index >= 0 and index < self.size():
            return_value = self.elements[index]
        return return_value


lista_prueba = Lista()

lista_prueba.insertr(5)
print(lista_prueba.elements)
lista_prueba.insertr(3)
print(lista_prueba.elements)
lista_prueba.insertr(1)
print(lista_prueba.elements)
lista_prueba.insertr(7)
print(lista_prueba.elements)
lista_prueba.insertr(4)
print(lista_prueba.elements)
lista_prueba.insertr(6)
print(lista_prueba.elements)
lista_prueba.insertr(2)
print(lista_prueba.elements)
lista_prueba.insertr(3)
print(lista_prueba.elements)
lista_prueba.insertr(7)
print(lista_prueba.elements)
lista_prueba.insertr(1)
print(lista_prueba.elements)

print(lista_prueba.search(4))

print(lista_prueba.delete(10))
print(lista_prueba.elements)
# print(lista_prueba.delete(4))
# print(lista_prueba.elements)
print(lista_prueba.delete(3))
print(lista_prueba.elements)


lista_prueba.barrido()

print(lista_prueba.get_element_by_value(4))
print(lista_prueba.get_element_by_value(10))

print(lista_prueba.get_element_by_index(4))
print(lista_prueba.get_element_by_index(100))

# lista_value = ['a', 'h', 'z', 'd', 'f']

# for index, value in enumerate(lista_value):
#     if value == 'c':
#         print(f'lo encontre en la posicion {index}')
#     print(index, value)
