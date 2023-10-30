from cola import Cola


class BinaryTree:

    class __Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert_node(self, value):
        def __insert(root, value):
            if root is None:
                return BinaryTree.__Node(value)
            elif value < root.value:
                root.left = __insert(root.left, value)
            else:
                root.right = __insert(root.right, value)

            return root

        self.root = __insert(self.root, value)
        # balancear(arbol)
        # actualizar_altura(arbol)

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value)
                __preorden(root.left)
                __preorden(root.right)

        if self.root is not None:
            __preorden(self.root)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        if self.root is not None:
            __inorden(self.root)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        if(self.root is not None):
            __postorden(self.root)

    def by_level(self):
        pendings = Cola()
        pendings.arrive(self.root)
        while not pendings.size == 0:
            node = pendings.atention()
            if node:
                print(node.value, node.left.value if node.left else None, node.right.value if node.right else None)
                if node.left:
                    pendings.arrive(node.left)
                if node.right:
                    pendings.arrive(node.right)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)
        aux = None
        if self.root is not None:
            aux = __search(self.root, key)
        return aux

    def delete_node(self, key):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, key):
            if root is not None:
                if key < root.value:
                    root.left, value = __delete(root.left, key)
                elif key > root.value:
                    root.right, value = __delete(root.right, key)
                else:
                    value = root.value
                    if root.left is None and root.right is not None:
                        return root.right, value
                    elif root.right is None and root.left is not None:
                        return root.left, value
                    elif root.left is None and root.right is None:
                        return None, value
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        return root, value
            return root, value
        deleted_value = None
        if self.root is not None:
            self.root, deleted_value = __delete(self.root, key)
            # actualizar_altura(arbol)
            # balancear(arbol)
        return deleted_value

# def altura(arbol):height
#     if arbol is None:
#         return -1
#     else:
#         return arbol['altura']

# def actualizar_altura(arbol):
#     if arbol is not None:
#         alt_izq = altura(arbol['izq'])
#         alt_der = altura(arbol['der'])
#         arbol['altura'] = (alt_izq if alt_izq > alt_der else alt_der) + 1

# def rotar_simple(arbol, control):
#     aux = nodoArbol()
#     if control:
#         copiar_nodo(arbol['izq'], aux)
#         arbol['izq'] = None
#         if(aux['der'] and not arbol['izq']):
#             arbol['izq'] = nodoArbol()
#         copiar_nodo(aux['der'], arbol['izq'])
#         aux['der'] = nodoArbol()
#         copiar_nodo(arbol, aux['der'])
#     else:
#         copiar_nodo(arbol['der'], aux)
#         arbol['der'] = None
#         if(aux['izq'] and not arbol['der']):
#             arbol['der'] = nodoArbol()
#         copiar_nodo(aux['izq'], arbol['der'])
#         aux['izq'] = nodoArbol()
#         copiar_nodo(arbol, aux['izq'])
#     arbol.update(aux)
#     actualizar_altura(aux['izq'])
#     actualizar_altura(aux['der'])
#     actualizar_altura(aux)

# def rotar_doble(arbol, control):
#     if control:
#         rotar_simple(arbol['izq'], False)
#         rotar_simple(arbol, True)
#     else:
#         rotar_simple(arbol['der'], True)
#         rotar_simple(arbol, False)

# def balancear(arbol):
#     if arbol is not None:
#         if altura(arbol['izq']) - altura(arbol['der']) == 2:
#             if(altura(arbol['izq']['izq']) >= altura(arbol['izq']['der'])):
#                 rotar_simple(arbol, True)
#             else:
#                 rotar_doble(arbol, True)
#         elif altura(arbol['der']) - altura(arbol['izq']) == 2:
#             if(altura(arbol['der']['der']) >= altura(arbol['der']['izq'])):
#                 rotar_simple(arbol, False)
#             else:
#                 rotar_doble(arbol, False)



arbol = BinaryTree()

arbol.insert_node(1)
arbol.insert_node(2)
arbol.insert_node(3)
arbol.insert_node(0)
arbol.insert_node(1)
arbol.insert_node(1)
arbol.insert_node(4)
arbol.insert_node(-1)
arbol.preorden()
# print()
# arbol.inorden()
# print()
# arbol.postorden()
# print()
# arbol.by_level()
# print()
# node = arbol.search(30)
# if node:
#     print('encontrado', node.value)
print()
print('eliminado', arbol.delete_node(1))
print()
arbol.preorden()
# print()
# print('eliminado', arbol.delete_node(4))
# print()
# arbol.preorden()