"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    valores_por_letra = {}
    with open("files/input/data.csv", 'r') as archivo:
            for linea in archivo:
                columnas = linea.strip().split('\t')
                letra = columnas[0]
                valor = int(columnas[1])

                if letra in valores_por_letra:
                    valores_por_letra[letra]['max'] = max(valores_por_letra[letra]['max'], valor)
                    valores_por_letra[letra]['min'] = min(valores_por_letra[letra]['min'], valor)
                else:
                    valores_por_letra[letra] = {'max': valor, 'min': valor}

    resultado = [(letra, datos['max'], datos['min']) for letra, datos in sorted(valores_por_letra.items())]
    return resultado
pregunta_05()
