from typing import List

class EditorAvanzado:
    def __init__(self):
        self.texto_actual: str = ""

        self.pila_deshacer: List[str] = []

        self.pila_rehacer: List[str] = []

    def escribir(self, nuevo_texto: str):

        self.pila_deshacer.append(self.texto_actual)
        
        # 2. Modificamos el texto
        if self.texto_actual:
            self.texto_actual += " " + nuevo_texto
        else:
            self.texto_actual += nuevo_texto
            

        self.pila_rehacer.clear()
        
        print(f"--> Escribiste: '{nuevo_texto}'")

    def deshacer(self):
        """(Ctrl+Z) Regresa al estado anterior."""
        if not self.pila_deshacer:
            print("(!) No hay acciones para deshacer.")
            return


        self.pila_rehacer.append(self.texto_actual)


        estado_anterior = self.pila_deshacer.pop()
        self.texto_actual = estado_anterior
        
        print("<< Acción deshecha (Ctrl+Z).")

    def rehacer(self):
        """(Ctrl+Y) Recupera lo que se deshizo."""
        if not self.pila_rehacer:
            print("(!) No hay acciones para rehacer.")
            return

        self.pila_deshacer.append(self.texto_actual)


        futuro_recuperado = self.pila_rehacer.pop()
        self.texto_actual = futuro_recuperado
        
        print(">> Acción recuperada (Ctrl+Y).")

    def ver_estado(self):
        print("\n" + "┌" + "─"*30 + "┐")
        print(f"│ PANTALLA: {self.texto_actual}")
        print("└" + "─"*30 + "┘")

        print(f"[Debug] Pila Undo: {len(self.pila_deshacer)} items | Pila Redo: {len(self.pila_rehacer)} items\n")




def main():
    editor = EditorAvanzado()
    
    while True:
        try:
            print("1. Escribir | 2. Deshacer | 3. Rehacer | 4. Salir")
            opcion = input("Opción: ")

            if opcion == "1":
                txt = input("Ingrese texto: ")
                editor.escribir(txt)
            elif opcion == "2":
                editor.deshacer()
            elif opcion == "3":
                editor.rehacer()
            elif opcion == "4":
                break
            else:
                print("Opción inválida.")
            
            editor.ver_estado()
            
        except Exception as e:
            print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()