def verificar_primeiro(lista):
    if len(lista) == 0:
        return None
    return lista[0]


if __name__ == "__main__":
    valores = [10, 20, 30]
    print(verificar_primeiro(valores))
