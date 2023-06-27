
import numpy as np
import matplotlib.pyplot as plt
from funcionesdef import*

#Datos a seleccionar
filename = "datos/TERU042A00.23O"
sat = 'G08'
l1 = L1(filename, sat)
datos = l1

#Algoritmo
#Indicación: 0 para umbral MAD y 1 para umbral STD
def algoritmo(seleccion = 0, datos= datos, window_size = 10, multiplo = 2 , tiempo = 1 ):
    graf_datos(datos,"Algoritmo_filtroPromedio",tiempo)
    saltos = []
    i = 0
    
    claves = list(datos.keys())
    valores = list(datos.values())
    
    moving_average = np.convolve(valores, np.ones(window_size)/window_size, mode='valid')
    
    while i + window_size< len(moving_average):
        
        if i + window_size < len(moving_average):
            brecha = max(np.diff(claves[i:i+window_size]))
            
            if brecha >30:
               saltos.append(claves[i])
               i = i + window_size
            else:
               b = True
               j = i
               if seleccion ==0 : umbral  =multiplo*median_absolute_desviation(valores[i:i+window_size])
               else: umbral  =multiplo*np.std(valores[i:i+window_size])
               
               while b== True and j < i + window_size:     
                
                if np.abs(valores[j]-moving_average[j])> umbral:
                    saltos.append(claves[i])
                    i = i + window_size
                    b = False
            
                else: 
                    j = j + 1
                    
               i = i+1
    saltos = list(map(lambda x: x*tiempo,saltos))
    return saltos

#Funciones auxiliares
def median_absolute_desviation(datos):
    mediana_datos = np.median(datos)
    restas = []
    for i in datos:
        restas.append(np.abs(i-mediana_datos))
    return np.median(restas)
