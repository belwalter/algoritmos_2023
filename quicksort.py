data = [
    {'nombre': 'algo', 'edad': 22},
    {'nombre': 'algo', 'edad': 22},
    {'nombre': 'algo', 'edad': 22},
    {'nombre': 'algo', 'edad': 22},
    {'nombre': 'algo', 'edad': 22},
    {'nombre': 'algo', 'edad': 22},
    {'nombre': 'algo', 'edad': 22},
    {'nombre': 'algo', 'edad': 22},
    {'nombre': 'algo', 'edad': 22},
]

from pila import Pila

def cargar_carta(stack, carta):
    pila_aux = Pila()
    if stack.size() == 0 or stack.on_top() <= carta:
        print('apilar carta', carta)
        stack.push(carta)
    else:
        while stack.size() > 0 and stack.on_top() > carta:
            carta_aux = stack.pop()
            print('cambiar carta de maso temporalmente', carta_aux)
            pila_aux.push(carta_aux)
        stack.push(carta)
        while pila_aux.size() > 0:
            stack.push(pila_aux.pop())



cartas = [12, 5, 1, 10, 3, 7]

pila_principal = Pila()



# for carta in cartas:
#     cargar_carta(pila_principal, carta)
#     input()


# while pila_principal.size() > 0:
#     print(pila_principal.pop())

# class Persona():
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
    
#     def __str__(self):
#         return f'{self.nombre}, {self.edad}'


# for persona in data:
#     pila_aux.push(persona)
#     # pila_aux.push(Persona(persona['nombre'], persona['edad']))


# while pila_aux.size() > 0:
#     print(pila_aux.pop())



cartas = [12, 5, 1, 10, 3, 7]

cadena = "hola mundo"


print(cadena[:-1])