from arbol_binario import BinaryTree


arbol = BinaryTree()


datos = [
    {'name': 'Medusa', 'derrotado': 'Perseo'},
    {'name': 'Medusa2', 'derrotado': 'Zeus'},
    {'name': 'Tifon', 'derrotado': 'Zeus'},
    {'name': 'Leon Nimea', 'derrotado': 'Heracles'},
    {'name': 'Hydrade lerna', 'derrotado': 'Heracles'},
    {'name': 'Otro', 'derrotado': 'Heracles'},
    {'name': 'Ceto', 'derrotado': None},
    {'name': 'Tore de Creta', 'derrotado': None},
    {'name': 'Ceto2', 'derrotado': "Apolo"},
    {'name': 'Ceto3', 'derrotado': "Apolo"},

]

for criatura in datos:
    arbol.insert_node(criatura['name'], {'derrotado': criatura['derrotado']})

arbol.inorden_add_field()


dic_ranking = {}
arbol.inorden_ranking(dic_ranking)

print(dic_ranking)


def order_por(item):
    print(item)
    return item[1]

ordenados = list(dic_ranking.items())
ordenados.sort(key=order_por, reverse=True)
print(ordenados[:3])


pos = arbol.search()
if pos is not None:
    pos.other_values['capturado'] = 'Heracles'