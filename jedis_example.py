from arbol_binario import BinaryTree, get_value_from_file

file_jedi = open('jedis.txt')
read_lines = file_jedi.readlines()
file_jedi.close()

name_tree = BinaryTree()
specie_tree = BinaryTree()
ranking_tree = BinaryTree()

read_lines.pop(0)
for index, linea_jedi in enumerate(read_lines):
    jedi = linea_jedi.split(';')
    jedi.pop() 
    name_tree.insert_node(jedi[0], index+2)
    specie_tree.insert_node(jedi[2], index+2)
    ranking_tree.insert_node(jedi[1], index+2)

# name_tree.inorden()
# print()
# ranking_tree.inorden_file('jedis.txt')
# print(get_value_from_file('jedis.txt', ))
# print()
# ranking_tree.by_level()
# print()
# specie_tree.by_level()

pos = name_tree.search('yoda1')
if pos:
    print(get_value_from_file('jedis.txt', pos.other_values))
else:
    print('no esta en la lista')

print()

# name_tree.inorden_file_lightsaber('jedis.txt', 'green')

name_tree.inorden_start_with_jedi('A')