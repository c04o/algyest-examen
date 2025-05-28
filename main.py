from collections import deque

class AlcaldiaGestionTramites:
    def __init__(self):
        self.cola = deque()  # Cola para ciudadanos en espera: tuplas (nombre, tramite)
        self.historial = {}  # Diccionario: {nombre_ciudadano: [lista_de_tramites_completados]}

    def agregar_ciudadano(self, nombre, tramite):
        """
        Agrega un ciudadano a la cola de espera con un trámite específico.
        """
        self.cola.append((nombre, tramite))
        print(f"Ciudadano '{nombre}' agregado a la cola con el trámite '{tramite}'.")

    def atender_siguiente(self):
        """
        Atiende al siguiente ciudadano en la cola, registra el trámite en su historial y lo elimina de la cola.
        """
        if not self.cola:
            print("No hay ciudadanos en la cola.")
            return
        nombre, tramite = self.cola.popleft()
        if nombre not in self.historial:
            self.historial[nombre] = []
        self.historial[nombre].append(tramite)
        print(f"Atendido ciudadano '{nombre}' para el trámite '{tramite}'. Trámite registrado como completado.")

    def mostrar_cola(self):
        """
        Muestra los ciudadanos en la cola de espera.
        """
        if not self.cola:
            print("La cola está vacía.")
            return
        print("\nCiudadanos en cola:")
        for i, (nombre, tramite) in enumerate(self.cola, start=1):
            print(f"{i}. {nombre} - Trámite: {tramite}")

    def ver_historial(self, ciudadano):
        """
        Muestra el historial de trámites de un ciudadano, del más reciente al más antiguo.
        """
        if ciudadano in self.historial and self.historial[ciudadano]:
            print(f"\nHistorial de trámites de {ciudadano}:")
            for i, tramite in enumerate(reversed(self.historial[ciudadano]), 1):
                print(f"   {i}. {tramite}")
        else:
            print(f"No hay historial de trámites para {ciudadano}.")

def menu():
    gestion = AlcaldiaGestionTramites()
    tramites_posibles = {
        "1": "Partida de nacimiento",
        "2": "Licencia de construcción",
        "3": "Permiso para eventos",
        "4": "Pago de impuestos municipales"
    }

    while True:
        print("\n--- Gestión de Trámites en la Alcaldía ---")
        print("1. Agregar ciudadano a la cola")
        print("2. Atender siguiente ciudadano")
        print("3. Mostrar cola de espera")
        print("4. Ver historial de ciudadano")
        print("5. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Ingrese el nombre del ciudadano: ").strip()
            if len(nombre) < 3:
                print("Nombre inválido. Debe tener al menos 3 caracteres.")
                continue
            print("\nTipos de trámite:")
            for k, v in tramites_posibles.items():
                print(f"{k}. {v}")
            tipo = input("Seleccione el número del trámite: ").strip()
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
            ciudadano = input("Ingrese el nombre del ciudadano: ").strip()
            gestion.ver_historial(ciudadano)

        elif opcion == "5":
            print("Saliendo del sistema. ¡Adiós!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()
