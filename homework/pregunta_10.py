"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    resultado = []
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for linea in file:
            letra = linea.strip().split("\t")[0]
            elementos_col4 = linea.strip().split("\t")[3].split(",")
            cantidad_col4 = len(elementos_col4)
            elementos_col5 = linea.strip().split("\t")[4].split(",")
            cantidad_col5 = len(elementos_col5)
            resultado.append((letra, cantidad_col4, cantidad_col5))
    return resultado

pregunta_10()