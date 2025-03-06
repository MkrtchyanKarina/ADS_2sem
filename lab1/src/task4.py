# Сбор подписей
def intersection_of_segments(seg_count: int, segments: list[tuple]):
    segments = [(segments[i][0], segments[i][1]) for i in range(seg_count)]
    segments = sorted(segments, key=lambda x: x[1])
    dots = []
    current_dot = float('-inf')

    for segment in segments:
        if segment[0] > current_dot:
            current_dot = segment[1]
            dots += [current_dot]

    return len(dots), dots

""" 
Сложность = O(n log(n))

Другие возможные решения, которые подходят так же для пересекающихся отрезков:
1) Представление отрезков в виде ребер графа, а концов - в виде вершин 
   (алгоритм построения минимального вершинного покрытия)
2) Дерево отрезков
3) Перебрать все точки от минимальной до максимальной координаты

Примеры использования алгоритма в реальной жизни:
1) Сбор подписей
2) Планирование доставки 
3) Организация мероприятий

Для отрицательных координат первоначальная точка будет минимальной, т.е. current_dot = float('-inf')
"""


if __name__ == "__main__":
    n = int(input())
    s = []
    for _ in range(n):
        a, b = tuple(map(int, input().split(' ')))
        s += [(a, -b)]
    l, d = intersection_of_segments(n, s)
    print(l)
    print(*d)