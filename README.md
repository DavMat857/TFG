# TFG: MÉTODOS HEURÍSTICOS PARA DETECCIÓN DE DISCONTINUIDADES EN LA RECEPCIÓN DE SATÉLITES DE POSICIONAMIENTO
#### Autor: David Labrador Merino
Observación: la creación de este repositorio no está basado en otros y la autoría me pertenece al 100%

Vamos a presentar distintos scripts para la detección de saltos de ciclo:
## Para el preprocesado de los ficheros Rinex 2.11 usaremos:

* `funcionesdef.py`: contiene la información relativa a las funciones utilizadas. 
*  `preprocesado.ipynb`: muestra ejemplos de utilización del anterior script.

## Algoritmos contiene scripts para la detección del ciclos[Todos están explicados en el TFG]:

Para ejecutarlos una de las opciones es: python -i script.py y luego poner algoritmo() o comprobación() para el caso de `contraste.py`. De esta manera se ejecutan unos valores predeterminados, que se podrían cambiar leyendo las indicaciones de cada algoritmo en `resumen.ipynb`.
__Observación__: los algoritmos siguen la misma estructura
1. Datos a seleccionar.
2. Algoritmo.
3. Funciones auxiliares.

### Veamos los algoritmos utilizados
	*Algoritmos basados en un ajuste polinomial: "combinacion_libre_geo.py",  "combinacion_libre_geo2.py",  "combinacion_libre_io.py",  "combinacion_geo_iono.py".
		
	*Algoritmo basado en clustering: "clustering.py".

	*Algoritmo basado en el filtro promedio: "filtropromedio.py".

	*Algoritmo basado en regresión lineal: "regresion.py".

	*Algoritmo para verificar la existencia de un salto de ciclo "contraste.py". 

Además contiene el script `aplicacion.py` que sirve para ejecutar una aplicación de escritorio para utilizar los Algoritmos previos de forma interactiva.
 `read.txt` aporta información sobre el uso de la aplicación.

	

	## Datos

Contiene información sobre los archivos Rinex, además en `read.txt` tenemos información adicional sobre cada archivo

	## Resultados
	
Contiene información acerca de las pruebas utilizadas y dos scripts: `resultados.py` con este script se han obtenido los .csv y `graficar_resultados.py` que permite graficar los .csv

## Aplicacion

Contiene los pasos previos a la creación de `aplicación.py` que se encuentra dentro de la carpeta `algoritmos`

## License 

Contiene una licencia de tipo `Apache-2.0license`


