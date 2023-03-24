def del_man(N, K):
    list_of_man = [i for i in range(1, N + 1)]
    i = 0
    if N < 0:
        return None
    if N == 1:
        return N

    while N > K:
        i += -1
        if i >= N:
            i -= N
        list_of_man.pop(i)
        N -= 1

    while N > 1:
        i += K % N - 1
        if i >= N:
            i -= N
        list_of_man.pop(i)
        if i == -1:
            i = 0
        if i <= N:
            i = 0
        N -= 1

    return list_of_man


# if __name__ == '__main__':
#     del_man(10, 20)

