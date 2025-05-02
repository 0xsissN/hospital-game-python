from .doctor import Doctor
from .tree import Node

class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pacientes = []

        self.doctores = {
            "PEDIATRIA": Doctor("Dr. Pepe", "PEDIATRIA"),
            "CARDIOLOGIA": Doctor("Dr. Kiko", "CARDIOLOGIA"),
            "NEUROLOGIA": Doctor("Dr. Goomba", "NEUROLOGIA"),
            "MEDICINA GENERAL": Doctor("Dr. Bowser", "MEDICINA GENERAL")
        }

        self.sintomas = createTree()

    def asignarDoctor(self):
        asignado = False

def createTree():
    r = Node("Sintomas")
    l11 = Node("Mareos")
    l12 = Node("Nauseas")
    l21 = Node("Dificultad para respirar")
    l22 = Node("Dolor en el pecho")
    l23 = Node("Dolor de cabeza")
    l24 = Node("Debilidad o hormigueo")
    l25 = Node("Dolor de cuerpo")
    l31 = Node("Sudoracion fria")
    l32 = Node("Palpitaciones")
    l33 = Node("Perdida de conciencia")
    l34 = Node("Vision borrosa")
    l35 = Node("Tos persistente")
    e1 = Node("Cardiolodia")
    e2 = Node("Neurologia")
    e3 = Node("Medicina general")

    r.addChild(l11)
    r.addChild(l12)
    l11.addChild(l21)
    l11.addChild(l22)
    l11.addChild(l23)
    l11.addChild(l24)
    l11.addChild(l25)
    l11.addChild(l35)
    l12.addChild(l23)
    l12.addChild(l24)
    l12.addChild(l25)
    l12.addChild(l35)
    l21.addChild(l31)
    l21.addChild(l32)
    l22.addChild(l31)
    l22.addChild(l32)
    l23.addChild(l33)
    l23.addChild(l34)
    l24.addChild(l33)
    l24.addChild(l34)
    l31.addChild(e1)
    l32.addChild(e1)
    l33.addChild(e2)
    l34.addChild(e2)
    l35.addChild(e3)
    l25.addChild(e3)

    return r


