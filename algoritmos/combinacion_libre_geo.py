import numpy as np
from funcionesdef import*


#Datos a utilizar
filename = "datos/MAD1047A00.23O"
sat = 'G10'
datos = all_information2(filename)
l1 = L1(filename, sat)
l2 = L2(filename, sat)
geo = f1menosf2(l1,l2)#L1-L2
numero_muestras = 10
    

#Algoritmo
def algoritmo(datos = geo,numero_muestras=numero_muestras,multiplo=3, tiempo=30):
     
    graf_datos(datos, "Algoritmo_geometria",tiempo)
    media,std = selector_umbral(datos,numero_muestras)#calculamos la media por si fuera necesaria en el umbral
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
        
       
        if claves[len(claves)-1]- claves[0] <= 30:
          
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

