import os

class CamionReparto:
    def __init__(self, capacidad):
        self.pila_paquetes = []
        self.capacidad = capacidad

    def cargar(self, paquete):
        if len(self.pila_paquetes) < self.capacidad:
            self.pila_paquetes.append(paquete)
            print(f"\n [CARGA] '{paquete}' ha sido colocado en la puerta.")
        else:
            print(f"\n [ERROR] El camión está lleno. No cabe '{paquete}'.")

    def entregar(self):
        if not self.pila_paquetes:
            print("\n [AVISO] No hay paquetes para entregar. El camión está vacío.")
        else:
            paquete = self.pila_paquetes.pop()
            print(f"\n [ENTREGA] Se ha entregado: '{paquete}'.")

    def mostrar_camion(self):
        print("\n--- VISTA ACTUAL DEL CAMIÓN (LIFO) ---")
        if not self.pila_paquetes:
            print("[ VACÍO ]")
        else:
            # Mostramos de arriba hacia abajo (lo último que entró es lo primero que se ve)
            for i, p in enumerate(reversed(self.pila_paquetes)):
                if i == 0:
                    print(f" -> [ {p} ]  <-- PRÓXIMO A SALIR (Puerta)")
                else:
                    print(f"    [ {p} ]")
        print("--------------------------------------")

def menu():
    print("\n SISTEMA DE GESTIÓN LOGÍSTICA (PILAS)")
    print("1. Cargar paquete (Push)")
    print("2. Entregar paquete (Pop)")
    print("3. Ver estado del camión")
    print("4. Salir")
    return input("Seleccione una opción: ")

def main():
    # Definimos una capacidad de 5 para el ejemplo
    camion = CamionReparto(capacidad=5)
    
    while True:
        opcion = menu()

        if opcion == "1":
            nombre = input("Nombre del paquete/producto: ")
            camion.cargar(nombre)
        
        elif opcion == "2":
            camion.entregar()
        
        elif opcion == "3":
            camion.mostrar_camion()
        
        elif opcion == "4":
            print("Saliendo del sistema de logística...")
            break
        
        else:
            print("Opcíon no válida, intente de nuevo.")

        input("\nPresione Enter para continuar...")
        # Limpia la pantalla según el sistema operativo para que se vea ordenado
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
