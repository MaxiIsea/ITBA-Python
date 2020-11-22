# IEEE ITBA - Curso introductorio de Python.
# Proyecto Final - Graficador de casos del COVID-19.
#
# Integrantes del equipo:
# Isea, Maximiliano. (ID: 29599 )
# Morales, Paul. (ID: 39317)

# Importar librerías.
import requests
import pandas
import numpy as np
import math
import matplotlib.pyplot as plt
import datetime
import os

# Al trabajar en Windows necesitamos declarar la funcion wget para obtener el archivo a procesar
def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)


def graficar(setPaises, fecDesde, fecHasta):                                      # Definimos funcion graficar la cual llamaremos desde el programa con sus respectivos parametros
 
    cantidadPaises = len(setPaises)                                               #Almacenamos la cantidad de paises del set que viene por parametro
    
    plt.figure(figsize=(30, 20))                                                  # Tamaño del grafico

    x = []                                                                        # Tiempo (date)
       
    for i in range(cantidadPaises):                                               # Iteramos la cantidad de veces como paises fueron ingresados
        
        nomPais = setPaises.pop()                                                 # Quitamos del set de Paises un pais y almacenamos su nombre en una variable
     
        # En la linea debajo filtramos el archivo para quedarnos solo con los datos del pais en cuestión con las fechas ingresadas por el usuario
        auxPais = df_archivo[((df_archivo['location'] == nomPais.title())) & ((df_archivo['date'] >= fecDesde) & (df_archivo['date'] <= fecHasta))]
     
        # Convertir el DataFrame a un Diccionario para trabajar mejor los datos.
        archivoPais = auxPais.to_dict("list")
        
        #Almacenamos la cantidad de datos que tiene nuestro diccionario     
        cantRegistrosPais = len(archivoPais["date"])
     
        x = []                                                                    # Tiempo (date)
        y = []                                                                    # Total de casos (total_cases)
        
        for j in range(cantRegistrosPais):                                        # Iteramos la cantidad de veces como registros tiene nuestro diccionario
            x.append(archivoPais["date"][j])                                      # Llenamos una variable que sera nuestro eje x con las fechas ya filtradas
            y.append(archivoPais["total_cases"][j])                               # Llenamos una variable que sera nuestro eje y con los casos totales ya filtrados                                         
   
        plt.xlabel('Tiempo / dias')                                               # Etiqueta Eje X
        plt.ylabel('Casos / personas')                                            # Etiqueta Eje Y
        plt.grid(axis='y')                                                        # Mostrar una grilla horizontal
        plt.yscale("log")
        plt.title("Casos totales detectados para Argentina y sus paises limítrofes")     # Titulo del grafico
        plt.plot(x, y, label=nomPais.title())                                     # Graficar Eje X. Se le asigna una etiqueta
        plt.xticks(x[::5], rotation=70)                                           # Le damos rotacion de 70° a la leyenda del eje x y mostramos cada 5 posiciones para que se vean claras las fechas 
        plt.legend(loc='upper center')                                            # Decimos que la leyenda va a estar arriba centrada

# Descargamos el archivo que vamos a procesar con la funcion wget
wget('https://covid.ourworldindata.org/data/ecdc/full_data.csv')

# Convertir el archivo descargado a DataFrame.
df_archivo = pandas.read_csv("full_data.csv")

# Campos CSV
# date, location, new_cases, new_deaths, total_cases, total_deaths, weekly_cases, weekly_deaths, biweekly_cases, biweekly_deaths

os.system("cls")  # Borrar terminal.

# Parte 4 - Grafico a entregar.
#
# Graficar sobre la misma imagen la cantidad de casos en una escala logaritmica de Argentina y todos sus países limítrofes (Chile, Bolivia, Paraguay, Brasil y Uruguay)
# Debe comprender los meses de invierno (21 de Junio a 21 de Septiembre).
# Debe quedar claro la curva que corresponde a cada país.

# Convertir el DataFrame a un Diccionario para trabajar mejor los datos.
archivoPaises = df_archivo.to_dict("list") 

# Armamos un set con los paises que queremos graficar
setPaises = {"Argentina", "Chile", "Bolivia", "Paraguay", "Brasil", "Uruguay"}

# Ingreso de fechas para acotar el grafico a lo pedido por el usuario
print("* Meses de invierno (21 de Junio a 21 de Septiembre) *")
fecDesde = "2020-06-21"
fecHasta = "2020-09-21"
# Llamado a la funcion que va a armar un grafico con sus respectivos sub-graficos por pais
graficar(setPaises, fecDesde, fecHasta)
# Le decimos a la libreria que muestra el grafico
plt.show()