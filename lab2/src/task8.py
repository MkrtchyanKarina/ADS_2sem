#  Задание №8 - Высота дерева
from collections import deque


def calculate_height(count, nodes):
    if len(nodes) > count or len(nodes) == 0:
        return 0

    queue = deque([0])
    height = 0

    while queue:
        height += 1
        level_size = len(queue)

        for _ in range(level_size):
            node_index = queue.popleft()
            _, left, right = nodes[node_index]

            if left != 0:
                queue.append(left - 1)
            if right != 0:
                queue.append(right - 1)

    return height

if __name__ == '__main__':
    c = 6
    n = [(-2, 0, 2), (8, 4, 3), (9, 0, 0), (3, 6, 5), (6, 0, 0), (0, 0, 0)]
    print(calculate_height(c, n))