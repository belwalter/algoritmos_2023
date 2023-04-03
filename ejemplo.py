

#! 5! = 5 * 4 * 3 * 2 * 1 = 120
#! 5! = 5 * 4!
#! fac(n) = n * fac(n-1)

def factorialr(numero):
    """resuleve el factorial de un numero n de manera recursiva"""
    if numero == 0:
        return 1
    else:
        return numero * factorialr(numero-1)



def factoriali(numero):
    """resuleve el factorial de un numero n de manera iterativo"""
    factorial = 1
    for i in range(1, numero+1):
        factorial = factorial * i
    return factorial

# print('iterativo', factoriali(150))
# print('recursivo', factorialr(150))

# a = input()


#! fib(n) = fib(n-1) + fib(n-2)

def fibonacciR(numero):
    if (numero == 0 or numero == 1):
        # print('valor de retorno', numero)
        return numero
    else:
        # print('llamada recursiva', numero)
        fib = fibonacciR(numero-1) + fibonacciR(numero-2)
        # print(fib)
        return fib
        # return fibonacci(numero-1) + fibonacci(numero-2)

def fibonacciI(numero):
    fib_0 = 0
    fib_1 = 1
    for i in range(2, numero+1):
        fibonacci = fib_0 + fib_1
        fib_0 = fib_1
        fib_1 = fibonacci
    return fibonacci


print(fibonacciI(100))
# print(fibonacciR(100))
a = input()

print('el valor en la succesion de fibonnacci es', fibonacci(3))

# 3 = 3 + 2 + 1

# suma(numero) = numero + suma(numero-1)

def suma(numero):
    if numero == 0:
        return numero
    else:
        return numero + suma(numero-1)

print(suma(4))

# 2 ^ 3 = 2 * 2 ^ 2

# potencia(base, exponente) = base * potencia(base, exponente -1)

def potencia(base, exponente):
    if exponente == 1:
        return base
    else:
        return base * potencia(base, exponente-1)

print(potencia(2, 5))

#! SLICING PARTICIONADO
# cadena = 'hola'
#     = 'a' + invertir('hol')
#     = 'a' + 'l' + invertir('ho')

#! invertir(cadena) = ultimo_caracter(cadena) + invertir(cadena-ultimo_caracter)

def invertir(cadena):
    if len(cadena) == 0:
        return ''
    else:
        return cadena[-1] + invertir(cadena[0:-1])

print(invertir('hola mundo'))

# producto(4, 3) = 4 + producto(4, 2) --> 2do valor = 0 retorna 0

# sumotoria(5) = 1/5 + sumatoria(5-1) --> numero = 1 retorna 1

# contar_digito(numero) = 1 + contra_dogito(numero//10) --> == 0 retorn 0


def invertir_numero(numero):
    if numero // 10 == 0:
        return numero
    else:
        return (numero % 10) * 10 ** len(str(numero//10)) + invertir_numero(numero//10)


print(invertir_numero(1253))

lista_valores = [1, 4, 7, 0, 2, 5, -3, 9]


def busqueda_secuencial(lista, buscado):
    if len(lista) == 0:
        return -1
    elif lista[-1] == buscado:
        return len(lista)-1
    else:
        return busqueda_secuencial(lista[0:-1], buscado)

print(busqueda_secuencial(lista_valores, 19))

lista_valores = [1, 4, 7, 10, 12]

def busqueda_binaria(lista, buscado, primero, ultimo):
    if primero > ultimo:
        return -1
    else:
        medio = (primero + ultimo) // 2
        if lista[medio] == buscado:
            return medio
        elif buscado > lista[medio]:
            return busqueda_binaria(lista, buscado, medio+1, ultimo)
        else:
            return busqueda_binaria(lista, buscado, primero, medio-1)


print(busqueda_binaria(lista_valores, 11, 0, len(lista_valores)-1))