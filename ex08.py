def ordenacao_bolha(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


if __name__ == "__main__":
    valores = [5, 1, 4, 2, 8]
    ordenacao_bolha(valores)
    print(valores)
