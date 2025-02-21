def refill(all_distance: int, max_dist_without_ref: int, stops_count: int, stops_places: list[int]):
    stops_places += [all_distance]
    last_stop = 0
    stops_res_count = 0

    for i in range(stops_count):
        if stops_places[i+1] - last_stop > max_dist_without_ref:
            if stops_places[i] - last_stop <= max_dist_without_ref:
                stops_res_count += 1
                last_stop = stops_places[i]
            else:
                return -1
    return stops_res_count


if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    s = list(map(int, input().split(' ')))
    print(refill(d, m, n, s))
