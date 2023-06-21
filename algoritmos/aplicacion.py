import os
from funcionesdef import*
import tkinter as tk
from tkinter import messagebox, scrolledtext
from combinacion_libre_geo import algoritmo as alg_geo
from combinacion_libre_io import algoritmo as alg_io
from clustering import algoritmo as alg_clus
from regresion2 import algoritmo as alg_reg
from filtropromedio import algoritmo as alg_fil
import threading

carpeta_datos = 'datos'
archivos = [os.path.join(carpeta_datos, archivo) for archivo in os.listdir(carpeta_datos) if archivo.endswith("O") and os.path.isfile(os.path.join(carpeta_datos, archivo))]
Algoritmos = ['alg_geo','alg_io','alg_clus','alg_fil','alg_reg'] # Crear lista funciones
Frecuencias = ['L1','L2','f1menosf2','combinacion_libre_ios']
Pasos = [i for i in range(10,20,1)]
Multiplos = [i for i in range(1,5,1)]
Tiempos = ["uno",30] #Pongo "uno" para que no se confunda con el 1 de Multiplos
Seleccion = ["MAD","sigma"]
Satelites = ['G0'+str(i) for i in range(1,10)]+ ['G'+str(i) for i in range(10,36)]
archivos_alg =["--- Selección ---"]+Seleccion+["--- Archivos ---"]+archivos+["--- Satélites ---"]+ Satelites+["--- Algoritmos ---"]+Algoritmos+["--- Frecuencias ---"]+Frecuencias+["--- Paso ---"]+Pasos+["--- Múltiplo ---"]+Multiplos+["--- Tiempo ---"]+Tiempos

def leer_contenido_archivo(archivo):
    with open(archivo, 'r') as f:
        contenido = f.read()  # Lee todo el contenido del archivo en una sola cadena
    return contenido

informacion = leer_contenido_archivo("datos/read.txt")
informacion2 = leer_contenido_archivo("read.txt")

def mostrar_informacion(elemento,titulo):
    ventana_info = tk.Toplevel(ventana)
    ventana_info.geometry("400x300+200+200")
    ventana_info.title(titulo)
    
    texto_info = scrolledtext.ScrolledText(ventana_info, width=50, height=10)
    texto_info.pack()
    texto_info.insert(tk.INSERT, elemento)
    texto_info.configure(state='disabled')

def obtener_elemento_seleccionado():
    lista_seleccion = lista.curselection()
    
    archivo = None
    algoritmo = None
    frecuencia = None
    paso = None
    multiplo = None
    tiempo = None
    seleccion = None
    satelite = None
    #if seleccion:
    if True:
        elementos_seleccionados = [lista.get(index) for index in lista_seleccion]
        for elemento in elementos_seleccionados:
            if elemento in archivos:
                archivo = elemento
            elif elemento in Algoritmos:
                algoritmo = elemento
            elif elemento in Frecuencias:
                frecuencia = elemento
            elif elemento in Pasos:
                paso = elemento
            elif elemento in Multiplos:
                multiplo = elemento
            elif elemento in Tiempos:
                tiempo = elemento
            elif elemento in Seleccion:
                seleccion = elemento
            elif elemento in Satelites:
                satelite = elemento
        if tiempo == "uno": tiempo = 1
        if seleccion=="MAD": seleccion =0
        if seleccion=="sigma": seleccion =1
        print(seleccion)
        #Datos aquí
        if frecuencia == 'L1' or frecuencia == 'L2': datos = eval(frecuencia)(archivo,satelite)
        else: 
            l1 = L1(archivo, satelite)
            l2 = L2(archivo, satelite)
            datos = eval(frecuencia)(l1,l2)

        if seleccion in {0,1} and multiplo and archivo and algoritmo and frecuencia and paso and tiempo:
            
            resultado = eval(algoritmo)(seleccion,datos,paso,multiplo,tiempo)
        
        elif multiplo and archivo and algoritmo and frecuencia and paso and tiempo:
            
            resultado = eval(algoritmo)(datos,paso,multiplo,tiempo)
        
        elif archivo and algoritmo and frecuencia and paso and tiempo:
            
            resultado = eval(algoritmo)(datos,paso,tiempo)
        
        mostrar_informacion(resultado,"resultados")
        
    else:
        messagebox.showwarning("Advertencia", "Debes seleccionar al menos un elemento")

# Crear la ventana principal
ventana = tk.Tk()

# Mostrar mensaje persistente al inicio del script
mensaje_persistente = mostrar_informacion(informacion,"Guía sobre ficheros")
mensaje_persistente2 = mostrar_informacion(informacion2,"Guía sobre algoritmos")
#hilo_mensaje_persistente = threading.Thread(target=mostrar_mensaje_persistente, args=(mensaje_persistente,))
#hilo_mensaje_persistente.start()

def desplegable(ventana_actual , select):
    opciones = select
    lista = tk.Listbox(ventana_actual, selectmode=tk.MULTIPLE)
    lista.pack()

    for opcion in opciones:
        lista.insert(tk.END, opcion)

    boton_seleccionar = tk.Button(ventana_actual, text="Seleccionar", command=obtener_elemento_seleccionado)
    boton_seleccionar.pack()
    return lista

lista = desplegable(ventana,archivos_alg)

ventana.mainloop()
