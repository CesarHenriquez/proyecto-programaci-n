#Proyecto Programación
print("Bienvenido al sistema de registros y reportes de alumno") #MENU INICIAL DEL PROGRAMA PRINCIPAL1

print("           ¿Qué acción desea realizar?")
accion_docente = int(input("""1. Promedio de notas    
2. Asistencia e inasistencia
3. Reporte de alumno con ropa informal
4. Salir
Ingrese una opción: """))
while True:
    if accion_docente == 1:
         notas = int(input("Registre las 8 notas del alumnado para saber su promedio:"))
