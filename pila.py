

class Pila():
    """Stack class"""

    def __init__(self):
        self.__elements = []

    def __eq__(self, stack_aux):
        if isinstance(stack_aux, Pila):
            return self.__elements == stack_aux.__elements
        else:
            return False

    def push(self, value):
        self.__elements.append(value)

    def pop(self):
        if self.size() > 0:
            dato = self.__elements.pop()
            return dato

    def size(self):
        return len(self.__elements)

    def on_top(self):
        if self.size() > 0:
            return self.__elements[-1]

# class PeliculaMarvel():

#     def __init__(self, title, year):
#         self.__title = title
#         self.__year = year
    
#     def get_title(self):
#         return self.__title

#     def get_year(self):
#         return self.__year

#     def __str__(self):
#         return f'{self.__title} - {self.__year}'


# pelis = [
#     #! 1 dictionary 
#     # {'title': 'iron man', 'year': 2008},
#     # {'title': 'iron man', 'year': 2010},
#     # {'title': 'capitan america', 'year': 2011}
#     #? list
#     # ['iron man', 2008],
#     # ['iron man', 2010],
#     # ['capitan america', 2011]
#     #* class
#     PeliculaMarvel('iron man', 2008),
#     PeliculaMarvel('iron man', 2010),
#     PeliculaMarvel('capitan america', 2011),
# ]


# pila_1 = Pila()
# for peli in pelis:
#     pila_1.push(peli)

# while pila_1.size() > 0:
#     dato = pila_1.pop()
#     # print(dato.get_title(), dato.get_year())
#     if dato.get_year() == 2008:
#         print(dato.get_year(), 'se estreno en el 2008')

# pila_aux = Pila()
# pila_1.push(3)
# pila_1.push(6)
# pila_1.push(1)


# print(f'la pila tiene {pila_1.size()} elementos')

# print('barrido')

# while pila_1.size() > 0:
#     dato = pila_1.pop()
#     print(dato)
#     pila_aux.push(dato)

# while pila_aux.size() > 0:
#     dato = pila_aux.pop()
#     pila_1.push(dato)

# print('tamanio', pila_1.size(), pila_aux.size())

# #! crear las estucturas
# pila = Pila()
# pila_aux = Pila()

# #! carga
# from random import randint
# for i in range(10):
#     pila.push(randint(1, 100))

# #! resolver problema
# while pila.size() > 0:
#     valor = pila.pop()
#     if valor % 2 == 0:
#         # print('es par', valor)
#         pila_aux.push(valor)
#     # else:
#     #     print('es impar', valor)

# while pila_aux.size() > 0:
#     pila.push(pila_aux.pop())

# print(pila.size())