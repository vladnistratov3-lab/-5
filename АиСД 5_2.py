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
            current_node = self.root
            while True:
                if key < current_node.data:
                    if current_node.left is None:
                        current_node.left = Node(key)
                        break
                    current_node = current_node.left
                elif key > current_node.data:
                    if current_node.right is None:
                        current_node.right = Node(key)
                        break
                    current_node = current_node.right
                else:
                    break

    def height(self):
        def height_recursive(node):
            if node is None:
                return 0
            return 1 + max(height_recursive(node.left), height_recursive(node.right))

        return height_recursive(self.root)
bst = BinarySearchTree()
numbers = input().split()

for el in numbers:
    if el != "0":
        bst.insert(int(el))
    else:
        break

print(bst.height())