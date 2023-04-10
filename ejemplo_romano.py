
#! I = 1, V = 5, X = 10, L = 50

#! Diccionarios (clave --> valor)

romano = {'i': 1, 'v': 5, 'x': 10, 'l': 50}

numero = 'iii'
numero = 'lxxxiv'

def convert_romano_to_dec(numero_romano):
    if len(numero_romano) == 1:
        return romano[numero_romano]
    else:
        if romano[numero_romano[0]] >= romano[numero_romano[1]]:
            return romano[numero_romano[0]] + convert_romano_to_dec(numero_romano[1:])
        else:
            return - romano[numero_romano[0]] + convert_romano_to_dec(numero_romano[1:])

print(convert_romano_to_dec(numero))


# dic = {'clave1': 123, 'clave2': 456, 3: 123}

# dic2 = {1: 56, 2: 12, 3: 4}

# print(type(dic))
# print(dic.get('clave3'))
# print(dic.pop('clave12', None))
# print(dic.update(dic2))

# dic['nueva'] = 'nuevo_valor'

# dic['clave2'] = 12345678

# del dic['nueva']

# print(dic)


# print('ciclo for')
# for key in dic.keys():
#     print(key, dic[key])