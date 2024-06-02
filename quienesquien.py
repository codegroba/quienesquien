'''
Creamos una base de datos temporal en python.
'''
Personaxes          = ['Max','Susan','Tom','Sam','Anne','Robert','Anita','Bill','Claire','Bernard','Alfred','Frans','George','David','Paul','Joe','Phillip','Peter','Alex','Maria','Eric','Herman','Richard','Charles']

mujer               = [  0  ,   1   ,  0  ,  0  ,   1  ,   0    ,   1   ,  0   ,   1    ,    0    ,   0    ,   0   ,   0    ,   0   ,  0   ,  0  ,    0    ,   0   ,  0   ,   1   ,  0   ,   0    ,    0    ,   0     ],['Es mujer?']
hombre              = [  1  ,   0   ,  1  ,  1  ,   0  ,   1    ,   0   ,  1   ,   0    ,    1    ,   1    ,   1   ,   1    ,   1   ,  1   ,  1  ,    1    ,   1   ,  1   ,   0   ,  0   ,   1    ,    1    ,   1     ],['Es hombre?']

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
mejillas sonrosadas = [  0  ,   1   ,  0  ,  0  ,   0  ,   1    ,   1   ,  1   ,   0    ,    0    ,   0    ,   0   ,   0    ,   0   ,  0   ,  0  ,    1    ,   0   ,  0   ,   0   ,  0   ,   0    ,    0    ,   0     ],['Tiene las mejillas sonrosadas?']


def levantaTablero():
    '''
    Al iniciar la partida cargamos todos los personajes en memoria los cuales
    iremos descartando a lo largo de la partida.

    Return:
        list: lista de personajes
    '''
    return personajes

def preguntaIa(personajes, pregunta_inicial = False):
    '''
    Le pasaremos los personajes que quedan en juego y nos dara la pregunta
    que debemos realizar.

    Args:
        personejes (list): lista de personajes que siguen en el juego.
        pregunta_inicial (bool): Evita pregunta inicial hombre o mujer.

    Returns:
        str: retorna la pregunta a realizar.
    '''

    # Temos que consultar todas as preguntas e ver cal facemos.
    return ""

def descartaPersonejes(personajes, pregunta, s/n):
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
    return personajes


def main():

    # Levantamos el tablero y damos comienzo a la partida
    tablero = levantaTablero()
    # Necesitamos una memoria para no preguntar si es hombre o mujer al inicio
    pregunta_inicial = True
    # Preguntaremos que personaje quiere seleccionar
    print("Que personeje quiere ser?:")
    print(tablero)


    for a in range(6):
        pregunta = preguntaIa(tablero, pregunta_inicial)
        print(pregunta)
        pregunta_inicial = False
        # Esperamos a resposta
        tablero = descartaPersonajes(tablero, pregunta, respuesta)
        # Evaluamos si solo queda uno y acabamos
        if len(tablero) == 1:
            break

    # Evaluamos si solo queda uno o tenemos que elegir


if __name__ == "__main__":
    main()
