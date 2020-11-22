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
import matplotlib.dates as mdates
import datetime
import os
 
# Al trabajar en Windows necesitamos declarar la funcion wget para obtener el archivo a procesar
def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)
 
# Descargamos el archivo que vamos a procesar con la funcion wget
wget('https://covid.ourworldindata.org/data/ecdc/full_data.csv')
 
# Convertir el archivo descargado a DataFrame.
df_archivo = pandas.read_csv("full_data.csv")
 
# Campos CSV
# date, location, new_cases, new_deaths, total_cases, total_deaths, weekly_cases, weekly_deaths, biweekly_cases, biweekly_deaths
 
os.system("cls") # Borrar terminal
 
# Parte 3
#
# Ingresar n países
# Graficar la cantidad de casos en una escala logarítmica.
# El programa debe pedirle al usuario el intervalo de tiempo deseado.

def graficar(setPaises, fecDesde, fecHasta):                                    # Definimos funcion graficar la cual llamaremos desde el programa con sus respectivos parametros
 
    cantidadPaises = len(setPaises)                                             # Almacenamos en una variable la cantidad de paises que ingresa el usuario
    plt.figure(figsize=(15*len(setPaises), 10*len(setPaises)))                  # Tamaño del grafico
 
    for i in range(cantidadPaises):                                             # Iteramos la cantidad de veces como paises fueron ingresados
        
        nomPais = setPaises.pop()                                               # Quitamos del set de Paises un pais y almacenamos su nombre en una variable
     
        # En la linea debajo filtramos el archivo para quedarnos solo con los datos del pais en cuestión con las fechas ingresadas por el usuario
        auxPais = df_archivo[((df_archivo['location'] == nomPais.title())) & ((df_archivo['date'] >= fecDesde) & (df_archivo['date'] <= fecHasta))]
     
        # Convertir el DataFrame a un Diccionario para trabajar mejor los datos.
        archivoPais = auxPais.to_dict("list")
     
        #Almacenamos la cantidad de datos que tiene nuestro diccionario
        cantRegistrosPais = len(archivoPais["date"])
     
        x = []                                                                  # Tiempo (date)
        y = []                                                                  # Total de casos (total_cases)
        
        for j in range(cantRegistrosPais):                                      # Iteramos la cantidad de veces como registros tiene nuestro diccionario
            x.append(archivoPais["date"][j])                                    # Llenamos una variable que sera nuestro eje x con las fechas ya filtradas
            y.append(archivoPais["total_cases"][j])                             # Llenamos una variable que sera nuestro eje y con los casos totales ya filtrados                       
             
        plt.subplot(cantidadPaises, 1, i+1)                                     # Indico posicion del sub-grafico
        plt.xlabel('Tiempo / dias')                                             # Etiqueta Eje X
        plt.ylabel('Casos / personas')                                          # Etiqueta Eje Y
        plt.grid(axis='y')                                                      # Mostrar una grilla horizontal
        plt.yscale("log")                                                       # Le decimos al eje y que utilice escala logaritmica
        plt.title("Casos totales y fallecimientos totales para " + nomPais)     # Titulo del grafico
        plt.plot(x, y, label='Casos detectados')                                # Graficar Eje X. Se le asigna una etiqueta
        plt.xticks(rotation=70)                                                 # Le damos rotacion de 70° a la leyenda del eje x para que se vean claras las fechas
        plt.legend(loc='upper center')                                          # Decimos que la leyenda va a estar arriba centrada
 

# Convertir el DataFrame a un Diccionario para trabajar mejor los datos.
archivoPaises = df_archivo.to_dict("list")

# Creamos un set para almacenar todos los paises y luego filtrar cuales pide el usuario
paisesDisponibles = set()

# Llenamos el set con todos los paises dentro del archivo principal
for i in range(len(archivoPaises["location"])):
    paisesDisponibles.add(archivoPaises["location"][i])

setPaises = set()                                                               # Set para almacenar países ingresados por el usuario

nomPais = input("Ingresar paises ('Salir' para salir): ")                       # Variable que ira almacenando los paises ingresados por el usuario

# Bloque que verificara si el pais existe, si no existe arroja un mensaje avisando esto, si existe se almacenara en el set, si esta repetido le dara aviso al usuario
while nomPais.title().strip() != "Salir":
    if nomPais.title().strip() not in paisesDisponibles:
        print("El pais ingresado no existe")
    elif nomPais.title().strip() in setPaises:
        print("Ya se ha ingresado este pais.")
    else:
        setPaises.add(nomPais)                                                  # Agrego pais ingresado al conjunto
        
    nomPais = input("Ingresar paises ('Salir' para salir): ")
 
# Ingreso de fechas para acotar el grafico a lo pedido por el usuario
print("* Ingresar rango de fechas para visualizar grafico. *")
fecDesde = input("Desde fecha: ")
fecHasta = input("Hasta fecha: ")
# Llamado a la funcion que va a armar un grafico con sus respectivos sub-graficos por pais
graficar(setPaises, fecDesde, fecHasta)
# Le decimos a la libreria que muestra el grafico
plt.show()