class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def añadir(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def eliminar(self, valor):
        actual = self.cabeza
        previo = None
        while actual and actual.valor != valor:
            previo = actual
            actual = actual.siguiente
        if not actual:
            print(f"La canción '{valor}' no se encuentra en la playlist.")
            return
        if not previo:
            self.cabeza = actual.siguiente
        else:
            previo.siguiente = actual.siguiente
        print(f"La canción '{valor}' ha sido eliminada de la playlist.")
    
    def mostrar(self):
        actual = self.cabeza
        if not actual:
            print("La playlist está vacía.")
            return
        print("Playlist:")
        while actual:
            print(f"- {actual.valor}")
            actual = actual.siguiente

class SistemaDeGestionDePlaylist:
    def __init__(self):
        self.playlist = ListaEnlazada()
    
    def añadir_cancion(self, cancion):
        self.playlist.añadir(cancion)
        print(f"La canción '{cancion}' ha sido añadida a la playlist.")
    
    def eliminar_cancion(self, cancion):
        self.playlist.eliminar(cancion)
    
    def mostrar_playlist(self):
        self.playlist.mostrar()
    
    def mostrar_menu(self):
        while True:
            print("\nSistema de Gestión de Playlist")
            print("1. Añadir canción")
            print("2. Eliminar canción")
            print("3. Mostrar playlist")
            print("4. Salir")
            opcion = input("Elige una opción: ")
            
            if opcion == '1':
                cancion = input("Ingrese el nombre de la canción a añadir: ")
                self.añadir_cancion(cancion)
            elif opcion == '2':
                cancion = input("Ingrese el nombre de la canción a eliminar: ")
                self.eliminar_cancion(cancion)
            elif opcion == '3':
                self.mostrar_playlist()
            elif opcion == '4':
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, elige una opción del 1 al 4.")

sistema = SistemaDeGestionDePlaylist()
sistema.mostrar_menu()