class Node:
    def __init__(self, value):
        self.value = value
        self.nodes = []

    def addChild(self, node):
        self.nodes.append(node)
    
        