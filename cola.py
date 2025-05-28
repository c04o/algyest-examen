from collections import deque

class AlcaldiaGestionTramites:
    def __init__(self):
        self.cola = deque()  # Queue for waiting citizens: tuples (name, procedure)
        self.historial = {}  # Dict: {citizen_name: [list_of_completed_procedures]}

    def agregar_ciudadano(self, nombre, tramite):
        self.cola.append((nombre, tramite))
        print(f"Ciudadano '{nombre}' agregado a la cola con el trámite '{tramite}'.")

    def atender_siguiente(self):
        if not self.cola:
            print("No hay ciudadanos en la cola.")
            return
        nombre, tramite = self.cola.popleft()
        if nombre not in self.historial:
            self.historial[nombre] = []
        self.historial[nombre].append(tramite)
        print(f"Atendido ciudadano '{nombre}' para el trámite '{tramite}'. Trámite registrado como completado.")

    def mostrar_cola(self):
        if not self.cola:
            print("La cola está vacía.")
            return
        print("\nCiudadanos en cola:")
        for i, (nombre, tramite) in enumerate(self.cola, start=1):
            print(f"{i}. {nombre} - Trámite: {tramite}")

    def mostrar_historial(self):
        if not self.historial:
            print("No hay trámites completados aún.")
            return
        print("\nHistorial de trámites completados por ciudadano:")
        for nombre, tramites in self.historial.items():
            print(f"- {nombre}:")
            for t in tramites:
                print(f"  • {t}")

def menu():
    gestion = AlcaldiaGestionTramites()

    opciones = {
        "1": "Agregar ciudadano a la cola",
        "2": "Atender siguiente ciudadano",
        "3": "Mostrar cola de espera",
        "4": "Mostrar historial de trámites completados",
        "0": "Salir"
    }

    while True:
        print("\n--- Gestión de Trámites en la Alcaldía ---")
        for k, v in opciones.items():
            print(f"{k}. {v}")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Ingrese el nombre del ciudadano: ").strip()
            if len(nombre) < 3:
                print("Nombre inválido. Debe tener al menos 3 caracteres.")
                continue
            print("Tipos de trámite:")
            print("1. Partida de nacimiento")
            print("2. Licencia de construcción")
            print("3. Permiso para eventos")
            print("4. Otros")
            tipo = input("Seleccione el número del trámite: ").strip()
            tramites_posibles = {
                "1": "Partida de nacimiento",
                "2": "Licencia de construcción",
                "3": "Permiso para eventos",
                "4": "Otros"
            }
            tramite = tramites_posibles.get(tipo)
            if not tramite:
                print("Trámite inválido.")
                continue
            gestion.agregar_ciudadano(nombre, tramite)

        elif opcion == "2":
            gestion.atender_siguiente()

        elif opcion == "3":
            gestion.mostrar_cola()

        elif opcion == "4":
            gestion.mostrar_historial()

        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
