def produto_de_matrizes(a, b, n):
    c = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]

    return c


if __name__ == "__main__":
    a = [[1, 2], [3, 4]]
    b = [[2, 0], [1, 2]]
    c = produto_de_matrizes(a, b, 2)
    print(c)
