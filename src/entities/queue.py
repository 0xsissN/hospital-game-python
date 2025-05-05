class Queue:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.insert(0, element)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0
