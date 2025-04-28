class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pacientes = []

        self.doctores = {
            "PEDIATRIA": Doctor("Dra. Ana", "PEDIATRIA"),
            "CARDIOLOGIA": Doctor("Dr. Luis", "CARDIOLOGIA"),
            "NEUROLOGIA": Doctor("Dra. Marta", "NEUROLOGIA"),
            "MEDICINA GENERAL": Doctor("Dr. José", "MEDICINA GENERAL")
        }

        self.sintomasEspecialidad = {
            "PEDIATRIA": ["fiebre", "tos", "gripe"],
            "CARDIOLOGIA": ["dolor pecho", "presión alta"],
            "NEUROLOGIA": ["mareo", "dolor cabeza", "temblores"],
            "MEDICINA GENERAL": ["dolor estómago", "resfriado", "malestar"]
        }

    def registrarPaciente(self, nombre, edad, sintomas, historial=None):
        paciente = Paciente(nombre, edad, sintomas, historial)
        self.pacientes.append(paciente)

        print(f"\nRegistro de {nombre}:")
        print(f"Síntomas: {', '.join(sintomas)}")
        if historial:
            print(f"Consultas previas: {len(historial)}")

        self.asignarDoctor(paciente)

    def asignarDoctor(self, paciente):
        asignado = False

        for especialidad, sintomas in self.sintomasEspecialidad.items():
            for sintoma in paciente.sintomas:
                if sintoma in sintomas:
                    doctor = self.doctores[especialidad]
                    doctor.pacientes.encolar(paciente)
                    paciente.doctoresAsignados.append(doctor.nombre)
                    print(
                        f"Asignado a {doctor.nombre} ({especialidad}) por {sintoma}")
                    asignado = True

        if not asignado:
            print("No se encontró especialidad adecuada")

    def atenderPacientes(self):
        print("\nIniciando consultas:")
        for doctor in self.doctores.values():
            while not doctor.pacientes.estaVacia():
                doctor.atenderPaciente()

    def enviarAFarmacia(self, farmacia):
        print("\nProceso en farmacia:")
        for paciente in self.pacientes:
            if paciente.recetario:
                dinero = int(
                    input(f"Dinero disponible para {paciente.nombre}: bs"))
                farmacia.procesarCompra(paciente, dinero)
