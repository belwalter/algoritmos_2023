from random import randint, choice
from lista import Lista


tabla_legion = [None] * 10
tabla_numero = [None] * 1000


def hash_numero(cadena):
    return int(cadena[-3:])

def bernstein(cadena, tabla):
    h = 0
    for caracter in cadena:
        h = (h * 33) + ord(caracter)
    return h % len(tabla)

legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']

for i in range(10):
    legion = choice(legiones)
    numero = randint(1100, 1110)
    codigo = f'{legion}-{numero}'
    posicion = bernstein(codigo[:2], tabla_legion)
    if tabla_legion[posicion] is None:
        tabla_legion[posicion] = Lista()
    tabla_legion[posicion].insert(codigo)
    posicion = hash_numero(codigo)
    print(codigo, posicion)
    if tabla_numero[posicion] is None:
        tabla_numero[posicion] = Lista()
    tabla_numero[posicion].insert(codigo)


# for index, lista in enumerate(tabla_legion):
#     if tabla_legion[index] is not None:
#         print('cantidad de elementos posicion', index, lista.size())
#         lista.barrido()
#         print()

for index, lista in enumerate(tabla_numero):
    if tabla_numero[index] is not None:
        print('cantidad de elementos posicion', index, lista.size())
        lista.barrido()
        print()