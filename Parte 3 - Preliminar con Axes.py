import requests
import pandas
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import os
 
def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)
 
wget('https://covid.ourworldindata.org/data/ecdc/full_data.csv')
 
# Convertir el archivo descargado a DataFrame.
df_archivo = pandas.read_csv("full_data.csv")
 
# Campos CSV
# date, location, new_cases, new_deaths, total_cases, total_deaths, weekly_cases, weekly_deaths, biweekly_cases, biweekly_deaths
 
os.system("cls") # Borrar terminal.
 
# Parte 3
#
# Ingresar n países
# Graficar la cantidad de casos en una escala logarítmica.
# El programa debe pedirle al usuario el intervalo de tiempo deseado.

def graficar(setPaises, fecDesde, fecHasta, axes):
 
    cantidadPaises = len(setPaises)
    #k=1
 
    for i in range(cantidadPaises): # REVISADO V2
        nomPais = setPaises.pop()
     
        auxPais = df_archivo[((df_archivo['location'] == nomPais.title())) & ((df_archivo['date'] >= fecDesde) & (df_archivo['date'] <= fecHasta))]
     
        # Convertir el DataFrame a un Diccionario para trabajar mejor los datos.
        archivoPais = auxPais.to_dict("list")
     
        cantRegistrosPais = len(archivoPais["date"])
     
        x = []      # Tiempo (date)
        y = []     # Total de casos (total_cases)
        
        for j in range(cantRegistrosPais):
            x.append(archivoPais["date"][j])
            y.append(archivoPais["total_cases"][j])
         
        #plt.figure(figsize=(18, 6))                                             # Tamaño del grafico
             
        axes[i] = plt.xlabel('Tiempo / dias')                                             # Etiqueta Eje X
        axes[i] = plt.ylabel('Casos / personas')                                          # Etiqueta Eje Y
             
        axes[i] = plt.grid(axis='y')                                                      # Mostrar una grilla horizontal
        axes[i] = plt.yscale("log")
            
        axes[i] = plt.subplot(cantidadPaises, 1, i+1)                                       # Indico posicion del sub-grafico
        #k+=1
        axes[i] = plt.title("Casos totales y fallecimientos totales para " + nomPais)     # Titulo del grafico
        axes[i] = plt.plot(x, y, label='Casos detectados')                                # Graficar Eje X. Se le asigna una etiqueta
        grados = 70
        axes[i] = plt.xticks(rotation=grados)
        axes[i] = plt.legend(loc='upper center')
        axes.subplot_adjust()
    #return axes
 

archivoPaises = df_archivo.to_dict("list")

paisesDisponibles = set()

for i in range(len(archivoPaises["location"])):
    paisesDisponibles.add(archivoPaises["location"][i])

setPaises = set()                   # Set para almacenar países

nomPais = input("Ingresar paises ('Salir' para salir): ")

while nomPais.title().strip() != "Salir":
    if nomPais.title().strip() not in paisesDisponibles:
        print("El pais ingresado no existe")
    elif nomPais.title().strip() in setPaises:
        print("Ya se ha ingresado este pais.")
    else:
        setPaises.add(nomPais)      # Agrego pais ingresado al conjunto
        
    nomPais = input("Ingresar paises ('Salir' para salir): ")
 
# Esto hay que modularizarlo asi se puede reutilizar. Asi es horrible:
# Hay que agregar un control de fechas que se pueda llamar desde las otras partes del programa.
print("* Ingresar rango de fechas para visualizar grafico. *")
fecDesde = input("Desde fecha: ")
fecHasta = input("Hasta fecha: ")
 
#cantidadPaises = len(setPaises)

fig, Axes = plt.subplots(nrows=len(setPaises), ncols=1, constrained_layout=True, figsize=(15*len(setPaises), 10*len(setPaises)))
graficar(setPaises, fecDesde, fecHasta, Axes)
plt.show()