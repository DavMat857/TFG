from funcionesdef import*
import numpy as np

#Método 1 tuve que cambiar el umbral porque duplicada la cantidad de saltos

#Datos a utilizar
filename = "datos/MAD1047A00.23O"
sat = 'G10'
datos = all_information2(filename)

l2 = L2(filename, sat)

numero_muestras = 10
    

#Algoritmo
def algoritmo(datos = l2,numero_muestras=numero_muestras,multiplo=1, tiempo = 30):
     
    graf_datos(datos, "Algoritmo_polinomial", tiempo)
    resultados = alg_sacar_saltos(datos,numero_muestras,multiplo)
    resultados = list(map(lambda x: x*tiempo, resultados))
    return resultados


#Funciones auxiliares
def alg_sacar_saltos(datos,numero_muestras,multiplo): 
    saltos = []
    i = 1
    
    claves = [int(i) for i in list(datos.keys())]
    valores = list(datos.values())
    #Primer polinomio
    saltos += crear_pol(claves[0:numero_muestras],valores[0:numero_muestras])
    while i<len(datos) - numero_muestras :
    #for i in range(0,len(datos),numero_muestras):
        
        if claves[i]- claves[i-1] > 30:
          saltos.append(claves[i])
          i=i+1
          saltos+= crear_pol(claves[i:i+numero_muestras],valores[i:i+numero_muestras])
        
        else:
            
            
            if crear_pol(claves[i:i+numero_muestras],valores[i:i+numero_muestras])!=[]:

                saltos+= crear_pol(claves[i:i+numero_muestras],valores[i:i+numero_muestras])

                i=i+numero_muestras
            else:
                
                i=i+1            
    return np.array(saltos)


def crear_pol(claves,valores):
    saltos = []
    degree = 2
        
    coeffs = np.polyfit(claves,valores,degree)
    p  = np.poly1d(coeffs)
    pol = [p(n) for n in claves]
    
    error = [abs(valores[i]-pol[i]) for i in range(len(valores))]
    valor_real = np.array(valores)
    valor_pol = np.array(pol)
    error = np.abs(valor_real - valor_pol)
    #umbral = np.mean(error) + np.std(error)
    umbral =  3*np.std(error)
    
    indicador =[i>umbral for i in error ]
    
    for i in range(len(indicador)):
        if indicador[i] == True:
            saltos.append(claves[i])
    
    return saltos




