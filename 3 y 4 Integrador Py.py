def opcion_3():                                                                     # Definimos funcion graficar la cual llamaremos desde el programa con sus respectivos parametros
 
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

def opcion_4():                                               # Definimos funcion graficar la cual llamaremos desde el programa con sus respectivos parametros
 
    # Armamos un set con los paises que queremos graficar
    setPaises = {"Argentina", "Chile", "Bolivia", "Paraguay", "Brasil", "Uruguay"}
    cantidadPaises = len(setPaises)                                               #Almacenamos la cantidad de paises del set que viene por parametro
    
    print("* Meses de invierno (21 de Junio a 21 de Septiembre) *")
    fecDesde = "2020-06-21"
    fecHasta = "2020-09-21"
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
