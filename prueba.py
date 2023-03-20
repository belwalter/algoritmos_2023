
#!TIPOS DE DATOS int float str bool None
num = None

num1 = 12
num2 = 0.5
# print(type(num2))
# num2 = "Juan"
# print(type(num2))
# num2 = False
# print(type(num2))

#! OPERADORES ARITMETICOS + - * / // % **  ASIGNACION =

NUM = 0
num1 = 5
num2 = 2

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 // num2)
# print(num1 % num2)
# print(num2 ** num1)

#! FUNCION CCONVERSION int() str() float() bool()
# numero_1 = int(input('Ingrese un numero: '))
# numero_2 = int(input('Ingrese otro numero: '))
# print(numero_1 + numero_2)

#! CONDICIONAL if if-else if-anidados  if-elif-else
#! OPERADORES DE CONTROL > < >= <= == !=
#! OPERADORES LOGICOS AND OR ^ (XOR)
# num = 1
# if num > 10:
#     print('es mayor que 10')
# else:
#     if num == 10:
#         print('es igual')
#     else:
#         print('menor que 10')

# if num > 10:
#     print('es mayor que 10')
# elif num == 10:
#     print('es igual')
# else:
#     print('es igual')

# if num > 1 and num < 10:
#     print('algo')

# #! CICLOS  for while
# num = 1
# while num < 10:
#     print(num)
#     num += 1

# for i in range(1, 11):
#     print('indice', i)

#! ESTRUCTURAS DE DATOS  list dic
lista_num = [10, 2, -3, 10, None]
lista_num.append(0)
lista_num.append(50)
# lista_num.remove(10)
lista_num.insert(1, 11)
# lista_num.sort()
lista_num[3] = 6
print(lista_num[3])
print(lista_num, len(lista_num))
lista_num.pop(2)
# print(lista_num, len(lista_num))

lista_num.reverse()
for i in range(len(lista_num)):
    print('elemento en indice', i, lista_num[i])

#! FUNCIONES    

numero = 0 


def mi_funcion2():
    print('hola')

def mi_funcion(num1, lista):
    lista.pop()
    print('salida de la funcio', mi_funcion2())
    num1 = 45
    return lista


valores = [1, 2, 3, 4]
numero_1, msj, numero2 = mi_funcion(numero, valores) 
print(numero_1, msj, numero2)
print(valores)