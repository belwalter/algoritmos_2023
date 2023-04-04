from pila import Pila
from random import randint

# stack = Pila()
# stack_aux = Pila()

# #! carga
# for i in range(10):
#     valor = randint(0, 100)
#     print('valor generado', valor)
#     stack.push(valor)

# while stack.size() > 0:
#     valor = stack.pop()
#     if valor % 2 == 0:
#         stack_aux.push(valor)

# while stack_aux.size() > 0:
#     stack.push(stack_aux.pop())

# while stack.size() > 0:
#     print(stack.pop())

# stack_palabra = Pila()

# #! carga
# palabra = input('ingrese una palabra ')
# for i in palabra:
#     stack_palabra.push(i)

# palabra_invertida = ''
# while stack_palabra.size() > 0:
#     palabra_invertida += stack_palabra.pop()

# print(palabra_invertida)

stack_letras = Pila()

#! carga
for i in range(10):
    stack_letras.push(chr(randint(65, 90)))

contador_vocales = 0
while stack_letras.size() > 0:
    valor = stack_letras.pop()
    if valor in ['A', 'E', 'I', 'O', 'U']:
        contador_vocales += 1

print(f'la cantidad de vocales son {contador_vocales}')