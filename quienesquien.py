import numpy as np
import csv

def levantaTablero():
    '''
    Al iniciar la partida cargamos todos los personajes en memoria los cuales
    iremos descartando a lo largo de la partida.

    Return:
        list: lista de personajes
        list: lista de preguntas
        np.array: lista de caracteristicas
        np.array: tablero
    '''
    lista_caract = []
    lista_preguntas = []
    csvFileArray = []

    # Abrimos base de datos y lo cargamos en variables
    with open('db_qeq.csv', newline='') as csvfile:
        spamreader  = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            csvFileArray.append(row)

        lista_personajes = csvFileArray[0]
        lista_personajes.pop(0)
        csvFileArray.pop(0)
        for a in csvFileArray:
            lista_preguntas.append(a[0])
            a.pop(0)
            list_float = list(map(float, a))
            np.array(list_float)
            lista_caract.append(list_float)

        np.array(lista_caract)
    # El tablero es una lista de 1 por cada personaje
    tablero = np.ones(24)

    return lista_personajes, lista_preguntas, lista_caract, tablero

def preguntaIa(tablero, lista_caract, lista_preguntas, pregunta_inicial = False):
    '''
    Le pasaremos los personajes que quedan en juego y nos dara la pregunta
    que debemos realizar.

    Args:
        personejes (list): lista de personajes que siguen en el juego.
        pregunta_inicial (bool): Evita pregunta inicial hombre o mujer.

    Returns:
        list: lista con personajes con la caracteristica y pregunta.
    '''
    num_carac = []
    for a in lista_caract:
        # Vemos cuantos de los personejes en juego tienen la característica de cada pregunta.
        b = tablero * np.array(a)
        # Almacenamos una lista con el resultado de todas las preguntas.
        num_carac.append((b == 1).sum())

    # Lo ideal es elegir una pregunta que descarte la mitad de los personajes en juego. Si no 
    # es posible elegiremos la mas cercana a la mitad.
    numPersonajes = (np.array(tablero) == 1).sum()
    mitadPersonajes = numPersonajes//2
    aryDiferencial = np.absolute(num_carac - mitadPersonajes)
    indiceCercano = aryDiferencial.argmin()
    valorCercano = num_carac[indiceCercano]
    aryPregunta = lista_caract[indiceCercano]
    pregunta = lista_preguntas[indiceCercano]

    # Temos que consultar todas as preguntas e ver cal facemos.
    return aryPregunta, pregunta

def descartaPersonejes(tablero, aryPregunta, s_n):
    '''
    Consultamos base de datos y vemos cual cumple o no las condidiones
    para descartar personajes.

    Args:
        personajes (list): personajes no descartados.
        pregunta (str): pregunta realizada.
        s/n (bool): respuesta true o false del oponente.

    Returns:
        list: lista de personajes que siguen en juego.
    '''
    if s_n == 'n':
        for a in range(len(aryPregunta)):
            if aryPregunta[a] == 1.0:
                aryPregunta[a] = 0.0
            else:
                aryPregunta[a] = 1.0

    tablero = tablero * aryPregunta

    return tablero

def personajesVivos(tablero, lista_personajes):
    '''
    Muestra los personajes que quedan en juego.
    '''
    for a in range(len(lista_personajes)):
        if tablero[a] == 1:
            print(lista_personajes[a])

def main():

    # Levantamos el tablero y damos comienzo a la partida
    lista_personajes, lista_preguntas, lista_caract, tablero = levantaTablero()

    for a in range(6):
        aryPregunta, pregunta = preguntaIa(tablero, lista_caract, lista_preguntas)

        print(pregunta)
        print('s ou n:')
        resposta = input()
        tablero = descartaPersonejes(tablero, aryPregunta, resposta)
        personajesVivos(tablero, lista_personajes)
        numPersonajes = (np.array(tablero) == 1).sum()
        if numPersonajes == 1:
            print(f'El personaje es')
            personajesVivos(tablero, lista_personajes)
            break

if __name__ == "__main__":
    main()
