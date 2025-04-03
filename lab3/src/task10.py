def bellman_ford(vertices_count: int, edges_count: int, data: list[tuple[int, int, int]], root: int) -> list:
    distances = [float('inf')] * (vertices_count + 1)
    distances[root] = 0

    for _ in range(vertices_count - 1):
        for v1, v2, weight in data:
            if distances[v1] != float('inf') and distances[v2] > distances[v1] + weight:
                distances[v2] = distances[v1] + weight

    for v1, v2, weight in data:
        if distances[v1] != float('inf') and distances[v2] > distances[v1] + weight:
            distances[v2] = float('-inf')

    # Формирование результата
    result = []
    for i in range(1, vertices_count + 1):
        if distances[i] == float('-inf'):
            result.append("-")
        elif distances[i] == float("inf"):
            result.append("*")
        else:
            result.append(str(distances[i]))

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
