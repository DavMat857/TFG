from funcionesdef import*
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

import time
import pandas as pd

#Datos a utilizar
filename = "datos/MAD1060R001s.23O"

sat = 'G08'
l1 = L1(filename , sat)
l2 = L2(filename, sat)
datos = f1menosf2(l1,l2)
paso = 10

#Algoritmo        
def algoritmo(datos = datos , paso = paso,tiempo =1):
    graf_datos(datos,"Algoritmo_regresion",tiempo)
    
    claves = np.array(list(datos.keys()))
    valores = np.array(list(datos.values()))
    resultados = []
    
    for i in range(0, len(valores), paso):
        
        if i + paso < len(claves):
            brecha = max(np.diff(claves[i:i + paso]))
           
            if brecha > 30:
                resultados.append(claves[i])
                pass
            else:
                b,salt = dosaux(valores[i:i + paso],claves[i: i +paso])
                
                if b:
                    resultados += salt
    resultados = list(map(lambda x: x*tiempo, resultados))
    return resultados

#Funciones auxiliares
def dosaux(data,claves): # graficar los residuos sin tener en cuenta el nº de observación
   
    saltos = []
    b = False
    data = np.array(data)
    
    
    x = np.arange(data.size).reshape((-1, 1))
    
    model = LinearRegression().fit(x, data)

    residuals = data - model.predict(x) 

    residuals = np.abs( data - model.predict(x))
    media = np.mean((residuals))
    std = np.std(residuals)
    umbral = media + 2*std
    #umbral = 3*std
    condicion = [i >umbral  for i in (residuals)]
    
    if True in condicion:
        b = True
    
        for i in range(len(condicion)):
            if condicion[i]==True:
                saltos.append(claves[i])
    return b, saltos


from sklearn.metrics import r2_score

def r2(valores,estimados):
    r2 = r2_score(valores,estimados)
    return r2    
