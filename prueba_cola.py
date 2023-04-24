from cola import Cola
from pila import Pila
from random import randint


cola = Cola()

# #! carga
# for i in range(10):
#     value = chr(randint(65, 90))
#     print(value)
#     cola.arrive(value)

# #!  d, f, e, g, j, i, a
# print()
# cont = 0
# total = cola.size()
# while cont < total:
#     if cola.on_front() in ['A', 'E', 'I', 'O', 'U']:
#         cola.atention()
#     else:
#         cola.move_to_end()
#     cont += 1

# cont = 0
# while cont < cola.size():
#     value = cola.move_to_end()
#     print(value)
#     cont += 1

def es_primo(numero):
    contador = 0
    for i in range(2, numero):
        if numero % i == 0:
            contador += 1
            break
    return contador == 0


# #! carga
# for i in range(10):
#     cola.arrive(randint(0, 10))

# contador = 0
# cant_elementos = cola.size()
# while contador < cant_elementos:
#     if es_primo(cola.on_front()):
#         cola.move_to_end()
#     else:
#         cola.atention()
#     contador += 1

# contador = 0
# while contador < cola.size():
#     print(cola.on_front())
#     cola.move_to_end()
#     contador += 1

cola_aux = Cola()
plia_aux = Pila()
# for i in range(5):
#     plia_aux.push(randint(0, 50))

# while plia_aux.size() > 0:
#     # print(plia_aux.on_top())
#     cola_aux.arrive(plia_aux.pop())

# while cola_aux.size() > 0:
#     plia_aux.push(cola_aux.atention())

# print()
# while plia_aux.size() > 0:
#     print(plia_aux.pop())

# #! carga
# palabra = input('ingrese una palabra ')

# for letra in palabra:
#     plia_aux.push(letra)
#     cola_aux.arrive(letra)


# while plia_aux.size() > 0 and plia_aux.on_top() == cola_aux.on_front():
#     plia_aux.pop()
#     cola_aux.atention()

# if plia_aux.size() > 0:
#     print('no es palindromo')
# else:
#     print('es palindromo')

valores = [3, 5, 1, 4, 2]


for numero in valores:
    if cola_aux.size() == 0:
        cola_aux.arrive(numero)
    elif numero < cola_aux.on_front():
        cola_aux.arrive(numero)
        contador = 0
        while contador < cola_aux.size()-1:
            cola_aux.move_to_end()
            contador += 1
    else:
        pass


while cola_aux.size() > 0:
    print(cola_aux.atention())


  

# cola = [1, 2, 3, 4, 5, 7]
# cola_aux = []