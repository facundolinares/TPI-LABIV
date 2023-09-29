class CuentaBancaria:
    def __init__(self, saldo_inicial=0.0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return True
        else:
            print("La cantidad a depositar debe ser mayor que cero.")
            return False

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        else:
            print("No tiene suficiente saldo para retirar esa cantidad.")
            return False

    def consultar_saldo(self):
        return self.saldo

# Crear una instancia de CuentaBancaria con un saldo inicial
saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))
mi_cuenta = CuentaBancaria(saldo_inicial)

while True:
    print("\nOpciones:")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar Saldo")
    print("4. Salir")

    opcion = input("Seleccione una opción (1/2/3/4): ")

    if opcion == '1':
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        mi_cuenta.depositar(cantidad)
    elif opcion == '2':
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        mi_cuenta.retirar(cantidad)
    elif opcion == '3':
        print("Saldo actual:", mi_cuenta.consultar_saldo())
    elif opcion == '4':
        print("Gracias por usar nuestro servicio. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")