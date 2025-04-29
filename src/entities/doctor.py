from entities.queue import Cola

class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.pacientes = Cola()

    def atenderPaciente(self):
        if self.pacientes.estaVacia():
            print(f"{self.nombre} no tiene pacientes en espera")
            return None

        paciente = self.pacientes.desencolar()
        print(f"\n{self.nombre} atendiendo a {paciente.nombre}")

        if paciente.historialMedico:
            print(f"Historial previo: {paciente.obtenerUltimoDiagnostico()}")

        receta = self.generarReceta(paciente)
        paciente.recetario.append(receta)

        consulta = {
            'doctor': self.nombre,
            'especialidad': self.especialidad,
            'sintomas': paciente.sintomas,
            'diagnostico': receta,
            'tratamiento': receta
        }
        paciente.agregarConsultaHistorial(consulta)

        print(f"Receta: {receta}")
        return paciente

    def generarReceta(self, paciente):
        if paciente.historialMedico:
            return f"Medicina para {self.especialidad} (ajustada)"
        return f"Medicina para {self.especialidad}"
