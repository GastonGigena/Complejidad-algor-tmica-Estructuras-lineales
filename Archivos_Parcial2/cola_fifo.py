class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0, item)

    def avanzar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)
    
    
c = Cola()
c.agregar("A")
c.agregar("B")
c.agregar("C")
print(c.items)       
print(c.avanzar())   
print(c.items)

