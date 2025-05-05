from .doctor import Doctor
from .tree import Node
from .stack import Stack

class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = {
            "PEDIATRIA": Doctor("Dr. Pepe", "PEDIATRIA"),
            "CARDIOLOGIA": Doctor("Dr. Kiko", "CARDIOLOGIA"),
            "NEUROLOGIA": Doctor("Dr. Goomba", "NEUROLOGIA"),
            "MEDICINA GENERAL": Doctor("Dr. Bowser", "MEDICINA GENERAL"),
            "DF": Doctor("Dr. df", "DF")
        }

    def assignedDoctor(self):
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
        e1 = Node("CARDIOLOGIA")
        e2 = Node("NEUROLOGIA")
        e3 = Node("MEDICINA GENERAL")

        r.child(l11)
        r.child(l12)
        l11.child(l21)
        l11.child(l22)
        l11.child(l23)
        l11.child(l24)
        l11.child(l25)
        l11.child(l35)
        l12.child(l23)
        l12.child(l24)
        l12.child(l25)
        l12.child(l35)
        l21.child(l31)
        l21.child(l32)
        l22.child(l31)
        l22.child(l32)
        l23.child(l33)
        l23.child(l34)
        l24.child(l33)
        l24.child(l34)
        l31.child(e1)
        l32.child(e1)
        l33.child(e2)
        l34.child(e2)
        l35.child(e3)
        l25.child(e3)
    
        a = Stack()
        vis = []

        for i in r.nodes:
            a.push(i.value)
    
        cd = 1

        dic = {
            "Sintomas": r,
            "Mareos": l11,
            "Nauseas": l12,
            "Dificultad para respirar": l21,
            "Dolor en el pecho": l22,
            "Dolor de cabeza": l23,
            "Debilidad o hormigueo": l24,
            "Dolor de cuerpo": l25,
            "Sudoracion fria": l31,
            "Palpitaciones": l32,
            "Perdida de conciencia": l33,
            "Vision borrosa": l34,
            "Tos persistente": l35,
            "CARDIOLOGIA": e1,
            "NEUROLOGIA": e2,
            "MEDICINA GENERAL": e3
        }

        dic2 = {
            1: ['Dificultad para respirar', 'Dolor en el pecho', 'Dolor de cabeza', 'Debilidad o hormigueo', 'Dolor de cuerpo', 'Tos persistente'],
            2: ['Sudoracion fria', 'Palpitaciones', 'Perdida de conciencia', 'Vision borrosa']
        }

        while True:
            x = a.pop()

            tx = dic[x]
    
            if len(tx.nodes) == 0:
                return self.doctors[tx.value]
    
            if tx.value not in vis:
                r = int(input(f"Sintoma: {tx.value}? 1. Si | 2. No: "))
                vis.append(tx.value)

            if r == 1:
                for i in tx.nodes:
                    if i.value not in vis:
                        a.push(i.value)

            if a.Len():
                if cd == 3:
                    return self.doctors["DF"] 
                    
                a.x = dic2[cd]
                cd += 1


