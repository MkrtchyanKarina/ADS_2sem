def refill(all_distance: int, max_dist_without_ref: int, stops_count: int, stops_places: list[int]):
    if stops_count == 0 and max_dist_without_ref < all_distance:
        return -1

    stops_places += [all_distance]
    last_stop = 0
    stops = 0

    for i in range(stops_count):  # сложность = O(n), где n - число заправок (stops_count)
        if stops_places[i+1] - last_stop > max_dist_without_ref:  # не можем пропустить ближайшую заправку
            if stops_places[i] - last_stop <= max_dist_without_ref:  # можем ли доехать до нее
                stops += 1
                last_stop = stops_places[i]  # новое начало отсчета
            else:
                return -1
    return stops


if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    s = list(map(int, input().split(' ')))
    print(refill(d, m, n, s))