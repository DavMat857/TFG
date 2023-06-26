import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

carpeta_resultados = "G:/Mi unidad/4 curso/Universidad/TFG/GITHUB/TFG-main/algoritmos/resultados"
csvs = [os.path.join(carpeta_resultados, archivo) for archivo in os.listdir(carpeta_resultados) if os.path.isfile(os.path.join(carpeta_resultados,archivo))]
csvs.remove('G:/Mi unidad/4 curso/Universidad/TFG/GITHUB/TFG-main/algoritmos/resultados\\read.txt')

lista_GRA = ['G:/Mi unidad/4 curso/Universidad/TFG/GITHUB/TFG-main/algoritmos/resultados\\saltos_geo_Gra2.csv', 'G:/Mi unidad/4 curso/Universidad/TFG/GITHUB/TFG-main/algoritmos/resultados\\saltos_io_Gra2.csv']
lista_VIGO = ['G:/Mi unidad/4 curso/Universidad/TFG/GITHUB/TFG-main/algoritmos/resultados\\saltos_geo_Vigo.csv','G:/Mi unidad/4 curso/Universidad/TFG/GITHUB/TFG-main/algoritmos/resultados\\saltos_io_Vigo.csv']
lista_TERU= ["G:/Mi unidad/4 curso/Universidad/TFG/GITHUB/TFG-main/algoritmos/resultados\\saltos_fil_TERU1.csv","G:/Mi unidad/4 curso/Universidad/TFG/GITHUB/TFG-main/algoritmos/resultados\\saltos_fil_TERU2.csv","G:/Mi unidad/4 curso/Universidad/TFG/GITHUB/TFG-main/algoritmos/resultados\\saltos_fil_TERU3.csv","G:/Mi unidad/4 curso/Universidad/TFG/GITHUB/TFG-main/algoritmos/resultados\\saltos_fil_TERU4.csv"]
lista_TERU2= ["G:/Mi unidad/4 curso/Universidad/TFG/GITHUB/TFG-main/algoritmos/resultados\\saltos_fil_TERU13MAD.csv","G:/Mi unidad/4 curso/Universidad/TFG/GITHUB/TFG-main/algoritmos/resultados\\saltos_fil_TERU13sigma.csv"]
lista_MAD = ["G:/Mi unidad/4 curso/Universidad/TFG/GITHUB/TFG-main/algoritmos/resultados\\Mad1_polinomial.csv","G:/Mi unidad/4 curso/Universidad/TFG/GITHUB/TFG-main/algoritmos/resultados\\Mad1_regresion.csv"]
#######Diccionarios
def graficar_dict(diccionario):
    # Crear una lista para almacenar los satélites y los instantes
    satelites = []
    instantes = []

    # Recorrer el diccionario
    for satelite, valores in diccionario.items():
        satelites.extend([satelite] * len(valores))
        instantes.extend(valores)

    # Crear el gráfico de dispersión
    plt.scatter(instantes, satelites, marker='.')

    # Configurar etiquetas y título
    plt.xlabel("Tiempo en segundos")
    plt.ylabel("Satélites")
    plt.title("Representación de los saltos de ciclo de todos los satélites")

    # Mostrar el gráfico
    plt.show()

    

#######CSVS

def graficar(csv):#graficar(csvs[1])
    dataframe = pd.read_csv(csv)
        
    # Obtener los nombres de las columnas
    columnas = dataframe.columns.tolist()
       
    # Crear una lista para almacenar los satélites y los instantes
    satelites = []
    instantes = []
        
    # Recorrer las columnas del dataframe
    for columna in columnas:
        satelites.extend([columna] * len(dataframe[columna]))
        instantes.extend(dataframe[columna])
        
    # Crear el gráfico de dispersión
    plt.scatter(instantes, satelites, marker='.')
        
    # Configurar etiquetas y título
    plt.xlabel("Tiempo en segundos")
    plt.ylabel("Satélites")
    plt.title("Representación de los saltos de todos los satélites")
        
    # Mostrar el gráfico
    plt.show()

#Si los quiero superponer entonces plt.show() lo separo
def graficar_lista(csvs):#graficar_lista(lista)
    for i in csvs:
        dataframe = pd.read_csv(i)
        
        # Obtener los nombres de las columnas
        columnas = dataframe.columns.tolist()
        
        # Crear una lista para almacenar los satélites y los instantes
        satelites = []
        instantes = []
        
        # Recorrer las columnas del dataframe
        for columna in columnas:
            satelites.extend([columna] * len(dataframe[columna]))
            instantes.extend(dataframe[columna])
        
        # Crear el gráfico de dispersión
        plt.scatter(instantes, satelites, marker='.')
        
        # Configurar etiquetas y título
        plt.xlabel("Tiempo en segundos")
        plt.ylabel("Satélites")
        plt.title("Representación de los saltos de todos los satélites")
        
    # Mostrar el gráfico
        plt.show()