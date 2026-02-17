class CamionReparto:
    def __init__(self, capacidad):
        self.pila_paquetes = []
        self.capacidad = capacidad

    def cargar_paquete(self, nombre_paquete):
        """Añade un paquete al camión (PUSH)"""
        if len(self.pila_paquetes) < self.capacidad:
            self.pila_paquetes.append(nombre_paquete)
            print(f" Cargado: '{nombre_paquete}' (Está en la puerta del camión)")
        else:
            print(f" ¡Camión lleno! No cabe el paquete: {nombre_paquete}")

    def entregar_paquete(self):
        """Entrega el paquete que está más a mano (POP)"""
        if not self.pila_paquetes:
            print("El camión está vacío. No hay nada que entregar.")
            return None
        
        paquete = self.pila_paquetes.pop()
        print(f"✅ Entregando: '{paquete}' (Salió del camión)")
        return paquete

    def ver_inventario(self):
        print("\n--- ESTADO ACTUAL DEL CAMIÓN (De la puerta hacia el fondo) ---")
        if not self.pila_paquetes:
            print("[ Vacío ]")
        else:

            for i, pkg in enumerate(reversed(self.pila_paquetes)):
                pos = "PUERTA" if i == 0 else f"Fila {i}"
                print(f"| {pos}: {pkg} |")
        print("----------------------------------------------------------\n")



def simulacion_logistica():

    mi_camion = CamionReparto(capacidad=3)

    print("--- FASE DE CARGA (En la bodega) ---")

    mi_camion.cargar_paquete("Lavadora (Cliente A - Al fondo)")
    mi_camion.cargar_paquete("Refrigerador (Cliente B - Medio)")
    mi_camion.cargar_paquete("Sofá (Cliente C - En la puerta)")

    mi_camion.ver_inventario()

    print("--- FASE DE REPARTO (En la ciudad) ---")

    mi_camion.entregar_paquete() 
    
    mi_camion.ver_inventario()

    print("--- LLEGADA DE EMERGENCIA ---")

    mi_camion.cargar_paquete("Televisor 75' (Cliente D - Nueva Puerta)")
    
    mi_camion.ver_inventario()

if __name__ == "__main__":
    simulacion_logistica()