def intersection_of_segments(seg_count: int, segments: list[tuple]):

    segments = [(segments[i][0], -segments[i][1]) for i in range(seg_count)]
    segments = sorted(segments)
    dots = []

    current_start, current_end = segments[0][0], -segments[0][1]
    for j in range(1, seg_count):
        segment = segments[j]
        start, end = segment[0], -segment[1]
        if current_start <= start <= current_end:
            current_start = start
            current_end = min(current_end, end)
        else:
            dots += [current_start]
            current_start = start
            current_end = end

    dots += [current_start]

    return len(dots), dots


if __name__ == "__main__":
    n = int(input())
    s = []
    for _ in range(n):
        a, b = tuple(map(int, input().split(' ')))
        s += [(a, -b)]
    l, d = intersection_of_segments(n, s)
    print(l)
    print(*d)