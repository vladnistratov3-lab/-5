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

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def is_balanced(self, node):
        if node is None:
            return True

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        if abs(left_height - right_height) <= 1 and \
                self.is_balanced(node.left) and \
                self.is_balanced(node.right):
            return True

        return False

bst = BinarySearchTree()
numbers = list(map(int, input().split()))

for number in numbers:
    if number == 0:
        break
    bst.insert(number)

if bst.is_balanced(bst.root):
    print("YES")
else:
    print("NO")