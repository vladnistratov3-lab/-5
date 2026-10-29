class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            current = self.root
            while True:
                if key < current.data:
                    if current.left is None:
                        current.left = Node(key)
                        break
                    current = current.left
                elif key > current.data:
                    if current.right is None:
                        current.right = Node(key)
                        break
                    current = current.right
                else:
                    break

    def find_nodes_with_two_children(self):
        result = []
        self._find_nodes_with_two_children(self.root, result)
        return sorted(result)

    def _find_nodes_with_two_children(self, node, result):
        if node is None:
            return
        if node.left is not None and node.right is not None:
            result.append(node.data)
        self._find_nodes_with_two_children(node.left, result)
        self._find_nodes_with_two_children(node.right, result)

bst = BinarySearchTree()
numbers = list(map(int, input().split()))
for number in numbers:
    if number == 0:
        break
    bst.insert(number)

nodes_with_two_children = bst.find_nodes_with_two_children()
for node in nodes_with_two_children:
    print(node)