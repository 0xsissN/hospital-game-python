from .queue import Queue

class Doctor:
    def __init__(self, name, speciality):
        self.name = name
        self.speciality = speciality
        self.patients = Queue()

    def assignedPatient(self, patient):
        self.patients.push(patient)

    def attendPatient(self):
        if self.patients.isEmpty():
            print(f"{self.name} no tiene pacientes en espera")
            return

        patient = self.patients.pop()
        print(f"\n{self.name} atendiendo a {patient.name}")

        recipe = "Medicina para " + self.speciality 
        patient.recipeBook.append(recipe)

        query = {
            'doctor': self.name,
            'especialidad': self.speciality,
            'diagnostico': recipe,
            'tratamiento': recipe
        }

        patient.medicalHistory.append(query)

        print(f"Receta: {recipe}")

