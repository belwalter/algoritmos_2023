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


arbol = BinaryTree()

print(arbol.root)
arbol.insert_node('H')
arbol.insert_node('M')
arbol.insert_node('D')
arbol.insert_node('R')
arbol.insert_node('L')
arbol.insert_node('P')
arbol.insert_node('Q')
arbol.insert_node('F')
arbol.insert_node('A')

# arbol.preorden()
print()
pos = arbol.search('Z')
print(pos)
if pos:
    print('valor encontrado', pos.value)
