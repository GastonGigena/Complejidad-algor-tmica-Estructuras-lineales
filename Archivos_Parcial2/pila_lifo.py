class Pila:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)  # se agrega al final (arriba)

    def desapilar(self):
        return self.items.pop()  # se quita el último (arriba)

    def tamano(self):
        return len(self.items)

p = Pila()
p.apilar(1)
p.apilar(2)
p.apilar(3)
print(p.items)       # [1, 2, 3]
print(p.desapilar()) # 3 (último en entrar, primero en salir)
print(p.items)       # [1, 2]
