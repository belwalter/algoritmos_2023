from arbol_binario import BinaryTree


lista_heroes = [
    {'name': 'iron man', 'heroe': True},
    {'name': 'thanos', 'heroe': False},
    {'name': 'capitan america', 'heroe': True},
    {'name': 'red skull', 'heroe': False},
    {'name': 'hulk', 'heroe': True},
    {'name': 'black widow', 'heroe': True},
    {'name': 'rocket raccon', 'heroe': True},
    {'name': 'dotor strage', 'heroe': True},
    {'name': 'doctor octopus', 'heroe': True},
    {'name': 'deadpool', 'heroe': True},
]

arbol = BinaryTree()

for heroe in lista_heroes:
    arbol.insert_node(heroe['name'], heroe['heroe'])


arbol.inorden_super_or_villano(False)
print()
arbol.inorden_start_with('R')
print()
print('cantidad de superheroes', arbol.contar_heroes())
print()
arbol.search_by_coincidence('do')

value = input('ingrese el nombre que desea modificar ')
pos = arbol.search(value)
if pos:
    is_hero = pos.other_values
    arbol.delete_node(value)
    print('modificar')
    new_value = input('ingrese en nuevo nombre ')
    arbol.insert_node(new_value, is_hero)
else:
    print('no esta')
print()
arbol.inorden()
