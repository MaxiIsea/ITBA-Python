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
import datetime
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

# Parte 2.
#
# Ingresar 2 países
# Graficar cantidad de casos y fallecimientos en dos gráficos con labels.
# Se debe poder ingresar el intervalo de tiempo a graficar.
# Calcular las intersecciónes entre gráficos si las hubiera y marcarlas con un punto de algún tipo.

# Pedir dato por pantalla.
nomPais1 = input("Ingresar 1º pais: ")
nomPais2 = input("Ingresar 2º pais: ")

respuesta = input("¿Ingresar rango de fechas?")
if respuesta.lower() == "s":
    fecDesde = input("Desde fecha: ")
    fecHasta = input("Hasta fecha: ")

    # Agregar controles

# Segun entiendo, al decir "Se debe poder ingresar el intervalo de tiempo", no seria obligatorio
# ... se deberia preguntar al usuario si quiere o no. En caso afirmativo, filtar
# Controlar que la fecha desde NO sea mayor a fecha hasta
# Controlar que las fechas sean validas y el usuario no ingrese datos invalidos. Quizas proponiendo el formato DD/MM/AAAA
# En el filtro, las fechas estan hardcodeadas.. Cuando se haga bien, si el usuario quiere un rango de fechas,
# ... se podria 1. Filtrar ahi mismo y obtener un archivo mas chico o 2. En el FOR que recorre y carga los EJES
# ... contemplar las fechas.

# Filtrado.
if respuesta.lower() == "s":
    auxPais1 = df_archivo[((df_archivo['location'] == nomPais1.title())) & ((df_archivo['date'] >= fecDesde) & (df_archivo['date'] <= fecHasta))]
    auxPais2 = df_archivo[((df_archivo['location'] == nomPais2.title())) & ((df_archivo['date'] >= fecDesde) & (df_archivo['date'] <= fecHasta))]
else:
    auxPais1 = df_archivo[(df_archivo['location'] == nomPais1.title())]
    auxPais2 = df_archivo[(df_archivo['location'] == nomPais2.title())]

# Convertir el DataFrame a un Diccionario para trabajar mejor los datos.
archivoPais1 = auxPais1.to_dict("list")
archivoPais2 = auxPais2.to_dict("list")

cantRegistrosPais1 = len(archivoPais1["date"])
cantRegistrosPais2 = len(archivoPais2["date"])

# Inicializar ejes del grafico para Pais 1.
x_p1 = []      # Tiempo (date)
y1_p1 = []     # Total de casos (total_cases)
y2_p1 = []     # Total de fallecimientos (total_deaths)

# Inicializar ejes del grafico para Pais 2.
#x_p2 = []      # Tiempo (date)
y1_p2 = []     # Total de casos (total_cases)
y2_p2 = []     # Total de fallecimientos (total_deaths)

# Falta agregar Menu
# Falta enriquecer el Grafico
# Control de fechas
# Control de paises

cruce_casos_x = []
cruce_casos_y = []
cruce_muertes_x = []
cruce_muertes_y = []

# Recorrer archivo e ir agregando datos que necesito mostrar en el grafico para Pais 1.
for i in range(cantRegistrosPais1):
  x_p1.append(archivoPais1["date"][i])
  y1_p1.append(archivoPais1["total_cases"][i])
  y2_p1.append(archivoPais1["total_deaths"][i])
  y1_p2.append(archivoPais2["total_cases"][i])
  y2_p2.append(archivoPais2["total_deaths"][i])
  if (y1_p1[i] == y1_p2[i]) or (y1_p1[i] > y1_p2[i] and y1_p1[i-1] < y1_p2[i-1]) or (y1_p1[i] < y1_p2[i] and y1_p1[i-1] > y1_p2[i-1]):
      cruce_casos_x.append(x_p1[i])
      cruce_casos_y.append(y1_p2[i])
  if(y2_p1[i] == y2_p2[i]) or (y2_p1[i] > y2_p2[i] and y2_p1[i-1] < y2_p2[i-1]) or (y2_p1[i] < y2_p2[i] and y2_p1[i-1] > y2_p2[i-1]):
      cruce_muertes_x.append(x_p1[i])
      cruce_muertes_y.append(y2_p2[i])

# Graficar datos para pais 1.
plt.figure(figsize=(30, 20))                                                    # Tamaño del grafico

plt.xlabel('Tiempo / dias')                                                     # Etiqueta Eje X
plt.ylabel('Casos / personas')                                                  # Etiqueta Eje Y

plt.subplot(2, 1, 1)
plt.grid(axis='y')
plt.xticks(rotation=70)                                                              # Indico posicion del sub-grafico
plt.title("Casos totales detectados para " + nomPais1.title() +" y "+ nomPais2.title())    # Titulo del grafico
plt.plot(x_p1, y1_p1, label= nomPais1.title())                                  # Graficar Eje X. Se le asigna una etiqueta
plt.plot(x_p1, y1_p2, label= nomPais2.title())                                  # Graficar Eje Y. Se le asigna una etiqueta
plt.plot(cruce_casos_x, cruce_casos_y, 'ko' )
plt.legend(loc='upper center')                                                  # Mostrar labels. Posicion inferior derecha


plt.subplot(2, 1, 2)
plt.grid(axis='y')
plt.xticks(rotation=70)                                                              # Indico posicion del sub-grafico
plt.title("Fallecimientos totales para " + nomPais1.title() +" y "+ nomPais2.title())    # Titulo del grafico
plt.plot(x_p1, y2_p1, label= nomPais1.title())                                  # Graficar Eje X. Se le asigna una etiqueta
plt.plot(x_p1, y2_p2, label= nomPais2.title())                                  # Graficar Eje Y. Se le asigna una etiqueta
plt.plot(cruce_muertes_x, cruce_muertes_y, 'ko')
plt.legend(loc='upper center')


plt.show()                                                                      # Dibujar grafico