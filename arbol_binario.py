class NodeTree():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert_node(self, value):

        def __insertar(root, value):
            if root is None:
                return NodeTree(value)
            elif value < root.value:
                root.left = __insertar(root.left, value)
            else:
                root.right = __insertar(root.right, value)
            return root

        self.root = __insertar(self.root, value)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        __inorden(self.root)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        __postorden(self.root)

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value)
                __preorden(root.left)
                __preorden(root.right)

        __preorden(self.root)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)

        return __search(self.root, key)

    def delete_node(self, key):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
            return root, replace_node

        def __delete(root, key):
            value = None
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

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, key)
        return delete_value


arbol = BinaryTree()

print(arbol.root)
arbol.insert_node('F')
arbol.insert_node('B')
# arbol.insert_node('E')
arbol.insert_node('K')
# arbol.insert_node('H')
# arbol.insert_node('J')
# arbol.insert_node('I')
# arbol.insert_node('R')

arbol.preorden()

print()
deleted = arbol.delete_node('F')
# if deleted:
#     print('el valor fue eliminado', deleted)
# print()
arbol.preorden()
deleted = arbol.delete_node('Z')
print()
arbol.preorden()
deleted = arbol.delete_node('K')
print()
arbol.preorden()


# print()
# pos = arbol.search('Z')
# print(pos)
# if pos:
#     print('valor encontrado', pos.value)
