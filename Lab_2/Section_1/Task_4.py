# Diccionario original con calificaciones por materia
grades = {
    "Alicia": {"Matematicas": 85, "Ciencias": 92, "Español": 78},
    "Roberto": {"Matematicas": 75, "Ciencias": 68, "Español": 80},
    "Carlos": {"Matematicas": 95, "Ciencias": 88, "Español": 90}
}

# Crear un nuevo diccionario para guardar los promedios
averages = {}

# Recorrer cada estudiante y sus materias
for student, subjects in grades.items():
    # Tomar solo las calificaciones (los valores del subdiccionario)
    values = list(subjects.values())

    # Calcular el promedio usando sum() y len()
    average = sum(values) / len(values)

    # Guardar en el nuevo diccionario
    averages[student] = average

# Mostrar resultado
print("Promedios de los estudiantes:")
print(averages)
