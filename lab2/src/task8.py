#  Задание №8 - Высота дерева
class Queue:
    def __init__(self):
        self.items = []
        self.head = 0

    def is_empty(self):
        return self.head >= len(self.items)

    def add(self, item):
        self.items.append(item)

    def get(self):
        if not self.is_empty():
            item = self.items[self.head]
            self.head += 1
            return item

    def size(self):
        return len(self.items) - self.head


def calculate_height(count, nodes):
    if len(nodes) != count or len(nodes) == 0:
        return 0

    queue = Queue()
    queue.add(0)
    height = 0

    while not queue.is_empty():
        height += 1
        level_size = queue.size()

        for _ in range(level_size):
            node_index = queue.get()
            _, left, right = nodes[node_index]

            if left != 0:
                queue.add(left - 1)
            if right != 0:
                queue.add(right - 1)

    return height


if __name__ == '__main__':
    c = 6
    n = [(-2, 0, 2), (8, 4, 3), (9, 0, 0), (3, 6, 5), (6, 0, 0), (0, 0, 0)]
    print(calculate_height(c, n))