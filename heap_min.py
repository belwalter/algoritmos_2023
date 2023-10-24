

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
        while index > 0 and self.vector[index] < self.vector[(index-1)//2]:
            padre = (index-1)//2
            self.vector[index], self.vector[padre] = self.vector[padre], self.vector[index]
            index = padre

    def hundir(self, index):
        hijo_izq = (index*2) + 1
        control = True
        while control and hijo_izq < len(self.vector):
            hijo_der = hijo_izq + 1
            menor = hijo_izq
            if hijo_der < len(self.vector):
                if self.vector[hijo_der] < self.vector[hijo_izq]:
                    menor = hijo_der

            if self.vector[index] > self.vector[menor]:
                self.vector[index], self.vector[menor] = self.vector[menor], self.vector[index]
                index = menor
                hijo_izq = (index*2) + 1
            else:
                control = False


    def size(self):
        return len(self.vector)

    def montculizar(self):
        for i in range(len(self.vector)):
            self.flotar(i)

    def change_priority(self, pos, new_priority):
        if pos < self.size():
            old_priority = self.vector[pos][0]
            self.vector[pos][0] = new_priority
            if new_priority > old_priority:
                self.hundir(pos)
            else:
                self.flotar(pos)

    def search(self, value):
        for index, vector in enumerate(self.vector):
            if vector[1][0] == value:
                return index
    
    def arrive(self, value, priority, anterior=None):
        self.add_element([priority, value, anterior])

    def atention(self):
        return self.remove_element()


# cola = Heap()
# from random import randint

# for i in range(10):
#     prioridad = randint(1, 3)
#     numero = randint(1, 10)
#     cola.arrive(numero, prioridad)

# print(cola.vector)
# print()
# while cola.size() > 0:
#     print(cola.atention())

