def alice_and_apples(apples_count: int, start_height: int, apples_data: list[tuple]):

    apples_data = {num+1: (apples_data[num][0], -apples_data[num][1]) for num in range(apples_count)}
    apples_order = []

    apples_data = dict(sorted(apples_data.items(), key=lambda item: item[1]))

    for number in apples_data.keys():
        minus_height, plus_height = apples_data[number]
        if minus_height < start_height:
            start_height -= minus_height
            start_height -= plus_height
            apples_order += [number]
        else:
            return -1
    return ' '.join(map(str, apples_order))


if __name__ == "__main__":
    n, s = map(int, input().split(' '))
    m = []
    for i in range(n):
        a, b = map(int, input().split(' '))
        m += [(a, b)]
    print(alice_and_apples(n, s, m))