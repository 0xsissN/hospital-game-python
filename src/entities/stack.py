class Stack:
    def __init__(self):
        self.x = []
    
    def push(self, n):
        self.x.append(n)

    def pop(self):
        return self.x.pop()
    
    def Len(self):
        return len(self.x) == 0