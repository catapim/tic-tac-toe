""" tic tac toe """
import sys
import collections

""" esta matriz corresponde al tablero de juego y la funcion creacion_tablero la recibe como parametro """
MATRIZ_TABLERO = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

def creacion_tablero(tablero):
    """ construccion del tablero en la terminal """
    print("|%s|%s|%s|" % (tablero[0][0], tablero[0][1], tablero[0][2]))
    print("|%s|%s|%s|" % (tablero[1][0], tablero[1][1], tablero[1][2]))
    print("|%s|%s|%s|" % (tablero[2][0], tablero[2][1], tablero[2][2]))
    return tablero

def valida_empate(function):
    """ este decorador mira el tablero y solo si hay empate retorna mensaje y finaliza juego """
    def wrap (*args, **kwargs):
        cantidad_x = sum(row.count('X') for row in tablero)
        cantidad_o = sum(row.count('O') for row in tablero)       
        if cantidad_x == 5 and cantidad_o == 4:
            print('Hay empate... fin del juego')
            sys.exit()
        elif cantidad_x == 4 and cantidad_o == 5:
            print('Hay empate... fin del juego')
            sys.exit()
        return function(*args, **kwargs)
    return wrap


def valida_ganador(funcion):
    """ decorador que recibe el tablero y siempre está revisando si se cumple alguna condicion considerada como ganadora """
    """ todas las combinaciones ganadoras se listan a continuacion """
    def wrap(*args, **kwargs):
        # diagonal
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != '_' and tablero[1][1] != '_' and tablero[2][2] != '_':
            indica_ganador(tablero[0][0])
        # diagonal
        elif tablero[2][0] == tablero[1][1] == tablero[0][2] and tablero[2][0] != '_' and tablero[1][1] != '_' and tablero[0][2] != '_':
            indica_ganador(tablero[2][0])
        # horizontal
        elif tablero[0][0] == tablero[0][1] == tablero[0][2] and tablero[0][0] != '_' and tablero[0][1] != '_' and tablero[0][2] != '_':
            indica_ganador(tablero[0][0])
        # horizontal    
        elif tablero[1][0] == tablero[1][1] == tablero[1][2] and tablero[1][0] != '_' and tablero[1][1] != '_' and tablero[1][2] != '_':
            indica_ganador(tablero[1][0])
        # horizontal
        elif tablero[2][0] == tablero[2][1] == tablero[2][2] and tablero[2][0] != '_' and tablero[2][1] != '_' and tablero[2][2] != '_':
            indica_ganador(tablero[2][0])
        # vertical
        elif tablero[0][0] == tablero[1][0] == tablero[2][0] and tablero[0][0] != '_' and tablero[1][0] != '_' and tablero[2][0] != '_':
            indica_ganador(tablero[0][0])
        # vertical 
        elif tablero[0][1] == tablero[1][1] == tablero[2][1] and tablero[0][1] != '_' and tablero[1][1] != '_' and tablero[2][1] != '_':
            indica_ganador(tablero[0][1])
        # vertical 
        elif tablero[0][2] == tablero[1][2] == tablero[2][2] and tablero[0][2] != '_' and tablero[1][2] != '_' and tablero[2][2] != '_':
            indica_ganador(tablero[0][2])
        else:
            pass
        return funcion(*args, **kwargs)
    return wrap        

def indica_ganador(indice):
    """ esta funcion recibe el indice del simbolo ganador y cierra el juego con sys.exit() """
    """ se le pasa como indice el primer parámetro dentro de la formacion ganadora """
    print('Felicidades! Ha ganado el símbolo: ', indice)
    sys.exit()

@valida_empate
@valida_ganador
def input_jugador(turno_x):
    """ funcion para que el jugador ingrese fila y columna donde quiere ingresar el simbolo que le corresponde """
    """ tambien valida que no se pueda jugar en un campo ocupado """
    jugada_row = input('Ingresa la FILA donde escribirás tu símbolo (del 0 al 2): ')
    jugada_col = input('Ingresa la COLUMNA donde escribirás tu símbolo (del 0 al 2): ')
    if tablero[int(jugada_row)][int(jugada_col)] == '_':
        tablero[int(jugada_row)][int(jugada_col)] = simbolo_turno
        return 0
    else:
        print('No puedes escribir aqui...')
        return 1

""" variable que si es True, ingresa X al tablero, de lo contrario ingresa O """
turno_x = True

while True:
    if turno_x:
        simbolo_turno = "X"
    else:
        simbolo_turno = "O"
    tablero = creacion_tablero(MATRIZ_TABLERO)
    print('Turno de: ', simbolo_turno)
    res = input_jugador(turno_x)
    if res == 0:
        turno_x = not turno_x