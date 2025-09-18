def son_parentesis_balanceados(expresion):
    pila = []
    mapeo_cierre = {')': '(', ']': '[', '}': '{'}

    for caracter in expresion:
        if caracter in '([{':
            pila.append(caracter)
        elif caracter in ')]}':
            if not pila: # Pila vacía
                return False
            # Extraer el último elemento de la pila
            simbolo_apertura = pila.pop()
            # Comprobar si coincide con el cierre
            if mapeo_cierre[caracter] != simbolo_apertura:
                return False

    # Al final, la pila debe estar vacía
    return not pila

# Ejemplos:
print(f'"{{[()]}}" es balanceado: {son_parentesis_balanceados("{[()]}")}')  # True
print(f'"{{[(])}}" es balanceado: {son_parentesis_balanceados("{[(])}")}')  # False
print(f'"(" es balanceado: {son_parentesis_balanceados("(")}')           # False
print(f'")(" es balanceado: {son_parentesis_balanceados(")(")}')         # False
print(f'"" es balanceado: {son_parentesis_balanceados("")}')             # True
