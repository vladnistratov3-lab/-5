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
                return

    def get_nodes_with_one_child(self):
        result = []
        stack = []
        current = self.root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            # Проверяем, есть ли только один потомок
            if (current.left is None and current.right is not None) or \
                    (current.left is not None and current.right is None):
                result.append(current.data)

            current = current.right

        return result
bst = BinarySearchTree()

# Быстрое чтение входных данных
data = sys.stdin.read().split()
numbers = []
for num in data:
    num_int = int(num)
    if num_int == 0:
        break
    numbers.append(num_int)

# Вставляем все числа
for num in numbers:
    bst.insert(num)

# Получаем и выводим вершины с одним потомком
single_child_nodes = bst.get_nodes_with_one_child()

# Быстрый вывод
sys.stdout.write('\n'.join(map(str, single_child_nodes)) + '\n')