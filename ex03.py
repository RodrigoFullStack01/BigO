def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        valor = lista[meio]

        if valor == alvo:
            return meio
        if valor < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1


if __name__ == "__main__":
    ordenada = [1, 3, 5, 7, 9, 11]
    print(busca_binaria(ordenada, 7))
