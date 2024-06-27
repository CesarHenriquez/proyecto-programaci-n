import Functions as fu 

def menu_notas(notas):
    notas = []
    while True:
        print("\nMenú de Notas:")
        print("1. Ingresar notas")
        print("2. Ver promedio de las notas")
        print("3. Volver a menu principal")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            notas = fu.ingresar_notas()
            print("Notas ingresadas correctamente.")
        elif opcion == '2':
            if notas:
                promedio = fu.calcular_promedio(notas)
                print(f"El promedio de las notas es: {promedio:.2f}")
            else:
                print("No hay notas ingresadas o generadas para calcular el promedio.")
        elif opcion == '3':
            break #regresa al Menu Principal ¨
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            

def menu_asistencia(asistencias):
    while True:
        print("\nMenu de Asistencia:")
        print("1. Ver listado de asistencia")
        print("2. Evaluar asistencia")
        print("3. Volver al menú principal")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            fu.mostrar_asistencia(asistencias)
        elif opcion == "2":
            fu.evaluar_asistencia(asistencias)
        elif opcion == "3":
            break  # Regresar al menú principal
        else:
            print("Opción no válida, por favor elige nuevamente.")

#Menu Principal 


def menu():
    
    notas=[]
    asistencias = fu.generar_asistencia(5)
    while True:
        print("\nMenú Principal de Liceo:")
        print("1. Promedio de Notas")
        print("2. Menu de asistencia e inasistencia")
        print("3. Reporte de alumno con ropa informal")
        print("4. Salir")
        opcion1 = input("Elige una opción: ")
        
        if opcion1 == "1":
            menu_notas(notas)
        elif opcion1 == "2":
            menu_asistencia(asistencias)
        elif opcion1 == "3":
            fu.mostrar_reporte_ropa_informal(asistencias)
        elif opcion1 == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor elige nuevamente.")

if __name__ == "__main__":
    menu()
