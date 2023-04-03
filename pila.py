

class Pila():
    """Stack class"""

    def __init__(self):
        self.__elements = []

    def push(self, dato):
        self.__elements.append(dato)

    def pop(self):
        if self.size() > 0:
            dato = self.__elements.pop()
            return dato

    def size(self):
        return len(self.__elements)

    def on_top(self):
        if self.size() > 0:
            return self.__elements[-1]


pila_1 = Pila()
pila_aux = Pila()
pila_1.push(3)
pila_1.push(6)
pila_1.push(1)


print(f'la pila tiene {pila_1.size()} elementos')

print('barrido')

while pila_1.size() > 0:
    dato = pila_1.pop()
    print(dato)
    pila_aux.push(dato)

while pila_aux.size() > 0:
    dato = pila_aux.pop()
    pila_1.push(dato)

print('tamanio', pila_1.size(), pila_aux.size())


