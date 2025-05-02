class Farmacia:
    def __init__(self):
        self.precios = {
            "Medicina para PEDIATRIA": 10,
            "Medicina para CARDIOLOGIA": 20,
            "Medicina para NEUROLOGIA": 25,
            "Medicina para MEDICINA GENERAL": 15,
            "Medicina para PEDIATRIA (ajustada)": 15,
            "Medicina para CARDIOLOGIA (ajustada)": 25,
            "Medicina para NEUROLOGIA (ajustada)": 30,
            "Medicina para MEDICINA GENERAL (ajustada)": 20
        }

    def procesarCompra(self, paciente):
        if len(paciente.recetario) == 0:
            print("Usted no cuenta con un recetario")
            return
        
        total = sum(self.precios.get(receta, 0)
                    for receta in paciente.recetario)

        print(f"\nFactura para {paciente.nombre}:")
        for receta in paciente.recetario:
            print(f"- {receta}: ${self.precios.get(receta, 0)}")

        print(f"\nTotal: ${total}")
        print(f"Pago: ${paciente.dinero}")

        if paciente.dinero >= total:
            print("Compra exitosa")
            return True

        print(f"Faltan ${total - paciente.dinero}")
        return False
