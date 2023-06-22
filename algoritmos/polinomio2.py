# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:30:28 2023

@author: David
"""


from funcionesdef import*
import numpy as np

#Método 2 tuve que cambiar el umbral porque todo era salto de ciclo

#Datos a utilizar
filename = "datos/MAD1047A00.23O"
sat = 'G10'
datos = all_information2(filename)

l2 = L2(filename, sat)

numero_muestras = 10
    

#Algoritmo
def algoritmo(datos = l2,numero_muestras=numero_muestras,multiplo=1, tiempo = 30):
     
    graf_datos(datos, "Algoritmo_geometria", tiempo)
    resultados = alg_sacar_saltos(datos,numero_muestras,multiplo)
    resultados = list(map(lambda x: x*tiempo, resultados))
    return resultados


#Funciones auxiliares

"""Introduces datos, numero de muestras por paso y el umbral"""
def alg_sacar_saltos(datos,numero_muestras,multiplo): 
    saltos = []
    i = 1
    
    claves = [int(i) for i in list(datos.keys())]
    valores = list(datos.values())
    #Primer polinomio
    pol, umbral= crear_pol(claves[0:numero_muestras],valores[0:numero_muestras])
    while i<len(datos) - numero_muestras :
    #for i in range(0,len(datos),numero_muestras):
        
        if claves[i]- claves[i-1] > 30:
          saltos.append(claves[i])
          i=i+1
          pol, umbral= crear_pol(claves[i:i+numero_muestras],valores[i:i+numero_muestras])
        
        else:
            valor_real = valores[i]
            valor_pol = pol(claves[i])
            error = np.abs(valor_real - valor_pol)
            
            
            if error  > multiplo*umbral:
                saltos.append(claves[i])
                i=i+numero_muestras
                pol, umbral= crear_pol(claves[i:i+numero_muestras],valores[i:i+numero_muestras])
        
            else:
                
                i=i+1            
    return np.array(saltos)

#Creación de un polinomio
    
def crear_pol(claves,valores):
    
    degree = 2
        
    coeffs = np.polyfit(claves,valores,degree)
    p  = np.poly1d(coeffs)
    pol = [p(n) for n in claves]
    
    error = [abs(valores[i]-pol[i]) for i in range(len(valores))]
    valor_real = np.array(valores)
    valor_pol = np.array(pol)
    error = np.abs(valor_real - valor_pol)
    umbral = np.mean(error) + np.std(error)
    #umbral = 3*np.std(error)
  
    return p,umbral
