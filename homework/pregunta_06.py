"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    with open('files/input/data.csv', 'r') as file:
        archivo = csv.reader(file, delimiter='\t')
        diccionario = {}
        for fila in archivo:
            claves=fila[4].split(",")
            for clave in claves:
                codigo=clave.split(":")
                if codigo[0] in diccionario.keys():
                    diccionario[codigo[0]].append(int(codigo[1]))
                else:
                    diccionario[codigo[0]]=[int(codigo[1])]
            
        respuesta=[]
        for clave in diccionario:
            respuesta.append((clave,min(diccionario[clave]),max(diccionario[clave])))
        return sorted(respuesta)
    
pregunta_06()