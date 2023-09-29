# Solicitar al usuario el nombre del archivo de texto
nombre_archivo = input("Ingrese el nombre del archivo de texto con su formato: ")

try:
    # Abrir el archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()

        # Dividir el contenido en palabras usando el espacio como separador
        palabras = contenido.split()

        # Contar la cantidad de palabras
        cantidad_palabras = len(palabras)

        # Mostrar el resultado
        print(f"El archivo '{nombre_archivo}' contiene {cantidad_palabras} palabras.")

except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se encuentra.")
except Exception as e:
    print(f"Se produjo un error: {e}")