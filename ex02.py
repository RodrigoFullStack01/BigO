def somar_lista(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total


if __name__ == "__main__":
    valores = [1, 2, 3, 4, 5]
    print(somar_lista(valores))
