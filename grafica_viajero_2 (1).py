# ruta de paises #https://es.acervolima.com/como-trazar-una-curva-suave-en-matplotlib/
# x = np.array([madrid[0],viena[0],roma[0]] ) #x de las distintas ciudades
# y = np.array([madrid[1],viena[1],roma[1]])  #y de las distintas ciudades
# plt.plot(x, y)

# puntos coordenadas = paises

# ax = plt.subplot()
# mad = ax.plot([89.], [37.], "gs")
# vie = ax.plot([15.], [28.], "ms")
# rom = ax.plot([5.], [8.], "cs")


# from cProfile import label
# from re import X
# import numpy as np
import matplotlib.pyplot as plt
import array as arr

listaciudades = ["Newyork", "Madrid", "Berlin"]
coordenadas = [[89, 37], [15, 28], [5, 8]]

def permutations(lista):
    viajes = []

    def permutatate(lista, final=[]):
        if len(lista) == 0:
            viajes.append(final)
        else:
            for i in range(len(lista)):
                permutatate(lista[:i] + lista[i+1:], final + lista[i:i+1])

    permutatate(lista)

    return viajes


def mapa_coordenadas(coords):

    def mapa_lineas(coords):
        contador = 0
        x_array = []
        y_array = []
        while contador < len(coords):
            x_array.append(coords[contador][0])
            y_array.append(coords[contador][1])
            contador += 1
        # x = np.array(x_array)
        # y = np.array(y_array)
        x = arr.array('i', x_array)
        y = arr.array('i', y_array)        
        plt.plot(x, y)

    def mapa_ciudades(coords):
        contador = 0
        ax = plt.subplot()
        while contador < len(coords):
            ax.plot([coords[contador][0]], [coords[contador][1]], 'o')
            contador += 1

    mapa_lineas(coords)
    mapa_ciudades(coords)

    plt.legend(['Ruta'] + listaciudades)
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.show()


if __name__ == "__main__":
    print("estoy aqui")
    viajes = permutations(coordenadas)
    for viaje in viajes:
        mapa_coordenadas(viaje)
