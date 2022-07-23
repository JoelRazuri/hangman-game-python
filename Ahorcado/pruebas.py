import random


LISTA_DEPORTES = ["Futbol","Voley","Handball","Tenis","Natacion","Golf","Beisbol","Basketball"]
LISTA_PELICULAS = ["Batman","Eternals","El señor de los anillos","Star Wars","Los vengadores","Harry Potter","Hercules"]
LISTA_COLORES = ["Rojo","Azul","Verde","Amarillo","Celeste","Negro","Blanco","Gris","Rosa","Marron","Lila","Violeta","Naranja"]
LISTA_ANIMALES = ["Perro","Gato","Leon","Leona","Jirafa","Iguana","Elefante","Hormiga","Tucan","Tigre","Puma","Tortuga","Ballena","Tiburon","Ocelote","Camello"]

LISTA_PALABRAS = [LISTA_DEPORTES,LISTA_PELICULAS,LISTA_COLORES,LISTA_ANIMALES]
LISTA_TEMATICAS = ["DEPORTES", "PELÍCULAS", "COLORES", "ANIMALES"]




def progreso_juego_mostrar(letras,error,palabra_barritas,tematica_azar):

    print(f"\n                  CATEGORÍA:{tematica_azar}",end="   ")
    mostrar_letras(letras)
    ahorcado(error)
    mostrar_palabra(palabra_barritas)
    print("\n\n")


def inicializar_jugador(jugadores,cant_jugadores):
    # Inicializa al jugador

    booleano = False

    for i in range(cant_jugadores):
        
        while not booleano:
            os.system('cls')
            nombre = input(f"Ingrese el nombre del jugador {i+1}(Solo se permiten letras):")
            jugadores.append(nombre)
            booleano = validar_nombre_jugador(jugadores[i])
        
            if not booleano:
                input("El nombre ingresado no es válido.(Solo se permiten letras)...")
                os.system('cls')

    os.system('cls')
    
    return jugadores