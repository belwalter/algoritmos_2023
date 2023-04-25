from lista import Lista
from random import randint


lista_valores = Lista()


# #! carga
for i in range(30):
    lista_valores.insert(chr(randint(65, 90)))


vocales = ['A', 'E', 'I', 'O', 'U']

lista_valores.barrido()
print()
contador = 0
while contador < lista_valores.size():
    value = lista_valores.get_element_by_index(contador)
    if value in vocales:
        print(lista_valores.delete(value))
    else:
        contador += 1


print()
lista_valores.barrido()