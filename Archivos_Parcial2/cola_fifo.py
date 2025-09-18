class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0, item)  # se agrega al final de la cola

    def avanzar(self):
        return self.items.pop()     # se quita el primero que entró

    def tamano(self):
        return len(self.items)
    
    
c = Cola()
c.agregar("A")
c.agregar("B")
c.agregar("C")
print(c.items)       # ['C', 'B', 'A']
print(c.avanzar())   # A (primero en entrar, primero en salir)
print(c.items)       # ['C', 'B']

