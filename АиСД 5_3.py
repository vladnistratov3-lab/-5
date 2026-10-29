class Node:
    __slots__ = ('data', 'left', 'right')  # Ускоряет доступ к атрибутам

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self._count = 0  # Счётчик элементов

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            self._count += 1
            return

        current = self.root
        while current:
            if key < current.data:
                if current.left is None:
                    current.left = Node(key)
                    self._count += 1
                    return
                current = current.left
            elif key > current.data:
                if current.right is None:
                    current.right = Node(key)
                    self._count += 1
                    return
                current = current.right
            else:
                # Элемент уже существует
                return

    def size(self):
        return self._count


if __name__ == "__main__":
    import sys

    bst = BinarySearchTree()

    # Чтение из stdin работает быстрее
    data = sys.stdin.read().split()

    for num_str in data:
        num = int(num_str)
        if num == 0:
            break
        bst.insert(num)

    print(bst.size())