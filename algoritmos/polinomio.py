
import numpy as np
from funcionesdef import*

#Método 1

#Datos a utilizar
filename = "datos/MAD1047A00.23O"
sat = 'G10'
datos = all_information2(filename)
l1 = L1(filename, sat)
numero_muestras = 10

#Algoritmo
def algoritmo(datos = l1,numero_muestras=numero_muestras,multiplo=3, tiempo=30):
     
    graf_datos(datos, "Algoritmo_geometria",tiempo)
    media,std = selector_umbral(datos,numero_muestras)
    #umbral = media + std
    umbral = std * multiplo
    resultados = alg_sacar_saltos(datos,numero_muestras,umbral)
    resultados = [i for i in resultados if i!=0]
    resultados = list(map(lambda x: x*tiempo,resultados))
    return resultados

#Funciones auxiliares

def selector_umbral(datos : dict,numero_muestras):
   
    errores_totales = np.array([])
    
    e = []
    for i in range(0,len(datos),numero_muestras):
        
        
        clave_items = list(datos.items())[i:i + numero_muestras]
        claves = [i[0] for i in clave_items]
        valores = [i[1] for i in clave_items]
        degree = 2
        
        coeffs = np.polyfit(claves,valores,degree)
        p  = np.poly1d(coeffs)
        pol = [p(n) for n in claves]
        
       
        if claves[len(claves)-1]- claves[0] > 30:
          #print(f"Salto de ciclo entre {claves[0]} y {claves[len(claves)-1]} por brecha de datos")
          pass
        else:
            valor_real = np.array(valores)
            valor_pol = np.array(pol)
            error = np.abs(valor_real - valor_pol)
            e.append(list(error))
            errores_totales = np.concatenate((errores_totales,error))
            

    media = np.mean(errores_totales)
    std = np.std(errores_totales)
    
    return media,std

def alg_sacar_saltos(datos,numero_muestras,umbral): 
    saltos = []
    
    for i in range(0,len(datos),numero_muestras):
    
        clave_items = list(datos.items())[i:i + numero_muestras]
        claves = [i[0] for i in clave_items]
        valores = [i[1] for i in clave_items]
        degree = 2
        
        coeffs = np.polyfit(claves,valores,degree)
        p  = np.poly1d(coeffs)
        pol = [p(n) for n in claves]
        
        if claves[len(claves)-1]- claves[0] > 30:
          saltos.append(claves[0])
        else:
            valor_real = np.array(valores)
            valor_pol = np.array(pol)
            error = np.abs(valor_real - valor_pol)

            for j in range(0,len(error)-1,1):
                if error[j]  > umbral:
                    saltos.append(claves[j])
                else:
                     saltos.append(0)
                     
    return np.array(saltos)
