def son_parentesis_balanceados(expresion):
    
    pila = []
    mapeo_cierre = {')': '(', ']': '[', '}': '{'}

    for caracter in expresion:
        if caracter in '([{':
            pila.append(caracter)
        elif caracter in ')]}':
            if not pila:
                return False       
            simbolo_apertura = pila.pop()
            
            if mapeo_cierre[caracter] != simbolo_apertura:
                return False

    return not pila


print(f'"{{[()]}}" es balanceado: {son_parentesis_balanceados("{[()]}")}')  # True
print(f'"{{[(])}}" es balanceado: {son_parentesis_balanceados("{[(])}")}')  # False
print(f'"(" es balanceado: {son_parentesis_balanceados("(")}')           # False
print(f'")(" es balanceado: {son_parentesis_balanceados(")(")}')         # False
print(f'"" es balanceado: {son_parentesis_balanceados("")}')             # True
