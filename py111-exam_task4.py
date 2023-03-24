def dna(dna: list) -> str:

    len_ = len(dna[0])
    d = {i: {} for i in range(len_)}
    for elem in dna:
        for i in range(len_):
            if elem[i] in d[i]:
                d[i][elem[i]] += 1
            else:
                d[i][elem[i]] = 0
    result = ''
    for small_dict in d:
        result += small_dict.items().sort(key=lambda x: x[1])[0][0]
    return result


# if __name__ == '__main__':
#     DNA_read(["ACTA", "ACTA", "ATTA"])
