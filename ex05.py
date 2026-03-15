def imprimir_elementos_e_pares(lista):
    for i in range(len(lista)):
        print(lista[i])

    for i in range(len(lista)):
        for j in range(len(lista)):
            print(lista[i], lista[j])


if __name__ == "__main__":
    valores = [1, 2, 3]
    imprimir_elementos_e_pares(valores)
