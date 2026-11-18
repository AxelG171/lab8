def binary_search(lista: list, objetivo: int) -> int:
    """
    Input:
        lista: list de ints ordenada de menor a mayor
        objetivo: int a buscar
    Output:
        int: índice de objetivo en lista, o -1 si no existe
    """
    left = 0
    right = len(lista) - 1

    while left <= right:
        medio = (left + right) // 2
        # Tu codigo empieza aquí. Recuerda eliminar el `pass`
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            left = medio + 1
        else:
            right = medio - 1

    return -1


def esta_en_lista(lista: list, objetivo: int) -> str:
    """
    Input:
        lista: list de ints ordenada de menor a mayor
        objetivo: int a buscar
    Output:
        str: "Puntaje X encontrado en posición Y" o "Puntaje X no encontrado"
    """
    # Tu codigo empieza aquí. Recuerda eliminar el `pass`
    
    posicion = binary_search(lista, objetivo)
    if posicion != -1:
        return f"Puntaje {objetivo} encontrado en posición {posicion}"
    else:
        return f"Puntaje {objetivo} no encontrado"


if __name__ == "__main__":
    puntajes = [10, 25, 33, 47, 58, 61, 74, 89]   

    # print(binary_search(puntajes, 47))   # → 3
    # print(binary_search(puntajes, 50))   # → -1

    # print(esta_en_lista(puntajes, 61))   # → "Puntaje 61 encontrado en posición 5"
    # print(esta_en_lista(puntajes, 99))   # → "Puntaje 99 no encontrado"
