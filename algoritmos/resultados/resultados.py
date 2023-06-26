import os
import pandas as pd


#ARCHIVOS

carpeta_datos = "G:/Mi unidad/4 curso/Universidad/TFG/GITHUB/TFG-main/algoritmos/datos"
archivos = [os.path.join(carpeta_datos, archivo) for archivo in os.listdir(carpeta_datos) if os.path.isfile(os.path.join(carpeta_datos,archivo))]
archivos.remove('G:/Mi unidad/4 curso/Universidad/TFG/GITHUB/TFG-main/algoritmos/datos\\read.txt')
archivos

# Ruta a la carpeta principal
ruta_principal = "G:/Mi unidad/4 curso/Universidad/TFG/GITHUB/TFG-main/algoritmos"
os.chdir(ruta_principal) # Trabajamos carpeta principal

from funcionesdef import*

#Activar cuando se vayan a usar
#from combinacion_libre_geo import algoritmo as alg_geo
#from combinacion_libre_io import algoritmo as alg_io
from regresion2 import algoritmo as alg_reg
from filtropromedio import algoritmo as alg_fil
from polinomio import algoritmo as alg_pol
from polinomio2 import algoritmo as alg_pol2
from clustering import algoritmo as alg_clus
############## Datos a utilizar sobre archivos[0]
#l1 = L1(archivos[0])
#l2 = L2(archivos[0])
#geo = f1menosf2(l1,l2)
#io = combinacion_libre_ios(l1,l2)

#SELECCIÓN DE ARCHIVO
#filename =  archivos[1]



#CALCULADOR DE DATOS


##############Datos para todos los satélites

def resultados_pol( algoritmo,tiempo, multiplo, filename=filename ):
    D={}
    
    sats = Satelites(filename)
    for i in sats:
        
        datos = L2(filename, i)
        saltos = eval(algoritmo)(datos,10,multiplo,tiempo)
        D[i]= saltos
    return D

def resultados_geo( algoritmo,tiempo, filename=filename ):
    D={}
    
    sats = Satelites(filename)
    for i in sats:
        l1 = L1(filename , i)
        l2 = L2(filename, i)
        datos = f1menosf2(l1,l2)
        saltos = eval(algoritmo)(datos,10,3,tiempo)
        D[i]= saltos
    return D


def resultados_io(algoritmo,tiempo, filename=filename):
    D={}
    sats = Satelites(filename)
    for i in sats:
        l1 = L1(filename , i)
        l2 = L2(filename, i)
        datos = combinacion_libre_ios(l1,l2)
        saltos = eval(algoritmo)(datos,10,3,tiempo)
        D[i]= saltos
    return D

def resultados_reg(algoritmo,tiempo, filename):
    D={}
    sats = Satelites(filename)
    for i in sats:
        #l1 = L1(filename , i)
        datos = L2(filename, i)
        #datos = f1menosf2(l1,l2)
        saltos = eval(algoritmo)(datos,10,tiempo)
        D[i]= saltos
    return D

####################Datos para todas los tamaño de ventanas

def resultados_clustering(filename, algoritmo, datos_por_paso, tiempo):
    D={}
    
    sats = Satelites(filename)
    for i in sats:
        l1 = L1(filename,i)
        l2 = L2(filename, i)
        datos = f1menosf2(l1,l2)
        salto = eval(algoritmo)(datos, datos_por_paso, tiempo)
        D[i]= salto
    return D

#seleccion = 0, datos= datos, window_size = 10, multiplo = 2 , tiempo = 1
def resultados_fil( seleccion, algoritmo,tiempo,multiplo, filename=filename ):
    D={}
    
    sats = Satelites(filename)
    for i in sats:
        l1 = L1(filename , i)
        l2 = L2(filename, i)
        datos = f1menosf2(l1,l2)
        saltos = eval(algoritmo)(seleccion, datos, 10, multiplo, tiempo)
        D[i]= saltos
    return D      


def resultados_fil2(numero_alg,algoritmo,tiempo,multiplo, filename):
    D={}
    #sat = 'G19'#Contiene grandes brechas de datos
    sat = 'G26'# 10 y 20 para MAD el otro regular
    #sat ='G27'
    l1 = L1(filename,sat)
    for i in range(5,100,5):
        saltos = eval(algoritmo)(numero_alg,l1,i,multiplo,30)
        D[str(i)] = saltos
        
    return D

#Meter diccionario
def generar_tabla(saltos_ciclo, name):
        
    # Directorio donde quieres guardar el archivo
    directorio_destino ="G:/Mi unidad/4 curso/Universidad/TFG/GITHUB/TFG-main/algoritmos/resultados"
    
    # Cambia al directorio de destino
    os.chdir(directorio_destino)
    #saltos_ciclo = resultados(filename)
    max_length = max(len(saltos) for saltos in saltos_ciclo.values())

# Rellenar las listas con NaN hasta tener la misma longitud
    saltos_ciclo = {satelite: saltos + [float('nan')] * (max_length - len(saltos)) for satelite, saltos in saltos_ciclo.items()}

# Crear DataFrame con las listas de distintas longitudes
    df_saltos = pd.DataFrame(saltos_ciclo)
     
    df_saltos.to_csv(name, index=False)






########Graficacion datos



####EXTRA
# Rutas a las subcarpetas por si fuera necesario
#subcarpeta1 = os.path.join(ruta_principal, "subcarpeta1")
#subcarpeta2 = os.path.join(ruta_principal, "subcarpeta2")
#

#print("Directorio actual:", os.getcwd())
#
## Cambiar al directorio de la subcarpeta 2
#os.chdir(subcarpeta2)
#print("Directorio actual:", os.getcwd())
