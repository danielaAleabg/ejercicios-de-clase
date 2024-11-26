import csv
from datetime import datetime

def obtener_datos_estudiante():
    """
    Función que solicita los datos de un estudiante.
    """
    nombre = input("Ingrese el nombre del estudiante: ")
    codigo = input("Ingrese el código del estudiante (8 dígitos): ")
    while len(codigo) != 8 or not codigo.isdigit():
        print("El código debe tener 8 dígitos numéricos.")
        codigo = input("Ingrese el código del estudiante (8 dígitos): ")
    return nombre, codigo

def registrar_asistencia(nombre, codigo, archivo_csv):
    """
    Función para registrar la asistencia de un estudiante en un archivo CSV.
    """
    fecha = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    asistencia = input(f"¿El estudiante {nombre} ({codigo}) asistió? (S/N): ").upper()
    
    while asistencia not in ['S', 'N']:
        print("Por favor ingrese 'S' para Sí o 'N' para No.")
        asistencia = input(f"¿El estudiante {nombre} ({codigo}) asistió? (S/N): ").upper()
    
    with open(archivo_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre, codigo, fecha, hora, asistencia])
    
    print(f"Asistencia registrada para el estudiante {nombre} ({codigo}).")

def mostrar_registros(archivo_csv):
    """
    Función para mostrar los registros de asistencia.
    """
    try:
        with open(archivo_csv, mode='r') as file:
            reader = csv.reader(file)
            print("\nRegistros de Asistencia:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No se ha encontrado el archivo de registros.")

def main():
    archivo_csv = 'registros_asistencia.csv'
    
    while True:
        print("\nMenú de opciones:")
        print("1. Registrar asistencia de un estudiante")
        print("2. Ver registros de asistencia")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == '1':
            nombre, codigo = obtener_datos_estudiante()
            registrar_asistencia(nombre, codigo, archivo_csv)
        
        elif opcion == '2':
            mostrar_registros(archivo_csv)
        
        elif opcion == '3':
            print("Saliendo del sistema.")
            break
        
        else:
            print("Opción no válida, por favor ingrese 1, 2 o 3.")

if __name__ == "__main__":
    main()
