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


legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO', 'AY']

for i in range(2000):
    legion = choice(legiones)
    numero = randint(1000, 9999)
    codigo = f'{legion}-{numero}'
    posicion = bernstein(codigo[:2], tabla_legion)
    if tabla_legion[posicion] is None:
        tabla_legion[posicion] = Lista()
    tabla_legion[posicion].insert(codigo)
    posicion = hash_numero(codigo)
    if tabla_numero[posicion] is None:
        tabla_numero[posicion] = Lista()
    tabla_numero[posicion].insert(codigo)

posicion = bernstein('FN', tabla_legion)
if tabla_legion[posicion] is None:
    tabla_legion[posicion] = Lista()
tabla_legion[posicion].insert('FN-2187')
posicion = hash_numero('FN-2187')
if tabla_numero[posicion] is None:
    tabla_numero[posicion] = Lista()
tabla_numero[posicion].insert('FN-2187')
#! c.determinar si el Stormtrooper FN-2187 está cargado para poder quitarlo
#! porque es un traidor desertor.
#! d. ahora obtenga todos los Stormtrooper terminados en 781 para asignarlos a 
#! una misión de asalto y a los terminados en 537 para una misión de exploración;
#! e. ahora obtenga los Stormtrooper de la legión CT para que custodien a 
#! Darth Vader a una misión de exploración al planeta Hoth y los de la 
#! legión TF para una misión de exterminación a Endor

#! tabla_legion, tabla_numero

#! C
# pos = bernstein('FN', tabla_legion)
# if tabla_legion[pos] is not None:
#     lista = tabla_legion[pos]
#     trooper = lista.delete('FN-2187')
#     if trooper is not None:
#         print('El stormtrooper fue eliminado de la tabla legion')
#     else:
#         print('El stormtrooper no esta en la lista')
        
# pos = hash_numero('FN-2187')
# if tabla_numero[pos] is not None:
#     lista = tabla_numero[pos]
#     trooper = lista.delete('FN-2187')
#     if trooper is not None:
#         print('El stormtrooper fue eliminado de la tabla numero')
#     else:
#         print('El stormtrooper no esta en la lista')


#! D 781, 587
# pos = hash_numero('FN-2781')
# print('Troopers terminados en 781')
# if tabla_numero[pos] is not None:
#     lista = tabla_numero[pos]
#     lista.barrido()
# print()
# pos = hash_numero('FN-2587')
# print('Troopers terminados en 587')
# if tabla_numero[pos] is not None:
#     lista = tabla_numero[pos]
#     lista.barrido()

#! E TF CT
# pos = bernstein('CT', tabla_legion)
# print('Troopers terminados en CT')
# if tabla_legion[pos] is not None:
#     lista = tabla_legion[pos]
#     lista.barrido()
# print()
# pos = bernstein('TF', tabla_legion)
# print('Troopers terminados en TF')
# if tabla_legion[pos] is not None:
#     lista = tabla_legion[pos]
#     lista.barrido()



# for index, lista in enumerate(tabla_legion):
#     if tabla_legion[index] is not None:
#         print('cantidad de elementos posicion', index, lista.size())
#         lista.barrido()
#         print()

# for index, lista in enumerate(tabla_numero):
#     if tabla_numero[index] is not None:
#         print('cantidad de elementos posicion', index, lista.size())
#         lista.barrido()
#         print()
