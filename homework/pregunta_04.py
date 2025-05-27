"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_04():
    """
    La columna 3 contiene una date en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada month, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    sums = {}

    with open("files/input/data.csv", "r") as file:
        for linea in file:
            columns = linea.split("\t")
            date = columns[2]  
            month = date.split("-")[1] 
            
            if month in sums:
                sums[month] += 1
            else:
                sums[month] = 1

    return sorted(sums.items())

pregunta_04()