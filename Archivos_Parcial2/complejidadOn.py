def contar_pares_O_n(lista_de_numeros):
    
    contador_pares = 0
    for numero in lista_de_numeros:
        if numero % 2 == 0:
            contador_pares += 1
    return contador_pares

mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50]
cantidad = contar_pares_O_n(mi_lista)
print(f"La lista original es: {mi_lista}")
print(f"Hay {cantidad} números pares en la lista.")
