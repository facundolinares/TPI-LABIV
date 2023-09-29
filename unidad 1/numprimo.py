def es_primo(numero):
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    # Comprobar si el número es divisible por cualquier número entre 2 y la raíz cuadrada del número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False  # El número es divisible, no es primo

    return True  # Si no se encontraron divisores, el número es primo

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Llamar a la función es_primo y mostrar el resultado
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")