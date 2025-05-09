def naive_string_search(p, t):  # p - подстрока, t - строка
    len_p = len(p)
    len_t = len(t)
    if len_p == 0:
        return 0, []
    result = []
    for i in range(len_t - len_p + 1):
        if t[i:i + len_p] == p:
            result.append(i + 1)
    return len(result), result

if __name__ == "__main__":
    print(naive_string_search("aba", "abaCaba"))

"""
1) При несовпадении шаблона с частью строки алгоритм продолжает проверку со следующей позиции в строке
2) Повторяющиеся символы не повлияют на работу алгоритма, просто увеличится число вхождений подстроки
3) В крайних случаях алгоритм возвращает 0 и пустой список, дополнительно понадобилось добавить только обработку случая с нулевой длиной подстроки 
"""