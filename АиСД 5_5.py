import sys


class Node:
    __slots__ = ('data', 'left', 'right')

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
            return

        current = self.root
        while True:
            if key < current.data:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            elif key > current.data:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right
            else:
                return  # элемент уже существует

    def order_up(self):
        result = []
        stack = []
        current = self.root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.data)
            current = current.right

        return result

data = sys.stdin.read().split()
bst = BinarySearchTree()

for num_str in data:
    num = int(num_str)
    if num == 0:
        break
    bst.insert(num)

sorted_elements = bst.order_up()
print("\n".join(map(str, sorted_elements)))