class Paciente:
    def __init__(self, nombre, edad, dinero, sintomas, historialMedico=None):
        self.nombre = nombre
        self.edad = edad
        self.dinero = dinero
        self.sintomas = sintomas
        self.doctoresAsignados = []
        self.recetario = []
        if historialMedico is None:
            self.historialMedico = []
        else:
            self.historialMedico = historialMedico

    def agregarConsultaHistorial(self, consulta):
        self.historialMedico.append(consulta)

    def obtenerUltimoDiagnostico(self):
        if not self.historialMedico:
            return None
        return self.historialMedico[-1]['diagnostico']

    def datosPaciente(self):
        sintomasStr = ', '.join(self.sintomas)
        return f"Paciente: {self.nombre}, Edad: {self.edad}, Síntomas: {sintomasStr}"
