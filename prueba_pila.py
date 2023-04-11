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

# stack_letras = Pila()

# #! carga
# for i in range(10):
#     stack_letras.push(chr(randint(65, 90)))

# contador_vocales = 0
# while stack_letras.size() > 0:
#     valor = stack_letras.pop()
#     if valor in ['A', 'E', 'I', 'O', 'U']:
#         contador_vocales += 1

# print(f'la cantidad de vocales son {contador_vocales}')

# pila1 = Pila()
# pila2 = Pila()
# pila3 = Pila()


# palabra = input('ingrese un palabra ')
# for letra in palabra:
#     pila1.push(letra)

# while pila1.size() > 0:
#     valor = pila1.pop()
#     pila2.push(valor)
#     pila3.push(valor)

# while pila3.size() > 0:
#     pila1.push(pila3.pop())

# while pila1.size() > 0 and pila1.on_top() == pila2.on_top():
#     pila1.pop()
#     pila2.pop()

# if pila1.size() == 0:
#     print('es palindromo')
# else:
#     print('no es palindromo')

# if pila1 == pila2:
#     print('es palindromo')
# else:
#     print('no es palindromo')

