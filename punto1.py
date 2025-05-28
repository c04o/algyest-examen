from collections import deque

# Cola para gestionar los trámites en espera (FIFO)
cola_espera = deque()

def agregar_a_cola(tramite):
    """
    Agrega un trámite a la cola de espera.
    """
    cola_espera.append(tramite)
    print(f"Trámite '{tramite}' agregado a la cola")

if __name__ == "__main__":
    while True:
        print("\nSeleccione el trámite a ingresar:")
        print("1. Partida de nacimiento")
        print("2. Licencia de construcción")
        print("3. Permiso para evento")
        print("4. Pago de impuestos municipales")
        print("5. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            agregar_a_cola("Partida de nacimiento")
        elif opcion == "2":
            agregar_a_cola("Licencia de construcción")
        elif opcion == "3":
            agregar_a_cola("Permiso para evento")
        elif opcion == "4":
            agregar_a_cola("Pago de impuestos municipales")
        elif opcion == "5":
            print("Saliendo del sistema. ¡Adiós!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
