from collections import deque


cola_tramites = deque()
historial = {}

# Función para mostrar la cola de espera
def ver_cola():
    print("\n Cola de espera:")
    if not cola_tramites:
        print("   La cola está vacía.")
    else:
        for i, (nombre, tramite) in enumerate(cola_tramites, 1):
            print(f"   {i}. {nombre} - {tramite}")

# Función para atender al siguiente ciudadano
def atender_ciudadano():
    print("\n Atendiendo ciudadano:")
    if not cola_tramites:
        print("   No hay ciudadanos en espera.")
        return
    nombre, tramite = cola_tramites.popleft()
    print(f"   Se atendió a {nombre}, trámite: {tramite}")

    
    if nombre not in historial:
        historial[nombre] = []
    historial[nombre].append(tramite)

# Función para ver el historial de un ciudadano
def ver_historial(nombre):
    print(f"\n Historial de trámites para {nombre}:")
    if nombre not in historial or not historial[nombre]:
        print("   No hay historial registrado.")
    else:
        for i, tramite in enumerate(reversed(historial[nombre]), 1):
            print(f"   {i}. {tramite}")

# Simulación local para prueba 
if __name__ == "__main__":
    # Prueba rápida
    cola_tramites.append(("Yader", "Partida de nacimiento"))
    cola_tramites.append(("Stacy", "Licencia de construcción"))

    while True:
        print("\n--- Funciones del Funcionario ---")
        print("1. Ver cola de espera")
        print("2. Atender al siguiente ciudadano")
        print("3. Ver historial de un ciudadano")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ver_cola()
        elif opcion == '2':
            atender_ciudadano()
        elif opcion == '3':
            nombre = input("Nombre del ciudadano: ")
            ver_historial(nombre)
        elif opcion == '4':
            break
        else:
            print("Opción inválida.")
