from arbol_binario import BinaryTree
from random import randint

arbol = BinaryTree()

for i in range(30):
    arbol.insert_node(randint(0, 30))

#! A falta por nivel
print('inorden')
arbol.inorden()
# print()
# print('postorden')
# arbol.postorden()
# print()
# print('preorden')
# arbol.preorden()

#! B
# numero = int(input('ingrese un numero: '))
# pos = arbol.search(numero)
# if pos:
#     print(f'{numero} esta cargado en el arbol')

#! C
# for i in range(3):
#     numero = int(input('ingrese un numeropara eliminar: '))
#     deleted_value = arbol.delete_node(numero)
#     if deleted_value:
#         print('el valor fue eliminado', numero)
#     else:
#         print('el valor no se puede eliminar porque no esta')
# arbol.inorden()

#! D
numero = int(input('ingrese un numero para contar: '))
count = arbol.contar(numero)
print(count)