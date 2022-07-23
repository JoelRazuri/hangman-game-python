from constantes import*
import os, sys
import random

def mostrar_reglas():
    # Muestra las reglas del juego

    print("\n-Jugadores: 2.")
    print("\n-Objetivo: Descubrir la palabra secreta.")
    print("\n-Preparación: Se elige una palabra al azar, se dibuja una línea por cada letra y se dibuja la base de la horca (sin el muñeco).\n Tambien se deja la categoría.")
    print("\n-Turnos: Empieza el jugador 1 en su turno escribe una letra. \n  --Si la letra está, entonces se anota sobre la línea que ocupa su lugar en la palabra secreta.\n  --Si la letra no está, entonces se anotará la letra sobre la horca y  se dibujará una parte del muñeco.\n-Una vez encontrada la palabra o completado el muñeco, sigue el jugador 2.")
    print("\n-Muñeco: El muñeco se dibuja en 6 partes (cabeza, tronco y extremidades), por lo que los adivinadores tiene 6 posibilidades de fallar.")
    print("\n-Encuentra la Palabra: \n  --Si el jugador encuentra la palabra, entonces se completa la solución en la pantalla y suma 2 puntos.")
    print("\n-Fin de la partida:\n   -GANA el primer jugador que llegue a 10 puntos, el otro PIERDE.")
    input("\nPresione enter para volver al menu...")
    sys.stdout.flush()
    os.system('cls')
    menu()


def mostrar_lista_palabras(lista_palabras,lista_tematicas):
    # Muestra las palabras que te pueden tocar en el juego y sus tematicas.

    
    for tematica in range(len(lista_palabras)):

        print()
        print(lista_tematicas[tematica])
        print("(",end="")

        for palabra in range(len(lista_palabras[tematica])):
            
            if palabra+1<len(lista_palabras[tematica]):
                print(lista_palabras[tematica][palabra],end=", ")
            else:
                print(lista_palabras[tematica][palabra],end=".)\n")
        
    print()
    input("Presione enter para volver al menu...")
    sys.stdout.flush()
    os.system('cls')
    menu()

    
def agregar_palabras():
    # Agrega palabras a las categorías existentes.

    print("EN MANTENIMIENTO :D\n")
    input("Presione enter para volver al menu...")
    sys.stdout.flush()
    os.system('cls')
    menu()


def palabra_azarf(lista_palabras,lista_tematicas):
    # Elige una palabra al azar con su tematica y las retorna.

    limite_sup = len(lista_tematicas) - 1
    tematica_azar = random.randint(0,limite_sup)
    palabra_azar = random.choice(lista_palabras[tematica_azar])

    return palabra_azar, lista_tematicas[tematica_azar]


def ahorcado(error):
    # Grafica el ahorcado
    
    print(" ___________")
    for i in range(5):
        if(i==0):
            print("\n |/")
        
        if(i>0):
            print("\n |")
        
        if(i<1):
            print("        |")
        
        if((i==1) and (error>0)):
            print("        O")
        
        if(i==2):
            if(error>1):
                print("      /",end="")
            
            if(error>2):
                print(" |",end="")
            
            if(error>3):
                print(" \\")
            
        
        if(i==3):
            if(error>4):
                print("      /",end="")
            
            if(error>5):
                print("   \\")
            
    print("_______")
    
    for i in range(2):
        if(i<1):
            print("\n |    |")
        
        if(i==1):
            print("\n |____|",end="   ")  



def validar_nombre_jugador(nombre):
    # Verifica que el nombre sean solo caracteres alfabeticos.

    booleano = False
    error = False
    i = 0

    while (i<len(nombre) and not error):
        if ((nombre[i]>='A' and nombre[i]<='Z') or (nombre[i]>='a' and nombre[i]<='z') or nombre[i]==" "):
            booleano = True
        else:
            booleano = False
            error = True             
        i+=1

    return booleano



def inicializar_jugador(nombre_jugadores,cant_jugadores):
    # Inicializa a los jugador

    for i in range(cant_jugadores):
        
        booleano = False

        while not booleano:
            os.system('cls')
            nombre = input(f"Ingrese el nombre del jugador {i+1}(Solo se permiten letras):")
            sys.stdout.flush()
            booleano = validar_nombre_jugador(nombre)
        
            if not booleano:
                input("El nombre ingresado no es válido.(Solo se permiten letras)...")
                sys.stdout.flush()
                os.system('cls')

        nombre = nombre.upper()
        nombre_jugadores.append(nombre)

    os.system('cls')
    
    return nombre_jugadores


def mostrar_letras(letras):
    # Muestra la letra

    print("LETRAS:",end=" ")
    for i in range(len(letras)):
        print(letras[i],end=" ")

    print()

def mostrar_palabra(palabra):
    # Muestra la palabra

    for i in range(len(palabra)):
        print(palabra[i],end=" ")



def palabra_con_barritas(palabra):
    # Oculta con barritas a la palabra al azar

    palabra_barritas = list(palabra)

    for i in range(len(palabra)):
        if (palabra_barritas[i]>='A' and palabra_barritas[i]<='Z'):
            palabra_barritas[i]="_"

    palabra_barritas = "".join(palabra_barritas)

    return palabra_barritas


def buscar_letra_en_palabra(letra,palabra_barritas,palabra_azar):
    # Busca la letra en la palabra y si esta la devuelve con la letra y un valor booleano.

    booleano = False
    palabra_barritas = list(palabra_barritas)

    for i in range(len(palabra_azar)):

        if (letra==palabra_azar[i]):
            palabra_barritas[i] = letra
            booleano = True

    palabra_barritas = "".join(palabra_barritas)

    return palabra_barritas,booleano



def progreso_juego_mostrar(letras,error,palabra_barritas,tematica_azar,contador_general,nombre_jugadores,max_puntaje):

    print(f"\n                  CATEGORÍA:{tematica_azar}",end="   ")
    mostrar_letras(letras)
    ahorcado(error)
    mostrar_palabra(palabra_barritas)
    print("\n\n")
    mostrar_puntajes(contador_general,nombre_jugadores,max_puntaje)
    print("\n\n")
        

def validar_letra(letra,letras,booleano):
    # Se fija que el caracter ingresado sea una letra y que no este repetida.

    if not (letra>='A' and letra<='Z'):
        input("Ingrese una letra...")
        sys.stdout.flush()
    else:
        booleano = True
    
    if letra in letras:
        input("Letra repetida, ingrese otra letra...")
        sys.stdout.flush()
        booleano = False
    
    if len(letra)>1:
        input("Ingrese solo una letra...")
        sys.stdout.flush()
        booleano = False

    return booleano



def juego (nombre_jugadores,contador_puntajes,lista_palabras,lista_tematicas,ganador,max_puntaje):
    # Lógica del juego 

    for i in range(len(nombre_jugadores)):
    
        os.system('cls')
        palabra_azar, tematica_azar = palabra_azarf(lista_palabras,lista_tematicas)
        palabra_azar = palabra_azar.upper()
        palabra_barritas = palabra_con_barritas(palabra_azar)
        error = 0
        palabra_encontrada = False
        letras = []

        while (error<6 and not palabra_encontrada):
            
            booleano = False
            
            while not booleano:
            
                progreso_juego_mostrar(letras,error,palabra_barritas,tematica_azar,contador_puntajes,nombre_jugadores,max_puntaje)
                letra = input(f"JUGADOR: {nombre_jugadores[i]}, ingrese una letra:")
                sys.stdout.flush()
                letra = letra.upper()
                booleano = validar_letra(letra,letras,booleano)
                os.system('cls')
                
            palabra_barritas,booleano = buscar_letra_en_palabra(letra,palabra_barritas,palabra_azar)
            
            if not booleano:
                letras.append(letra)
                error+=1
            else:
                letras.append(letra)

            if (palabra_barritas == palabra_azar):
                palabra_encontrada = True
        
            
        if palabra_encontrada:
            progreso_juego_mostrar(letras,error,palabra_barritas,tematica_azar,contador_puntajes,nombre_jugadores,max_puntaje)
            print("\n\n")
            input("ENCONTRASTE LA PALABRA :D ...")
            sys.stdout.flush()
            contador_puntajes[i] = contador_puntajes[i] + 2
            
        if (error==6):
            progreso_juego_mostrar(letras,error,palabra_barritas,tematica_azar,contador_puntajes,nombre_jugadores,max_puntaje)
            print("\n\n")
            input("SE TE ACABARON LOS INTENTOS, SUERTE LA PROXIMA :C ...")
            sys.stdout.flush()

        if (contador_puntajes[i])==max_puntaje:
            ganador = True
            break
    
    return ganador


def mostrar_puntajes(contador_puntajes,nombre_jugadores,max_puntaje):

    for i in range(len(contador_puntajes)):
        print(f"JUGADOR {i+1}: {nombre_jugadores[i]}, PUNTAJE: {contador_puntajes[i]}")

    for i in range(len(contador_puntajes)):
        
        if (contador_puntajes[i]==max_puntaje):
            print(f"\nEL GANADOR ES {nombre_jugadores[i]}\n\nFELICITACIONES!!!! :D")
        

def empezar_juego(lista_palabras,lista_tematicas,cant_jugadores,max_puntaje):
    # Inicializa a los jugadores, busca la palabra y la tematica al azar y empieza el juego.

    ganador = False
    nombre_jugadores = []
    contador_puntajes = [0,0]

    inicializar_jugador(nombre_jugadores,cant_jugadores)
    
    while not ganador:
        os.system('cls')
        ganador = juego(nombre_jugadores,contador_puntajes,lista_palabras,lista_tematicas,ganador,max_puntaje)
            
    print("")
    mostrar_puntajes(contador_puntajes,nombre_jugadores,max_puntaje)
    
    input("Presione enter para volver al menu...")
    sys.stdout.flush()
    os.system('cls')
    menu()



def menu():
    
    print("AHORCADO")
    print("------------------------------------------------------------------------------------------------------------------")
    print("1.EMPEZAR JUEGO\n2.REGLAS\n3.VER PALABRAS\n4.AGREGAR PALABRAS\n5.SALIR")
    print("------------------------------------------------------------------------------------------------------------------")

    n = input()
    sys.stdout.flush()

    if n=="1":
        os.system('cls')
        empezar_juego(LISTA_PALABRAS,LISTA_CATEGORIAS,CANT_JUGADORES,MAX_PUNTAJE)
    elif n=="2":
        os.system('cls')
        mostrar_reglas()
    elif n=="3":
        os.system('cls')
        mostrar_lista_palabras(LISTA_PALABRAS,LISTA_CATEGORIAS)
    elif n=="4":
        os.system('cls')
        agregar_palabras()
    elif n=="5":
        print()
        print("MUCHAS GRACIAS POR JUGAR :D")
    else:
        os.system('cls')
        if not (n=="1" or n=="2" or n=="3" or n=="4" or n=="5"):
            menu()
    


