#  Задание №8 - Высота дерева

class Node:
    """ Класс узла дерева """
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None


class BinaryTree:
    """Класс дерева с функцией нахождения высоты"""

    def __init__(self, count: int, nodes: list):

        self.count = count
        self.nodes = nodes
        self.parent = self.create_tree(1)

    def create_tree(self, index: int):
        key, left_child, right_child = self.nodes[index-1]
        parent = Node(key)
        if left_child != 0:
            parent.left_child = self.create_tree(left_child)
        if right_child != 0:
            parent.right_child = self.create_tree(right_child)
        return parent

    # def result_in_order(self, parent):
    #     if parent:
    #         self.result_in_order(parent.left_child)
    #         print(parent.key, end=" ")
    #         self.result_in_order(parent.right_child)
    #
    # def print_tree(self):
    #     self.result_in_order(self.parent)

    def height(self, node):
        if node is None:
            return 0
        else:
            return max(self.height(node.left_child), self.height(node.right_child)) + 1

    def print_height(self):
        print(self.height(self.parent))




if __name__ == '__main__':
    count = 6
    nodes = [(-2, 0, 2), (8, 4, 3), (9, 0, 0), (3, 6, 5), (6, 0, 0), (0, 0, 0)]
    tree = BinaryTree(count, nodes)
    tree.print_height()