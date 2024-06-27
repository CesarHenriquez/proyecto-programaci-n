import random
#Funcion para agregar notas y evaluarlas 
def ingresarnotas():
    notas = []
    for i in range(8):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i + 1}: "))
                if 1.0 <= nota <= 7.0:  # Asumiendo que las notas en Chile van de 1.0 a 7.0
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 1.0 y 7.0")
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return notas

#Función para calcular el promedio de las notas
def calcular_promedio(notas):
    suma = sum(notas)
    promedio = suma / len(notas)
    return promedio

def generar_asistencia (num_asistencias):
    return [random.randint(1, 2) for _ in range(num_asistencias)]

def mostrar_asistencia(asistencias):
    print("Listado de Asistencia:")
    for i, asistencia in enumerate(asistencias, 1):
        estado = "Presente" if asistencia == 2 else "Ausente"
        print(f"Clase {i}: {estado}")
def evaluar_asistencia(asistencias):
    total_asistencias = len(asistencias)
    asistencias_presentes = asistencias.count(2)
    porcentaje_asistencia = (asistencias_presentes / total_asistencias) * 100
    print(f"\nPorcentaje de Asistencia: {porcentaje_asistencia:.2f}%")
    if porcentaje_asistencia == 100:
        print("El siguiente estudiante tiene asistencia perfecta, se le recompensara con un diploma y un presente")
    elif porcentaje_asistencia < 80:
        print("El estudiante está en riesgo de reprobar debido a la baja asistencia.")
    else:
        print("El estudiante tiene una buena asistencia.")

#Funcion de reportes 
def mostrar_reporte_ropa_informal(asistencias):
    reportes = 0
    monto_a_pagar = 0


    print("Reporte de Ropa Informal:")
    for i, asistencia in enumerate(asistencias, 1):
        dia_semana = (i - 1) % 7
        if asistencia == 2:
            if dia_semana == 4:  # Viernes
                monto_a_pagar += 300
                print(f"Día {i} (Viernes): Ropa de calle (Permitido)")

            else:
                reportes += 1
                print(f"Día {i} ({dia_nombre(dia_semana)}): Ropa de calle (No permitido)")

    print(f"\nTotal de reportes por ropa de calle: {reportes}")
    if reportes > 5:
        print("Alumno citado a dirección.")
    else:
        print("Alumno no citado a dirección.")
    print(f"Total a pagar por ropa de calle: {monto_a_pagar} pesos")

def dia_nombre(dia):
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return dias[dia]