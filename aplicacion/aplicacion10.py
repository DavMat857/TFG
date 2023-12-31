from combinacion_libre_geo import algoritmo as alg_geo
from combinacion_libre_io import algoritmo as alg_io
from clustering import algoritmo as alg_clus
from regresion2 import algoritmo as alg_reg
from filtropromedio import algoritmo as alg_fil

import os
from funcionesdef import *
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

carpeta_datos = 'datos'
archivos = [
    os.path.join(carpeta_datos, archivo)
    for archivo in os.listdir(carpeta_datos)
    if archivo.endswith("O") and os.path.isfile(os.path.join(carpeta_datos, archivo))
]

Algoritmos = ['alg_geo', 'alg_io', 'alg_clus', 'alg_fil', 'alg_reg']
Frecuencias = ['L1', 'L2', 'f1menosf2', 'combinacion_libre_ios']
Pasos = list(range(10, 20))
Multiplos = list(range(1, 5))
Tiempos = ["uno", 30]
Seleccion = ["MAD", "sigma"]
Satelites = ['G0' + str(i) for i in range(1, 10)] + ['G' + str(i) for i in range(10, 36)]
archivos_alg = ["--- Selección ---"] + Seleccion + ["--- Archivos ---"] + archivos + ["--- Satélites ---"] + Satelites + [
    "--- Algoritmos ---"] + Algoritmos + ["--- Frecuencias ---"] + Frecuencias + ["--- Paso ---"] + Pasos + [
                   "--- Múltiplo ---"] + Multiplos + ["--- Tiempo ---"] + Tiempos

historial_resultados = []  # Lista para almacenar los resultados obtenidos


def leer_contenido_archivo(archivo):
    with open(archivo, 'r') as f:
        contenido = f.read()
    return contenido


def mostrar_informacion(elemento, titulo):
    ventana_info = tk.Toplevel(ventana)
    ventana_info.geometry("400x300+200+200")
    ventana_info.title(titulo)

    texto_info = scrolledtext.ScrolledText(ventana_info, width=50, height=10)
    texto_info.pack()
    texto_info.insert(tk.INSERT, elemento)
    texto_info.configure(state='disabled')


def mostrar_resultados(resultado):
    texto_resultados.configure(state='normal')
    texto_resultados.delete("1.0", tk.END)
    texto_resultados.insert(tk.INSERT, resultado)
    texto_resultados.configure(state='disabled')
    historial_resultados.append(resultado)  # Agregar resultado al historial


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

    if tiempo == "uno":
        tiempo = 1
    if seleccion == "MAD":
        seleccion = 0
    if seleccion == "sigma":
        seleccion = 1

    if frecuencia == 'L1' or frecuencia == 'L2':
        datos = eval(frecuencia)(archivo, satelite)
    else:
        l1 = L1(archivo, satelite)
        l2 = L2(archivo, satelite)
        datos = eval(frecuencia)(l1, l2)

    if seleccion in {0, 1} and multiplo and archivo and algoritmo and frecuencia and paso and tiempo:
        resultado = eval(algoritmo)(seleccion, datos, paso, multiplo, tiempo)
    elif multiplo and archivo and algoritmo and frecuencia and paso and tiempo:
        resultado = eval(algoritmo)(datos, paso, multiplo, tiempo)
    elif archivo and algoritmo and frecuencia and paso and tiempo:
        resultado = eval(algoritmo)(datos, paso, tiempo)
       
    mostrar_resultados(resultado)


ventana = tk.Tk()
ventana.attributes('-fullscreen', True)

contenedor_principal = tk.Frame(ventana)
contenedor_principal.pack(fill=tk.BOTH, expand=True)

frame_guia1 = tk.Frame(contenedor_principal)
frame_guia1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frame_guia2 = tk.Frame(contenedor_principal)
frame_guia2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

label_guia1 = tk.Label(frame_guia1, text="Instrucciones de guía 1:")
label_guia1.pack()

informacion1 = leer_contenido_archivo("datos/read.txt")

texto_guia1 = scrolledtext.ScrolledText(frame_guia1, width=50, height=10)
texto_guia1.pack()
texto_guia1.insert(tk.INSERT, informacion1)
texto_guia1.configure(state='disabled')

label_guia2 = tk.Label(frame_guia2, text="Instrucciones de guía 2:")
label_guia2.pack()

informacion2 = leer_contenido_archivo("read.txt")

texto_guia2 = scrolledtext.ScrolledText(frame_guia2, width=50, height=10)
texto_guia2.pack()
texto_guia2.insert(tk.INSERT, informacion2)
texto_guia2.configure(state='disabled')

texto_resultados = scrolledtext.ScrolledText(contenedor_principal, width=50, height=10)
texto_resultados.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
texto_resultados.configure(state='disabled')

lista = tk.Listbox(contenedor_principal, selectmode=tk.MULTIPLE)
lista.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

for opcion in archivos_alg:
    lista.insert(tk.END, opcion)

boton_seleccionar = tk.Button(contenedor_principal, text="Seleccionar", command=obtener_elemento_seleccionado)
boton_seleccionar.pack(side=tk.BOTTOM)

ventana.mainloop()
