

#! 5! = 5 * 4 * 3 * 2 * 1 = 120
#! 5! = 5 * 4!

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



print('recursivo', factorialr(5))
print('iterativo', factoriali(5))
