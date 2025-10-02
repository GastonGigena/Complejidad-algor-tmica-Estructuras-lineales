class Pila:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)  

    def desapilar(self):
        return self.items.pop()  

    def tamano(self):
        return len(self.items)

p = Pila()
p.apilar(1)
p.apilar(2)
p.apilar(3)
print(p.items)       
print(p.desapilar()) 
print(p.items)
