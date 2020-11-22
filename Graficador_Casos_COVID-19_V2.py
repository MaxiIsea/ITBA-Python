# IEEE ITBA - Curso introductorio de Python.
# Proyecto Final - Graficador de casos del COVID-19.
#
# Integrantes del equipo:
# Isea, Maximiliano. (ID: 29599)
# Morales, Paul. (ID: 39317)

# Importar librerias.
import requests
import pandas
import matplotlib.pyplot as plt
from datetime import datetime
import time
import os
import msvcrt

def wget(url):
  r = requests.get(url, allow_redirects=True)
  with open(url[url.rfind('/') + 1::], 'wb') as f:
      f.write(r.content)

def borrar_pantalla():
  os.system("cls") # Borrar terminal.

def pedirOpcion(): 
  correcto = False
  opcion = 0
  while(not correcto):
      try:
          opcion = int(input("Ingresar opción: "))
          correcto = True
      except ValueError:
          print('Error, introduce un numero entero')
    
  return opcion

def pedirSiNo():
  while True:
    print("Ingrese S (Si) - N (No): ")
    opcion = input().upper()
    if opcion in ["S", "N"]:
        return opcion

def pedirFecha():
  while True:
    try:
      auxFecha = input("Formato fecha ==> 'AAAA-MM-DD'...: ")
      fecha = datetime.strptime(auxFecha, '%Y-%m-%d')
      break
    except:
      print("No ha ingresado una fecha correcta...")
  return fecha

#def pedirPais():

def menu_opcion_1():
  # Recibir nombre de pais.
  # Graficar casos detectados y fallecimientos totales para ese país en función del tiempo.

  # Pedir dato por pantalla.
  nomPais = input("Ingresar pais ('Salir' para volver al Menú): ")

  while nomPais.title().strip() != "Salir":
    if nomPais.title().strip() not in paisesDisponibles:
      print("El pais ingresado no existe. Presione una tecla para continuar...")
      msvcrt.getch()
    else:
      break

      borrar_pantalla() 
      nomPais = input("\nIngresar pais ('Salir' para volver al Menú): ")   

  # Filtrado.
  aux = df_archivo[df_archivo['location'] == nomPais.title()]

  # Convertir el DataFrame a un Diccionario para trabajar mejor los datos.
  archivo = aux.to_dict("list")
  cantRegistros = len(archivo["date"])

  # Inicializar ejes del grafico.
  x = []      # Tiempo (date)
  y1 = []     # Casos detectados (new_cases)
  y2 = []     # Muertes totales (total_deaths)

  # Recorrer archivo e ir agregando datos que necesito mostrar en el grafico.
  for i in range(cantRegistros):
    x.append(archivo["date"][i])
    y1.append(archivo["new_cases"][i])
    y2.append(archivo["total_deaths"][i])

  # Configurar grafico
  plt.figure(figsize=(16, 8))                                                     # Tamaño del grafico
  plt.title("Casos detectados y fallecimientos totales para " + nomPais.title())  # Titulo del grafico
  plt.xlabel('Tiempo / dias')                                                     # Etiqueta Eje X
  plt.ylabel('Casos / personas')                                                  # Etiqueta Eje Y

  plt.grid(axis='y')                                                              # Mostrar una grilla horizontal
  plt.plot(x, y1, label='Casos detectados')                                       # Graficar Eje X. Se le asigna una etiqueta
  plt.plot(x, y2, label='Fallecimientos totales')                                 # Graficar Eje Y. Se le asigna una etiqueta
  plt.xticks(x[::10], rotation=70)                                                # Rotar 70º los labels del eje X
  plt.legend(loc='upper center')                                                  # Mostrar labels

  # Dar la posibilidad al usuario de guardar el grafico eligiendo el nombre del archivo.
  print("\n¿Desea almacenar el gráfico generado?")
  if pedirSiNo() == "S": 
    nombreGrafico = input("\nIngresar nombre para el grafico: ")
    nombreGrafico = nombreGrafico.strip() + ".png"
    plt.savefig(nombreGrafico)

def menu_opcion_2():
  # Ingresar 2 países
  # Graficar cantidad de casos y fallecimientos en dos gráficos con labels.
  # Se debe poder ingresar el intervalo de tiempo a graficar.
  # Calcular las intersecciónes entre gráficos si las hubiera y marcarlas con un punto de algún tipo.

  # Pedir primer dato por pantalla.
  nomPais1 = input("Ingresar 1º pais ('Salir' para volver al Menú): ")

  while nomPais1.title().strip() != "Salir":
      if nomPais1.title().strip() not in paisesDisponibles:
          print("El pais ingresado no existe. Presione una tecla para continuar...")
          msvcrt.getch()
      else:
        break

      borrar_pantalla() 
      nomPais1 = input("\nIngresar 1º pais ('Salir' para volver al Menú): ")

  # Pedir segundo dato por pantalla.
  nomPais2 = input("Ingresar 2º pais ('Salir' para volver al Menú): ")
  while nomPais2.title().strip() != "Salir":
      if nomPais2.title().strip() not in paisesDisponibles:
          print("El pais ingresado no existe. Presione una tecla para continuar...")
          msvcrt.getch()
      else:
        break

      borrar_pantalla() 
      nomPais2 = input("Ingresar 2º pais ('Salir' para volver al Menú): ")

  # Dar la posibilidad de ingresar un rango de fechas.
  filtrarFechaSN = False
  print("\n¿Ingresar rango de fechas?")
  if pedirSiNo() == "S":
    print("Ingrese fecha desde: ")
    fecDesde = pedirFecha()
    print("Ingrese fecha hasta: ")
    fecHasta = pedirFecha()
    while fecHasta <= fecDesde:
      print("\nError: La 'fecha desde' debe ser inferior a la 'fecha hasta'")
      print("Ingrese fecha desde: ")
      fecDesde = pedirFecha()
      print("Ingrese fecha hasta: ")
      fecHasta = pedirFecha()
    filtrarFechaSN = True

  # Filtrado.
  if filtrarFechaSN:
    auxPais1 = df_archivo[((df_archivo['location'] == nomPais1.title())) & ((df_archivo['date'] >= fecDesde.strftime('%Y-%m-%d')) & (df_archivo['date'] <= fecHasta.strftime('%Y-%m-%d')))]
    auxPais2 = df_archivo[((df_archivo['location'] == nomPais2.title())) & ((df_archivo['date'] >= fecDesde.strftime('%Y-%m-%d')) & (df_archivo['date'] <= fecHasta.strftime('%Y-%m-%d')))]
  else:
    auxPais1 = df_archivo[(df_archivo['location'] == nomPais1.title())]
    auxPais2 = df_archivo[(df_archivo['location'] == nomPais2.title())]

  # Convertir el DataFrame a un Diccionario para trabajar mejor los datos.
  archivoPais1 = auxPais1.to_dict("list")
  archivoPais2 = auxPais2.to_dict("list")

  cantRegistrosPais1 = len(archivoPais1["date"])
  cantRegistrosPais2 = len(archivoPais2["date"])

  eje_x = 0  
  if(cantRegistrosPais1 < cantRegistrosPais2):
      eje_x = cantRegistrosPais1
  else:
      eje_x = cantRegistrosPais2


  # Inicializar ejes del grafico para Pais 1.
  x_p1 = []      # Tiempo (date)
  y1_p1 = []     # Total de casos (total_cases)
  y2_p1 = []     # Total de fallecimientos (total_deaths)

  # Inicializar ejes del grafico para Pais 2.
  y1_p2 = []     # Total de casos (total_cases)
  y2_p2 = []     # Total de fallecimientos (total_deaths)

  # Genero listas para almacenar las coordenadas de los cruces de los graficos.
  cruce_casos_x = []
  cruce_casos_y = []
  cruce_muertes_x = []
  cruce_muertes_y = []

  # Recorrer archivo e ir agregando datos que necesito mostrar en el grafico para Pais 1.
  for i in range(eje_x):
      x_p1.append(archivoPais1["date"][i])
      y1_p1.append(archivoPais1["total_cases"][i])
      y2_p1.append(archivoPais1["total_deaths"][i])
      y1_p2.append(archivoPais2["total_cases"][i])
      y2_p2.append(archivoPais2["total_deaths"][i])

      # Calculo cruces.
      if (y1_p1[i] == y1_p2[i]) or (y1_p1[i] > y1_p2[i] and y1_p1[i-1] < y1_p2[i-1]) or (y1_p1[i] < y1_p2[i] and y1_p1[i-1] > y1_p2[i-1]):
          cruce_casos_x.append(x_p1[i])
          cruce_casos_y.append(y1_p2[i])

      # Calculo cruces.    
      if(y2_p1[i] == y2_p2[i]) or (y2_p1[i] > y2_p2[i] and y2_p1[i-1] < y2_p2[i-1]) or (y2_p1[i] < y2_p2[i] and y2_p1[i-1] > y2_p2[i-1]):
          cruce_muertes_x.append(x_p1[i])
          cruce_muertes_y.append(y2_p2[i])

  # Configurar grafico.
  plt.figure(figsize=(30, 20))                                                                # Tamaño del grafico

  # Configurar sub grafico para el primer pais ingresado.
  plt.subplot(2, 1, 1)
  plt.xlabel('Tiempo / dias')                                                                 # Etiqueta Eje X
  plt.ylabel('Casos / personas')                                                              # Etiqueta Eje Y
  plt.grid(axis='y')                                                                          # Mostrar una grilla horizontal
  plt.yscale("log")                                                                           # Escala Eje Y: Logaritmica
  plt.xticks(rotation=70)                                                                     # Indico posicion del sub-grafico
  plt.title("Casos totales detectados")                                                       # Titulo del grafico
  plt.plot(x_p1, y1_p1, label= nomPais1.title())                                              # Graficar Eje X. Se le asigna una etiqueta
  plt.plot(x_p1, y1_p2, label= nomPais2.title())                                              # Graficar Eje Y. Se le asigna una etiqueta
  plt.plot(cruce_casos_x, cruce_casos_y, 'ko' )                                               # Graficar puntos de cruce en el grafico
  plt.legend(loc='upper center')                                                              # Mostrar labels. Posicion inferior derecha

  # Configurar sub grafico para el segundo pais ingresado.
  plt.subplot(2, 1, 2)
  plt.xlabel('Tiempo / dias')                                                                 # Etiqueta Eje X
  plt.ylabel('Casos / personas')                                                              # Etiqueta Eje Y
  plt.grid(axis='y')                                                                          # Mostrar una grilla horizontal
  plt.yscale("log")                                                                           # Escala Eje Y: Logaritmica
  plt.xticks(rotation=70)                                                                     # Indico posicion del sub-grafico
  plt.title("Fallecimientos totales")                                                         # Titulo del grafico
  plt.plot(x_p1, y2_p1, label= nomPais1.title())                                              # Graficar Eje X. Se le asigna una etiqueta
  plt.plot(x_p1, y2_p2, label= nomPais2.title())                                              # Graficar Eje Y. Se le asigna una etiqueta
  plt.plot(cruce_muertes_x, cruce_muertes_y, 'ko')                                            # Graficar puntos de cruce en el grafico
  plt.legend(loc='upper center')                                                              # Mostrar labels                                               

  # Dar la posibilidad al usuario de guardar el grafico eligiendo el nombre del archivo.
  print("\n¿Desea almacenar el gráfico generado?")
  if pedirSiNo() == "S": 
    nombreGrafico = input("Ingresar nombre para el grafico: ")
    nombreGrafico = nombreGrafico.strip() + ".png"
    plt.savefig(nombreGrafico)

def menu_opcion_3():
  # Definimos funcion graficar la cual llamaremos desde el programa con sus respectivos parametros
  # Creamos un set para almacenar todos los paises y luego filtrar cuales pide el usuario

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
  print("\nIngresar rango de fechas para visualizar grafico.")
  
  print("Ingrese fecha desde: ")
  fecDesde = pedirFecha()
  print("Ingrese fecha hasta: ")
  fecHasta = pedirFecha()
  while fecHasta <= fecDesde:
    print("\nError: La 'fecha desde' debe ser inferior a la 'fecha hasta'")
    print("Ingrese fecha desde: ")
    fecDesde = pedirFecha()
    print("Ingrese fecha hasta: ")
    fecHasta = pedirFecha()

  cantidadPaises = len(setPaises)                                             # Almacenamos en una variable la cantidad de paises que ingresa el usuario
  plt.figure(figsize=(15*len(setPaises), 10*len(setPaises)))                  # Tamaño del grafico

  for i in range(cantidadPaises):                                             # Iteramos la cantidad de veces como paises fueron ingresados
    nomPais = setPaises.pop()                                                 # Quitamos del set de Paises un pais y almacenamos su nombre en una variable
  
    # En la linea debajo filtramos el archivo para quedarnos solo con los datos del pais en cuestión con las fechas ingresadas por el usuario
    auxPais = df_archivo[((df_archivo['location'] == nomPais.title())) & ((df_archivo['date'] >= fecDesde.strftime('%Y-%m-%d')) & (df_archivo['date'] <= fecHasta.strftime('%Y-%m-%d')))]
  
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

  # Dar la posibilidad al usuario de guardar el grafico eligiendo el nombre del archivo.
  print("\n¿Desea almacenar el gráfico generado?")
  if pedirSiNo() == "S": 
    nombreGrafico = input("\nIngresar nombre para el grafico: ")
    nombreGrafico = nombreGrafico.strip() + ".png"
    plt.savefig(nombreGrafico)

def menu_opcion_4():
  # Definimos funcion graficar la cual llamaremos desde el programa con sus respectivos parametros
  # Armamos un set con los paises que queremos graficar
  setPaises = {"Argentina", "Chile", "Bolivia", "Paraguay", "Brasil", "Uruguay"}
  cantidadPaises = len(setPaises)                                               #Almacenamos la cantidad de paises del set que viene por parametro

  print("Meses de invierno (21 de Junio a 21 de Septiembre)")
  fecDesde = datetime.strptime("2020-06-21", '%Y-%m-%d')
  fecHasta = datetime.strptime("2020-09-21", '%Y-%m-%d')
  plt.figure(figsize=(30, 20))                                                  # Tamaño del grafico

  x = []                                                                        # Tiempo (date)
      
  for i in range(cantidadPaises):                                               # Iteramos la cantidad de veces como paises fueron ingresados     
    nomPais = setPaises.pop()                                                   # Quitamos del set de Paises un pais y almacenamos su nombre en una variable

    # En la linea debajo filtramos el archivo para quedarnos solo con los datos del pais en cuestión con las fechas ingresadas por el usuario
    auxPais = df_archivo[((df_archivo['location'] == nomPais.title())) & ((df_archivo['date'] >= fecDesde.strftime('%Y-%m-%d')) & (df_archivo['date'] <= fecHasta.strftime('%Y-%m-%d')))]

    # Convertir el DataFrame a un Diccionario para trabajar mejor los datos.
    archivoPais = auxPais.to_dict("list")
    
    #Almacenamos la cantidad de datos que tiene nuestro diccionario     
    cantRegistrosPais = len(archivoPais["date"])

    x = []                                                                           # Tiempo (date)
    y = []                                                                           # Total de casos (total_cases)
    
    for j in range(cantRegistrosPais):                                               # Iteramos la cantidad de veces como registros tiene nuestro diccionario
      x.append(archivoPais["date"][j])                                               # Llenamos una variable que sera nuestro eje x con las fechas ya filtradas
      y.append(archivoPais["total_cases"][j])                                        # Llenamos una variable que sera nuestro eje y con los casos totales ya filtrados                                         

    plt.xlabel('Tiempo / dias')                                                      # Etiqueta Eje X
    plt.ylabel('Casos / personas')                                                   # Etiqueta Eje Y
    plt.grid(axis='y')                                                               # Mostrar una grilla horizontal
    plt.yscale("log")
    plt.title("Casos totales detectados para Argentina y sus paises limítrofes")     # Titulo del grafico
    plt.plot(x, y, label=nomPais.title())                                            # Graficar Eje X. Se le asigna una etiqueta
    plt.xticks(x[::5], rotation=70)                                                  # Le damos rotacion de 70° a la leyenda del eje x y mostramos cada 5 posiciones para que se vean claras las fechas 
    plt.legend(loc='upper center')                                                   # Decimos que la leyenda va a estar arriba centrada

  # Dar la posibilidad al usuario de guardar el grafico eligiendo el nombre del archivo.
  print("\n¿Desea almacenar el gráfico generado?")
  if pedirSiNo() == "S": 
    nombreGrafico = input("\nIngresar nombre para el grafico: ")
    nombreGrafico = nombreGrafico.strip() + ".png"
    plt.savefig(nombreGrafico)    

def menu_opcion_5():
  # Ayuda de la aplicacion
  print("********************************")
  print("*    Ayuda de la aplicacion    *")
  print("********************************")
  print("\nOpción 1:")
  print("La aplicación recibe del usuario el nombre del país deseado permitiendo graficar los casos detectados y fallecimientos totales para dicho país en función del tiempo.")

  print("\nOpción 2:")
  print("La aplicación recibe del usuario 2 países permitiendo graficar y comparar la cantidad de casos y fallecimientos totales para dichos paises.")
  print("Opcionalmente, el usuario podrá ingresar el intervalo de tiempo a graficar si lo desea.")
  print("Se marcarán las intersecciones de los graficos con un punto.")

  print("\nOpción 3:")
  print("La aplicación recibe del usuario la cantidad deseada de países permitiendo graficar la cantidad de casos en una escala logaritmica.")
  print("El programa solicitará al usuario el intervalo de tiempo a informar.")

  print("\nOpción 4:")
  print("La aplicacion graficará las cantidad de casos en Argentina y todos sus países limítrofes (Chile, Bolivia, Paraguay, Brasil y Uruguay).")
  print("Se graficará el periodo comprendido entre las fechas 21/06/2020 y 21/09/2020 (Temporada de invierno).")
  print("Se graficará cada pais con un color diferente de modo que los datos puedan interpretarse con mayor facilidad.")

  print("\nNota adicional: Todas las opciones de la aplicación permitirán al usuario guardar una imagen del grafico generado en formato PNG. Se solicitará al usuario el nombre del archivo en cuestión.")

  print("\nPresione cualquier tecla para salir de la ayuda...")
  msvcrt.getch()

# Descargar archivo desde repositorio.
#wget('https://covid.ourworldindata.org/data/ecdc/full_data.csv')

# Campos CSV
# date, location, new_cases, new_deaths, total_cases, total_deaths, weekly_cases, weekly_deaths, biweekly_cases, biweekly_deaths 

# Convertir el archivo descargado a DataFrame.
df_archivo = pandas.read_csv("full_data.csv")
 
# Llenar conjunto con los paises existentes en el archivo para realizar los controles pertinentes.
archivoPaises = df_archivo.to_dict("list")
paisesDisponibles = set()
for i in range(len(archivoPaises["location"])):
    paisesDisponibles.add(archivoPaises["location"][i])

 # Menu Principal.
borrar_pantalla()
salir = False
opcion = 0

while not salir:
 
    print("*******************************************************")
    print("*    Menú principal - Graficador de casos COVID-19    *")
    print("*******************************************************")

    print("\n1. Graficar estadisticas de un pais a elección")
    print("2. Graficar estadisticas de dos paises a elección")
    print("3. Graficar estadisticas 'n' paises")
    print("4. Graficar estadisticas de Argentina y paises limítrofes.")
    print("5. Desplegar ayuda")

    print("\n0. Salir \n ")
 
    opcion = pedirOpcion()
  
    borrar_pantalla()

    if opcion == 1:
        menu_opcion_1()
        borrar_pantalla()
    elif opcion == 2:
        menu_opcion_2()
        borrar_pantalla()
    elif opcion == 3:
        menu_opcion_3()
        borrar_pantalla()
    elif opcion == 4:
        menu_opcion_4()
        borrar_pantalla()
    elif opcion == 5:
        menu_opcion_5()
        borrar_pantalla()       
    elif opcion == 0:
        salir = True
    else:
        print ("Opcion no válida. Presione '5' para desplegar ayuda.")
    # Mostrar grafico generado    
    plt.show()
 
print ("Fin del programa.")