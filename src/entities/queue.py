class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        self.elementos.insert(0, elemento)

    def desencolar(self):
        if self.estaVacia():
            return None
        return self.elementos.pop()

    def estaVacia(self):
        return len(self.elementos) == 0
