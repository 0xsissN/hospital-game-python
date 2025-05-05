class Pharmacy:
    def __init__(self):
        self.prices = {
            "Medicina para PEDIATRIA": 10,
            "Medicina para CARDIOLOGIA": 20,
            "Medicina para NEUROLOGIA": 25,
            "Medicina para MEDICINA GENERAL": 15,
            "Medicina para PEDIATRIA (ajustada)": 15,
            "Medicina para CARDIOLOGIA (ajustada)": 25,
            "Medicina para NEUROLOGIA (ajustada)": 30,
            "Medicina para MEDICINA GENERAL (ajustada)": 20
        }

    def processPurchase(self, patient):
        if len(patient.recipeBook) == 0:
            print("Usted no cuenta con un recetario")
            return
        
        total = sum(self.prices.get(i, 0) for i in patient.recipeBook)

        print(f"\nFactura para {patient.name}:")
        for i in patient.recipeBook:
            print(f"- {i}: ${self.prices.get(i, 0)}")

        print(f"\nTotal: ${total}")
        print(f"Pago: ${patient.money}")

        if patient.money >= total:
            print("Compra exitosa")
            return
    
        print(f"Faltan ${total - patient.money}")
    
