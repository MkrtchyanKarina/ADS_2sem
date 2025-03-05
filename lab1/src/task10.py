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

"""
1) Яблоко сначала уменьшает рост на ai, а затем увеличивает на bi
Какой порядок съедания яблок может привести к тому, что рост Алисы станет равным нулю?
Как можно определить, что Алиса не сможет съесть все яблоки, не потеряв рост?
Как можно визуализировать процесс съедания яблок и изменения роста Алисы?

2) Рост станет = 0, если Алиса начнет с яблок, которые сильно уменьшают рост (особенно, если 
они уменьшают рост сразу до нуля или отрицательного числа) и/или при этом дают небольшое увеличение

3) Нужно воспользоваться алгоритмом или просто сложить рост Алисы со всеми bi  вычесть все ai. 
Если результат окажется меньше 1, то такого порядка не найдется.

4) Процесс поедания яблок можно визуализировать с помощью ступенчатой или столбчатой диаграммы.
"""


if __name__ == "__main__":
    n, s = map(int, input().split(' '))
    m = []
    for i in range(n):
        a, b = map(int, input().split(' '))
        m += [(a, b)]
    print(alice_and_apples(n, s, m))