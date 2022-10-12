from ast import comprehension
from turtle import color
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as dates

def linea_infer():
    
    color_campo = '#0159bc'
    coord_x = [0, 100]
    coord_y = [0, 0]
    plt.plot(coord_x, coord_y, color_campo)
    #plt.show()

    #Linea gol -izq los puntos (0,0) a (0, 65)
    coord_x = [0, 0]
    coord_y = [0, 65]
    plt.plot(coord_x, coord_y, color_campo)
    #plt.show()

    # Linea superior los puntos (x,y) a(0,65) , b(100, 65)
    coord_x = [0, 100]
    coord_y = [65, 65]
    plt.plot(coord_x, coord_y, color_campo)
    #plt.show()
    # Linea gol-dcha los puntos (100, 0) a (100, 65)
    coord_x = [100, 100]
    coord_y = [0, 65]
    plt.plot(coord_x, coord_y, color_campo)
    # plt.show()
    #Linea central 
    coord_x = [50, 50]
    coord_y = [0, 65]
    plt.plot(coord_x, coord_y, color_campo)

    # Linea area GRANDE izq son tres líneas, esto requiere unir 4 puntos (x, y)
    # requiere de 4 puntos a ir conectando, el formato (x, y) de los puntos sería
    coord_areagrande_izq_x = [0, 16.5, 16.5, 1]
    coord_areagrande_izq_y = [12.34, 12.34, 52.66, 52.66]
    plt.plot(coord_areagrande_izq_x, coord_areagrande_izq_y, color_campo)
    # plt.show()
    ##Linea de area pequeña son tres lineas, requerie unir 4 puntos(x,y)x
    coord_pequeña_izq_x = [0, 5.5, 5.5, 0]
    coord_pequeña_izq_y = [23.34, 23.34, 41.66, 41.66]
    plt.plot(coord_pequeña_izq_x, coord_pequeña_izq_y, color_campo)
    # plt.show()
    ##list comprehension
    coord_areagrande_dcha_x = [abs(c -100) for c in coord_areagrande_izq_x]
    ## coord_areagrande_dcha_x = [100, 83.5, 83.5, 100]
    coord_areagrande_dcha_y = coord_areagrande_izq_y
    plt.plot(coord_areagrande_dcha_x, coord_areagrande_dcha_y, color_campo)

    coord_pequeña_dcha_x = [abs(c -100) for c in coord_pequeña_izq_x]
    coord_pequeña_dcha_y = coord_pequeña_izq_y
    plt.plot(coord_pequeña_dcha_x, coord_pequeña_dcha_y, color_campo)
    
    cicle1 = plt.Circle((50,32.5), radius=9.15, fill= False, color = color_campo)
    plt.gca().add_patch(cicle1)
    #plt.show()

    # Portería izquierda
    port_izq_x = [0,-2.44,-2.44,0]
    port_izq_y = [28.84,28.84,36.16,36.16]
    plt.plot(port_izq_x, port_izq_y, color_campo)

    port_dcha_x = [abs(c -100) for c in port_izq_x]
    port_dcha_y = port_izq_y
    plt.plot(port_dcha_x, port_dcha_y, color_campo)
    
    #Le podemos añadir un titular.

    plt.text(0,-11,'Como pintar un campo de'\
        ' fútbol y jugadores en él'\
            '', fontsize=10, color= color_campo)
    

def pintar_jugador(coor_x: int, coord_y: int, dorsal: int, tamaño: int, color:str):
    icon_player = plt.Circle((coor_x, coord_y), tamaño, fill=True, color=color)
    plt.gca().add_patch(icon_player)
    plt.text(coor_x, coord_y - 0.9, dorsal, fontsize=11, ha='center', color='w')
    
    
def run():
    camp_juego = linea_infer()
    print (camp_juego)

    color_jugador = '#aaaaaa'
    equipo = {'Nacho': {
        'dorsal': 5,
        'pos_x': 12,
        'pos_y': 54,
        },
        'Fran': {
        'dorsal': 12,
        'pos_x': 12,
        'pos_y': 10,
        },
        'Javi': {
        'dorsal': 9,
        'pos_x': 80.5,
        'pos_y': 35.0
        },
        'Fer': {
        'dorsal': 4,
        'pos_x': 45,
        'pos_y': 50
        },
        'Sergio': {
        'dorsal': 8,
        'pos_x': 35,
        'pos_y': 15
        },
        }

    for key, value in equipo.items():
        print("El jugador se llama {0} y sus datos son: {1}".format(key, value))
        pintar_jugador(value['pos_x'], value['pos_y'], value['dorsal'],tamaño=3, color=color_jugador)
        
    plt.show()

if __name__ == '__main__':
    run()
    
    