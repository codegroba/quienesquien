import numpy as np

'''
Creamos una base de datos temporal en python.
'''
personajes          = ['Max','Susan','Tom','Sam','Anne','Robert','Anita','Bill','Claire','Bernard','Alfred','Frans','George','David','Paul','Joe','Phillip','Peter','Alex','Maria','Eric','Herman','Richard','Charles']

mujer               = [  0  ,   1   ,  0  ,  0  ,   1  ,   0    ,   1   ,  0   ,   1    ,    0    ,   0    ,   0   ,   0    ,   0   ,  0   ,  0  ,    0    ,   0   ,  0   ,   1   ,  0   ,   0    ,    0    ,   0     ],['Es mujer?']
hombre              = [  1  ,   0   ,  1  ,  1  ,   0  ,   1    ,   0   ,  1   ,   0    ,    1    ,   1    ,   1   ,   1    ,   1   ,  1   ,  1  ,    1    ,   1   ,  1   ,   0   ,  1   ,   1    ,    1    ,   1     ],['Es hombre?']

pelirrojo           = [  0  ,   0   ,  0  ,  0  ,   0  ,   0    ,   0   ,  1   ,   1    ,    0    ,   1    ,   1   ,   0    ,   0   ,  0   ,  0  ,    0    ,   0   ,  0   ,   0   ,  0   ,   1    ,    0    ,   0     ],['Es pelirrojo?']
pelo_castaño        = [  0  ,   0   ,  0  ,  0  ,   0  ,   1    ,   0   ,  0   ,   0    ,    1    ,   0    ,   0   ,   0    ,   0   ,  0   ,  0  ,    0    ,   0   ,  0   ,   1   ,  0   ,   0    ,    0    ,   0     ],['Tiene el pelo castaño?']
pelo_rubio          = [  0  ,   0   ,  0  ,  0  ,   0  ,   0    ,   1   ,  0   ,   0    ,    0    ,   0    ,   0   ,   0    ,   1   ,  0   ,  1  ,    0    ,   0   ,  0   ,   0   ,  1   ,   0    ,    0    ,   1     ],['Es rubio?']
pelo_negro          = [  1  ,   0   ,  1  ,  0  ,   1  ,   0    ,   0   ,  0   ,   0    ,    0    ,   0    ,   0   ,   0    ,   0   ,  0   ,  0  ,    1    ,   0   ,  1   ,   0   ,  0   ,   0    ,    0    ,   0     ],['Tiene el pelo negro?']
pelo_blanco         = [  0  ,   1   ,  0  ,  1  ,   0  ,   0    ,   0   ,  0   ,   0    ,    0    ,   0    ,   0   ,   1    ,   0   ,  1   ,  0  ,    0    ,   1   ,  0   ,   0   ,  0   ,   0    ,    0    ,   0     ],['Tiene el pelo blanco?']

raya_al_lado        = [  0  ,   1   ,  0  ,  0  ,   0  ,   1    ,   0   ,  0   ,   0    ,    0    ,   0    ,   0   ,   0    ,   1   ,  1   ,  0  ,    0    ,   1   ,  0   ,   0   ,  0   ,   0    ,    0    ,   1     ],['Tiene la raya al lado?']
raya_al_medio       = [  0  ,   0   ,  0  ,  0  ,   0  ,   0    ,   1   ,  0   ,   0    ,    0    ,   1    ,   0   ,   0    ,   0   ,  0   ,  0  ,    0    ,   0   ,  0   ,   0   ,  0   ,   0    ,    0    ,   0     ],['Tiene la raya al medio?']

calva               = [  0  ,   0   ,  1  ,  1  ,   0  ,   0    ,   0   ,  1   ,   0    ,    0    ,   0    ,   0   ,   0    ,   0   ,  0   ,  0  ,    0    ,   0   ,  0   ,   0   ,  0   ,   1    ,    1    ,   0     ],['Es calvo?']
pelo_largo          = [  0  ,   1   ,  0  ,  0  ,   0  ,   0    ,   1   ,  0   ,   0    ,    0    ,   1    ,   0   ,   0    ,   0   ,  0   ,  0  ,    0    ,   0   ,  0   ,   1   ,  0   ,   0    ,    0    ,   0     ],['Tiene el pelo largo?']
pelo_corto          = [  1  ,   0   ,  0  ,  0  ,   1  ,   0    ,   0   ,  0   ,   0    ,    0    ,   0    ,   1   ,   0    ,   0   ,  0   ,  1  ,    1    ,   0   ,  1   ,   0   ,  0   ,   0    ,    0    ,   0     ],['Tiene el pelo corto?']

nariz_grande        = [  1  ,   0   ,  0  ,  0  ,   1  ,   1    ,   0   ,  0   ,   0    ,    1    ,   0    ,   0   ,   0    ,   0   ,  0   ,  0  ,    0    ,   1   ,  0   ,   0   ,  0   ,   1    ,    0    ,   0     ],['Tiene la nariz grande?']
nariz_pequeña       = [  0  ,   1   ,  1  ,  1  ,   0  ,   0    ,   1   ,  1   ,   1    ,    0    ,   1    ,   1   ,   1    ,   1   ,  1   ,  1  ,    1    ,   0   ,  1   ,   1   ,  1   ,   0    ,    1    ,   1     ],['Tiene la nariz pequeña?']

ojos_marrones       = [  1  ,   1   ,  0  ,  1  ,   1  ,   0    ,   1   ,  1   ,   1    ,    1    ,   0    ,   1   ,   1    ,   1   ,  1   ,  1  ,    1    ,   0   ,  1   ,   1   ,  1   ,   1    ,    1    ,   1     ],['Tiene los ojos marrones?']
ojos_azules         = [  0  ,   0   ,  1  ,  0  ,   0  ,   1    ,   0   ,  0   ,   0    ,    0    ,   1    ,   0   ,   0    ,   0   ,  0   ,  0  ,    0    ,   1   ,  0   ,   0   ,  0   ,   0    ,    0    ,   0     ],['Tiene los ojos azules?']

boca_pequeña        = [  0  ,   0   ,  1  ,  1  ,   1  ,   0    ,   1   ,  1   ,   1    ,    1    ,   1    ,   1   ,   0    ,   0   ,  1   ,  1  ,    0    ,   0   ,  0   ,   1   ,  0   ,   0    ,    0    ,   0     ],['Tiene la boca pequeña?']
boca_grande         = [  1  ,   0   ,  0  ,  0  ,   0  ,   0    ,   0   ,  0   ,   0    ,    0    ,   0    ,   0   ,   1    ,   0   ,  0   ,  0  ,    0    ,   1   ,  1   ,   0   ,  1   ,   0    ,    0    ,   1     ],['Tiene la boca grande?']

labios_gruesos      = [  1  ,   1   ,  0  ,  0  ,   0  ,   0    ,   0   ,  0   ,   0    ,    0    ,   0    ,   0   ,   0    ,   0   ,  0   ,  0  ,    0    ,   1   ,  1   ,   0   ,  0   ,   0    ,    0    ,   1     ],['Tiene los labios gruesos?']

cejas_gruesas       = [  0  ,   0   ,  0  ,  0  ,   0  ,   0    ,   0   ,  0   ,   0    ,    0    ,   0    ,   1   ,   0    ,   0   ,  1   ,  0  ,    0    ,   1   ,  0   ,   0   ,  0   ,   1    ,    0    ,   0     ],['Tiene las cejas gruesas?']
cejas_finas         = [  0  ,   0   ,  0  ,  0  ,   0  ,   0    ,   0   ,  0   ,   0    ,    1    ,   0    ,   0   ,   0    ,   0   ,  0   ,  0  ,    1    ,   0   ,  0   ,   1   ,  0   ,   0    ,    0    ,   0     ],['Tiene las cejas finas?']

sombrero            = [  0  ,   0   ,  0  ,  0  ,   0  ,   0    ,   0   ,  0   ,   1    ,    1    ,   0    ,   0   ,   1    ,   0   ,  0   ,  0  ,    0    ,   0   ,  0   ,   1   ,  1   ,   0    ,    0    ,   0     ],['Lleva sombrero?']
gorra               = [  0  ,   0   ,  0  ,  0  ,   0  ,   0    ,   0   ,  0   ,   0    ,    0    ,   0    ,   0   ,   0    ,   0   ,  0   ,  0  ,    0    ,   0   ,  0   ,   0   ,  1   ,   0    ,    0    ,   0     ],['Lleva gorra?']
gafas               = [  0  ,   0   ,  1  ,  1  ,   0  ,   0    ,   0   ,  0   ,   1    ,    0    ,   0    ,   0   ,   0    ,   0   ,  1   ,  1  ,    0    ,   0   ,  0   ,   0   ,  0   ,   0    ,    0    ,   0     ],['Lleva gafas?']
pendientes          = [  0  ,   0   ,  0  ,  0  ,   1  ,   0    ,   0   ,  0   ,   0    ,    0    ,   0    ,   0   ,   0    ,   0   ,  0   ,  0  ,    0    ,   0   ,  0   ,   1   ,  0   ,   0    ,    0    ,   0     ],['Lleva pendientes?']

orejas_grandes      = [  1  ,   0   ,  0  ,  0  ,   0  ,   1    ,   0   ,  1   ,   0    ,    0    ,   1    ,   0   ,   0    ,   1   ,  1   ,  0  ,    1    ,   0   ,  1   ,   0   ,  0   ,   0    ,    1    ,   1     ],['Tiene las orejas grandes?']

bigote              = [  1  ,   0   ,  0  ,  0  ,   0  ,   0    ,   0   ,  0   ,   0    ,    0    ,   1    ,   0   ,   0    ,   0   ,  0   ,  0  ,    0    ,   0   ,  1   ,   0   ,  0   ,   0    ,    1    ,   1     ],['Tiene bigote?']
barba               = [  0  ,   0   ,  0  ,  0  ,   0  ,   0    ,   0   ,  1   ,   0    ,    0    ,   1    ,   0   ,   0    ,   1   ,  0   ,  0  ,    1    ,   0   ,  0   ,   0   ,  0   ,   0    ,    1    ,   0     ],['Tiene barba?']

cara_alargada       = [  0  ,   0   ,  1  ,  0  ,   0  ,   1    ,   0   ,  0   ,   0    ,    0    ,   0    ,   0   ,   0    ,   0   ,  0   ,  0  ,    0    ,   0   ,  0   ,   0   ,  0   ,   0    ,    1    ,   0     ],['Tiene la cara alargada?']
cara_triste         = [  0  ,   0   ,  0  ,  0  ,   0  ,   1    ,   0   ,  0   ,   0    ,    0    ,   0    ,   0   ,   1    ,   0   ,  0   ,  0  ,    0    ,   0   ,  0   ,   0   ,  0   ,   0    ,    0    ,   0     ],['Tiene cara triste?']
mejillas_sonrosadas = [  0  ,   1   ,  0  ,  0  ,   0  ,   1    ,   1   ,  1   ,   0    ,    0    ,   0    ,   0   ,   0    ,   0   ,  0   ,  0  ,    1    ,   0   ,  0   ,   0   ,  0   ,   0    ,    0    ,   0     ],['Tiene las mejillas sonrosadas?']

lista_preguntas =[mujer, hombre, pelirrojo, pelo_castaño, pelo_rubio, pelo_negro, pelo_blanco, raya_al_lado, raya_al_medio, calva, pelo_largo, pelo_corto, nariz_grande, nariz_pequeña, ojos_marrones,
                  ojos_azules, boca_pequeña, boca_grande, labios_gruesos, cejas_gruesas, cejas_finas, sombrero, gorra, gafas, pendientes, orejas_grandes, bigote, barba, cara_alargada, cara_triste,
                  mejillas_sonrosadas]

def levantaTablero():
    '''
    Al iniciar la partida cargamos todos los personajes en memoria los cuales
    iremos descartando a lo largo de la partida.

    Return:
        list: lista de personajes
    '''
    tablero = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    return tablero

def preguntaIa(personajes, pregunta_inicial = False):
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
    for a in lista_preguntas:
        # Vemos cuntos de los personejes en juego tienen la característica de cada pregunta.
        b = np.array(personajes) * np.array(a[0])
        # Almacenamos una lista con el resultado de todas las preguntas.
        num_carac.append((b == 1).sum())

    # Lo ideal es elegir una pregunta que descarte la mitad de los personajes en juego. Si no 
    # es posible elegiremos la mas cercana a la mitad.
    numPersonajes = (np.array(personajes) == 1).sum()
    print(f'num personaxes {numPersonajes}')
    mitadPersonajes = numPersonajes//2
    aryDiferencial = np.absolute(num_carac - mitadPersonajes)
    indiceCercano = aryDiferencial.argmin()
    valorCercano = num_carac[indiceCercano]

    print(f'ary direfencia {aryDiferencial}')
    print(f'valorCercano {valorCercano}')

    print(lista_preguntas[indiceCercano])

    print(num_carac)
    aryPregunta = np.array(lista_preguntas[indiceCercano][0])
    pregunta = lista_preguntas[indiceCercano][1]

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
        # Cambiamos 0 po 1 e 1 por 0
        aryPregunta[aryPregunta == 1] = 2
        aryPregunta[aryPregunta == 0] = 1
        aryPregunta[aryPregunta == 2] = 0

    tablero = tablero * aryPregunta



    return tablero

def personajesVivos(tablero):
    '''
    Muestra los personajes que quedan en juego.
    '''
    for a in range(len(personajes)):
        if tablero[a] == 1:
            print(personajes[a])

def main():

    # Levantamos el tablero y damos comienzo a la partida
    tablero = levantaTablero()

    for a in range(6):
        aryPregunta, pregunta = preguntaIa(tablero)

        print(pregunta)
        print('s ou n:')
        resposta = input()

        print(tablero)
        tablero = descartaPersonejes(tablero, aryPregunta, resposta)
        print(tablero)
        personajesVivos(tablero)
        numPersonajes = (np.array(tablero) == 1).sum()
        if numPersonajes == 1:
            print(f'El personaje es')
            personajesVivos(tablero)
            break

if __name__ == "__main__":
    main()
