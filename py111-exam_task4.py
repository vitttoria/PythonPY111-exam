def DNA_read(roster: list) -> str:

    width = len(roster[0])
    d = {i: {} for i in range(width)}
    for elem in roster:
        for i in range(width):
            if elem[i] in d[i]:
                d[i][elem[i]] += 1
            else:
                d[i][elem[i]] = 0
    res = ''
    for small_dict in d:
        res += small_dict.items().sort(key=lambda x: x[1])[0][0]
    return res


# if __name__ == '__main__':
#     DNA_read(["ACTA", "ACTA", "ATTA"])
