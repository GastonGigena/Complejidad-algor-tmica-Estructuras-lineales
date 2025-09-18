def invertir_lista_con_pila(lista_original):
    """
    Invierte una lista utilizando una pila (implementada con una lista de Python).

    Args:
        lista_original: La lista que se desea invertir.

    Returns:
        Una nueva lista con los elementos de lista_original en orden inverso.
    """
    pila = []  # Inicializa una lista vacía que actuará como pila
    lista_invertida = [] # Lista para almacenar los elementos invertidos

    # 1. Apilar todos los elementos de la lista original
    for elemento in lista_original:
        pila.append(elemento) # Agrega el elemento a la cima de la pila

    # 2. Desapilar los elementos para crear la lista invertida
    while pila: # Mientras la pila no esté vacía
        lista_invertida.append(pila.pop()) # Extrae el último elemento y lo agrega a la lista invertida

    return lista_invertida

# Ejemplo de uso:
mi_lista = [1, 2, 3, 4, 5]
lista_invertida = invertir_lista_con_pila(mi_lista)
print(f"Lista original: {mi_lista}")
print(f"Lista invertida: {lista_invertida}")
