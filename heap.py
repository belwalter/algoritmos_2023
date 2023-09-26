

class Heap:

    def __init__(self):
        self.vector = []

    def add_element(self, value):
        self.vector.append(value)
        self.flotar(len(self.vector)-1)

    def remove_element(self):
        self.vector[0], self.vector[-1] = self.vector[-1], self.vector[0]
        value = self.vector.pop()
        self.hundir(0)
        return value

    def flotar(self, index):
        while index > 0 and self.vector[index] > self.vector[(index-1)//2]:
            padre = (index-1)//2
            self.vector[index], self.vector[padre] = self.vector[padre], self.vector[index]
            index = padre

    def hundir(self, index):
        hijo_izq = (index*2) + 1
        control = True
        while control and hijo_izq < len(self.vector):
            hijo_der = hijo_izq + 1
            mayor = hijo_izq
            if hijo_der < len(self.vector):
                if hijo_der > hijo_izq:
                    mayor = hijo_der

            if self.vector[index] < self.vector[mayor]:
                self.vector[index], self.vector[mayor] = self.vector[mayor], self.vector[index]
                index = mayor
                hijo_izq = (index*2) + 1
            else:
                control = False


    def size(self):
        return len(self.vector)

# #! obtener hijos
# print(vector[(pos*2) + 1], vector[(pos*2) + 2])

# #! obtener padre
# print(vector[(pos-1)//2])

heap = Heap()
from random import randint
for i in range(10):
    numero = randint(1, 50)
    heap.add_element(numero)

print(heap.vector)
heap.remove_element()
print(heap.vector)