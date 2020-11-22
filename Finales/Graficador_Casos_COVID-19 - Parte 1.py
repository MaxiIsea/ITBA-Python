# IEEE ITBA - Curso introductorio de Python.
# Proyecto Final - Graficador de casos del COVID-19.
#
# Integrantes del equipo:
# Isea, Maximiliano. (ID: )
# Morales, Paul. (ID: 39317)

# Importar librerias.
import requests
import pandas
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)

#wget('https://covid.ourworldindata.org/data/ecdc/full_data.csv')

# Convertir el archivo descargado a DataFrame.
df_archivo = pandas.read_csv("full_data.csv")

# Campos CSV
# date, location, new_cases, new_deaths, total_cases, total_deaths, weekly_cases, weekly_deaths, biweekly_cases, biweekly_deaths

os.system("cls") # Borrar terminal.

# Parte 1.
#
# Recibir nombre de pais.
# Graficar casos detectados y fallecimientos totales para ese país en función del tiempo.

# Pedir dato por pantalla.
nomPais = input("Ingresar pais: ")

# Filtrado.
aux = df_archivo[df_archivo['location'] == nomPais.title()]

# Convertir el DataFrame a un Diccionario para trabajar mejor los datos.
archivo = aux.to_dict("list")
cantRegistros = len(archivo["date"])

# Inicializar ejes del grafico.
x = []      # Tiempo (date)
y1 = []     # Casos detectados (new_cases)
y2 = []     # Muertes totales (total_deaths)

# Se podria graficar con un punto el dia de mayor muertes
# Se podria graficar con un punto el dia de mayor casos detectados
# Falta agregar Menu
# Falta enriquecer el Grafico
# Para investigar: Formatear EJE X para mostrar mejor fechas.. Quizas mes a mes???
#   https://matplotlib.org/3.3.2/gallery/text_labels_and_annotations/date.html

# Recorrer archivo e ir agregando datos que necesito mostrar en el grafico.
for i in range(cantRegistros):
  x.append(archivo["date"][i])
  y1.append(archivo["new_cases"][i])
  y2.append(archivo["total_deaths"][i])

plt.figure(figsize=(12, 4))                                                     # Tamaño del grafico
plt.title("Casos detectados y fallecimientos totales para " + nomPais.title())  # Titulo del grafico
plt.xlabel('Tiempo / dias')                                                     # Etiqueta Eje X
plt.ylabel('Casos / personas')                                                  # Etiqueta Eje Y

# plt.xticks(x[ : :30])                             # Mostrar una de cada 30 fechas - NO ANDA !!
plt.grid(axis='y')                                  # Mostrar una grilla horizontal

plt.plot(x, y1, label='Casos detectados')           # Graficar Eje X. Se le asigna una etiqueta
plt.plot(x, y2, label='Fallecimientos totales')     # Graficar Eje Y. Se le asigna una etiqueta

plt.legend(loc='upper left')                        # Mostrar labels. Posicion inferior derecha
plt.show()                                          # Dibujar grafico


