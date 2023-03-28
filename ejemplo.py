

#! 5! = 5 * 4 * 3 * 2 * 1 = 120
#! 5! = 5 * 4!
#! fac(n) = n * fac(n-1)

def factorialr(numero):
    """resuleve el factorial de un numero n de manera recursiva"""
    # print('valor devariable', numero)
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

# print('recursivo', factorialr(5))
# print('iterativo', factoriali(5))


#! fib(n) = fib(n-1) + fib(n-2)

def fibonacci(numero):
    if (numero == 0 or numero == 1):
        print('valor de retorno', numero)
        return numero
    else:
        print('llamada recursiva', numero)
        fib = fibonacci(numero-1) + fibonacci(numero-2)
        print(fib)
        return fib
        # return fibonacci(numero-1) + fibonacci(numero-2)


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
