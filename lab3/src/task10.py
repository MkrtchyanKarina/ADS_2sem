class Queue:
    def __init__(self):
        self.items = []
        self.head = 0

    def is_empty(self):
        return self.head >= len(self.items)

    def add(self, item):
        self.items.extend(item)

    def get(self):
        if not self.is_empty():
            item = self.items[self.head]
            self.head += 1
            return item

    def size(self):
        return len(self.items) - self.head


def bellman_ford(vertices_count, edges_count, data, root):
    graph = {key: [] for key in range(1, vertices_count + 1)}
    for edge in range(edges_count):
        graph[data[edge][0]].append(data[edge])

    distances = [float('inf')] * (vertices_count + 1)
    distances1 = dijkstra_algorithm(graph.copy(), root, distances)
    distances2 = dijkstra_algorithm(graph.copy(), root, distances1.copy())

    distances_result = [""] * vertices_count
    for i in range(1, vertices_count + 1):
        if distances2[i] != distances1[i]:
            distances_result[i-1] = "-"
        else:
            distances_result[i-1] = "*" if distances1[i] == float("inf") else str(distances1[i])
    return distances_result



def dijkstra_algorithm(graph: dict, root, distances):
    queue = Queue()
    visited = set()

    queue.add(graph[root])
    visited.add(root)

    distances[root] = 0

    while not queue.is_empty():
        for i in range(queue.size()):
            edge = queue.get()
            start, end, weight = edge
            distances[end] = min(distances[end], weight+distances[start])
            if end not in visited:
                queue.add(graph[end])
                visited.add(end)
    return distances



if __name__ == "__main__":
    v, e = 6, 7
    d = [(1, 2, 10), (2, 3, 5), (1, 3, 100), (3, 5, 7), (5, 4, 10), (4, 3, -18), (6, 1, -1)]
    s = 1
    print("\n".join(bellman_ford(v, e, d, s)))
    print("--------------")
    v, e = 5, 4
    d = [(1, 2, 1), (4, 1, 2), (2, 3, 2), (3, 1, -5)]
    s = 4
    print("\n".join(bellman_ford(v, e, d, s)))
