import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn import metrics
from funcionesdef import*

#Datos a utilizar
filename = "datos/TERU042A00.23O"
sat = 'G24'
datos= L1(filename,sat)
datos_por_paso = 35


#Algoritmo
def algoritmo(datos=datos,datos_por_paso=datos_por_paso,tiempo=30): 
    graf_datos(datos,"Algoritmo_clustering",tiempo)
    for i in range(0,len(datos),datos_por_paso):
        print("RANGO entre" , i*tiempo , (i+datos_por_paso)*tiempo)
        DBS(datos,i,i+datos_por_paso,tiempo)
    

#Funciones auxiliares

def DBS(frec ,rango_min,rango_max,tiempo):
    valores = seleccion_umbral(frec,rango_min,rango_max,tiempo) #valores[0] me da el eps y valores[1] me da std
    if valores:
        grafica_DBSCAN(frec ,2 ,valores[0]+1*valores[1],rango_min,rango_max,tiempo) #Sumarle dos veces la desviación típica


        
def seleccion_umbral(frec,rango_min,rango_max,tiempo,n=3):
    
    infor = list(frec.items())[rango_min:rango_max]
    infor = [[i[0]*tiempo,i[1]] for i in infor]
    infor = np.array(infor)
    brecha_datos = np.diff(infor,axis=0)
    if max(brecha_datos[:,0])<3*tiempo: 
    
        phase_diff = np.diff(infor, axis = 0) 
        phase_diff = np.linalg.norm(phase_diff,axis = 1)
        std = np.std(phase_diff)
        
        phase_diff_abs = [abs(i) for i in phase_diff]
        
        eps1 = seleccion_eps(infor,n,min(phase_diff_abs), max(phase_diff_abs))
        return eps1, std
    else:
        print("SALTO DE CICLO")
        

def seleccion_eps(datos ,n, minimo,maximo):
    

    eps = np.linspace(minimo,maximo, num=1000)
    
    sil = []
    for i in eps:
        db = DBSCAN(eps=i, min_samples=n, metric='euclidean').fit(datos)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        labels = db.labels_
        if len(set(labels))> 1:
            sil.append(metrics.silhouette_score(datos, labels))
        else:
            sil.append(0)
    maximo = max(sil)
    indice = sil.index(maximo)
    return eps[indice]

def grafica_DBSCAN(frec ,n ,eps,rango_min,rango_max,tiempo):
    
    
    infor = list(frec.items())[rango_min:rango_max]
    infor = [[i[0]*tiempo,i[1]] for i in infor]
    infor = np.array(infor) 
    
    epsoptimo = eps 
    
    db = DBSCAN(eps=epsoptimo, min_samples=n, metric='euclidean').fit(infor)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_
        
    
    #SOLO GRAFICAR
    unique_labels = set(labels)
    print(unique_labels)
    if len(unique_labels)>1:
        
        colors = [plt.cm.Spectral(each)
                for each in np.linspace(0, 1, len(unique_labels))]
        
        plt.figure(figsize=(8,4))
        for k, col in zip(unique_labels, colors):
            if k == -1:
                # Negro usado para ruido
                col = [0, 0, 0, 1]
        
            class_member_mask = (labels == k)
        
            xy = infor[class_member_mask & core_samples_mask]
            plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                    markeredgecolor='k', markersize=5)
        
            xy = infor[class_member_mask & ~core_samples_mask]
            plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                    markeredgecolor='k', markersize=3)
        plt.title('Estimated number of DBSCAN clusters: %d' % (len(unique_labels - {-1})))
        plt.show()
    
    