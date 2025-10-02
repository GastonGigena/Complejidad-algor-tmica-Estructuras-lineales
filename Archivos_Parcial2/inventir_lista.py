def invertir_lista_con_pila(lista_original):

    pila = []
    lista_invertida = []

    for elemento in lista_original:
        pila.append(elemento)

    while pila:
        lista_invertida.append(pila.pop())

    return lista_invertida


mi_lista = [1, 2, 3, 4, 5]
lista_invertida = invertir_lista_con_pila(mi_lista)
print(f"Lista original: {mi_lista}")
print(f"Lista invertida: {lista_invertida}")
