"""
Как будет определяться временная и пространственная сложность алгоритма, и какие факторы будут влиять на эти оценки?

Алгоритм Беллмана-Форда имеет временную сложность O(V*E) и пространственную сложность O(V). 
"""


def bellman_ford(vertices_count: int, edges_count: int, data: list[tuple[int, int, int]], root: int) -> list:
    # Инициализация расстояний до всех вершин
    distances = [float('inf')] * (vertices_count + 1)
    distances[root] = 0  # Расстояние до начальной вершины равно 0

    # Основной цикл алгоритма Беллмана-Форда
    for _ in range(vertices_count - 1):
        for u, v, weight in data:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Проверка на наличие отрицательных циклов
    for u, v, weight in data:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            distances[v] = float('-inf')  # Устанавливаем значение для вершин в отрицательном цикле

    # Формирование результата
    result = []
    for i in range(1, vertices_count + 1):
        if distances[i] == float('-inf'):
            result.append("-")  # Отрицательный цикл
        elif distances[i] == float("inf"):
            result.append("*")  # Нет пути
        else:
            result.append(str(distances[i]))  # Кратчайшее расстояние

    return result


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
