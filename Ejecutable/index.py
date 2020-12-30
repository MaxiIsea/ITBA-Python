from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter.ttk import Combobox
import requests
import pandas
import matplotlib.pyplot as plt


class CovidDrawer:
    
    def __init__(self, window):

        def wget(url):
            r = requests.get(url, allow_redirects=True)
            with open(url[url.rfind('/') + 1::], 'wb') as f:
                f.write(r.content)
        
        def tab1_plotter():
            # Recibir nombre de pais.
            # Graficar casos detectados y fallecimientos totales para ese país en función del tiempo.

            # Pedir dato por pantalla.
            nomPais = tab1_country.get()

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
            plt.show()
        


        def tab2_plotter():
            # Ingresar 2 países
            # Graficar cantidad de casos y fallecimientos en dos gráficos con labels.
            # Se debe poder ingresar el intervalo de tiempo a graficar.
            # Calcular las intersecciónes entre gráficos si las hubiera y marcarlas con un punto de algún tipo.

            # Pedir primer dato por pantalla.
            nomPais1 = tab2_country1.get()

            # Pedir segundo dato por pantalla.
            nomPais2 = tab2_country2.get()

            # Filtrado.
            if len(txt_date1.get()) == 10 and len(txt_date2.get()) == 10:
                auxPais1 = df_archivo[((df_archivo['location'] == nomPais1.title())) & ((df_archivo['date'] >= txt_date1.get()) & (df_archivo['date'] <= txt_date2.get()))]
                auxPais2 = df_archivo[((df_archivo['location'] == nomPais2.title())) & ((df_archivo['date'] >= txt_date1.get()) & (df_archivo['date'] <= txt_date2.get()))]
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
            plt.show()
        
        def tab3_plotter():
        # Definimos funcion graficar la cual llamaremos desde el programa con sus respectivos parametros
        # Creamos un set para almacenar todos los paises y luego filtrar cuales pide el usuario

            cantidadPaises = len(setPaises_tab3)                                                    # Almacenamos en una variable la cantidad de paises que ingresa el usuario
            plt.figure(figsize=(15*len(setPaises_tab3), 10*len(setPaises_tab3)))                    # Tamaño del grafico

            for i in range(cantidadPaises):                                                         # Iteramos la cantidad de veces como paises fueron ingresados
                nomPais = setPaises_tab3.pop()                                                      # Quitamos del set de Paises un pais y almacenamos su nombre en una variable
            
                # En la linea debajo filtramos el archivo para quedarnos solo con los datos del pais en cuestión con las fechas ingresadas por el usuario
                auxPais = df_archivo[((df_archivo['location'] == nomPais.title())) & ((df_archivo['date'] >= txt_date1_tab3.get()) & (df_archivo['date'] <= txt_date2_tab3.get()))]
            
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
                plt.title("Casos totales detectados para " + nomPais)                              # Titulo del grafico
                plt.plot(x, y, label='Casos detectados')                                # Graficar Eje X. Se le asigna una etiqueta
                plt.xticks(rotation=70)                                                 # Le damos rotacion de 70° a la leyenda del eje x para que se vean claras las fechas
                plt.legend(loc='upper center')                                          # Decimos que la leyenda va a estar arriba centrada
            plt.show()
        
        def tab2_date_verification():
            if (tab2_country1.get() != tab2_country2.get()) and (tab2_country1.get() != '' or tab2_country2.get() != ''):
                if len(txt_date1.get()) != 10 and len(txt_date2.get()) == 10:
                    messagebox.showwarning('Error','Verificar fecha de inicio')
                elif len(txt_date2.get()) != 10 and len(txt_date1.get()) == 10:
                    messagebox.showwarning('Error','Verificar fecha de fin')
                elif len(txt_date1.get()) == 0 and len(txt_date2.get()) == 0:
                    tab2_plotter()
                elif len(txt_date1.get()) == 10 and len(txt_date2.get()) == 10:
                    tab2_plotter()
            else:
                messagebox.showwarning('Error','Los países deben ser distintos')
        
        def listbox_add():
            aux = tab3_listbox.size()
            if tab3_countries.get() in aux3_paises:
                tab3_listbox.insert(aux+1, tab3_countries.get())
                aux3_paises.remove(tab3_countries.get())
                setPaises_tab3.add(tab3_countries.get())
            elif aux == 0:
                messagebox.showwarning('Error al añadir','No se ha seleccionado un país')
            else:
                messagebox.showwarning('Error al añadir', 'El país ya fue añadido')
            tab3_countries.update()
            aux3_paises.update()
        
        def listbox_delete():
            if tab3_listbox.size() == 0:
                messagebox.showwarning('Error al eliminar', 'No hay países en la lista')
            elif len(tab3_listbox.curselection()) == 0:
                messagebox.showwarning('Advertencia','No ha seleccionado un país de la lista')
            else:
                aux_deleted = tab3_listbox.curselection()
                deleted_item = tab3_listbox.get(aux_deleted)
                tab3_listbox.delete(ANCHOR)
                aux3_paises.add(deleted_item)
                setPaises_tab3.pop(deleted_item)
            tab3_countries.update()
            aux3_paises.update()

        def tab3_date_verification():
            if tab3_listbox.size() == 0:
                messagebox.showwarning('Error al graficar','No hay países seleccionados')
            else:
                if len(txt_date1_tab3.get()) != 10 and len(txt_date2_tab3.get()) == 10:
                    messagebox.showwarning('Error','Verificar fecha de inicio')
                elif len(txt_date2_tab3.get()) != 10 and len(txt_date1_tab3.get()) == 10:
                    messagebox.showwarning('Error','Verificar fecha de fin')
                elif len(txt_date1_tab3.get()) == 0 or len(txt_date2_tab3.get()) == 0:
                    messagebox.showwarning('Error','Debe ingresar fechas válidas')
                elif len(txt_date1_tab3.get()) == 10 and len(txt_date2_tab3.get()) == 10:
                    tab3_plotter()
        
        def tab4_plotter():
            # Definimos funcion graficar la cual llamaremos desde el programa con sus respectivos parametros
            # Armamos un set con los paises que queremos graficar
            setPaises = setPaises_tab4
            cantidadPaises = len(setPaises)                                               #Almacenamos la cantidad de paises del set que viene por parametro
            
            plt.figure(figsize=(30, 20))                                                  # Tamaño del grafico

            x = []                                                                        # Tiempo (date)
      
            for i in range(cantidadPaises):                                               # Iteramos la cantidad de veces como paises fueron ingresados     
                nomPais = setPaises.pop()                                                   # Quitamos del set de Paises un pais y almacenamos su nombre en una variable

                # En la linea debajo filtramos el archivo para quedarnos solo con los datos del pais en cuestión con las fechas ingresadas por el usuario
                auxPais = df_archivo[((df_archivo['location'] == nomPais.title())) & ((df_archivo['date'] >= txt_date1_tab4.get()) & (df_archivo['date'] <= txt_date2_tab4.get()))]

                # Convertir el DataFrame a un Diccionario para trabajar mejor los datos.
                archivoPais = auxPais.to_dict("list")
                
                #Almacenamos la cantidad de datos que tiene nuestro diccionario     
                cantRegistrosPais = len(archivoPais["date"])

                x = []                                                                           # Tiempo (date)
                y = []                                                                           # Total de casos (total_cases)
                
                for j in range(cantRegistrosPais):                                                 # Iteramos la cantidad de veces como registros tiene nuestro diccionario
                    x.append(archivoPais["date"][j])                                               # Llenamos una variable que sera nuestro eje x con las fechas ya filtradas
                    y.append(archivoPais["total_cases"][j])                                        # Llenamos una variable que sera nuestro eje y con los casos totales ya filtrados                                         

                plt.xlabel('Tiempo / dias')                                                      # Etiqueta Eje X
                plt.ylabel('Casos / personas')                                                   # Etiqueta Eje Y
                plt.grid(axis='y')                                                               # Mostrar una grilla horizontal
                plt.yscale("log")
                plt.title("Casos totales detectados para Argentina y sus paises limítrofes")     # Titulo del grafico
                plt.plot(x, y, label=nomPais.title())                                            # Graficar Eje X. Se le asigna una etiqueta
                plt.xticks(rotation=70)                                                          # Le damos rotacion de 70° a la leyenda del eje x y mostramos cada 5 posiciones para que se vean claras las fechas 
                plt.legend(loc='upper center')                                                   # Decimos que la leyenda va a estar arriba centrada
            plt.show()

        # Descargar archivo desde repositorio.
        wget('https://covid.ourworldindata.org/data/ecdc/full_data.csv')

        # Campos CSV
        # date, location, new_cases, new_deaths, total_cases, total_deaths, weekly_cases, weekly_deaths, biweekly_cases, biweekly_deaths 
        
        # Convertir el archivo descargado a DataFrame.
        df_archivo = pandas.read_csv("full_data.csv")
        
        # Llenar conjunto con los paises existentes en el archivo para realizar los controles pertinentes.
        archivoPaises = df_archivo.to_dict("list")
        paisesDisponibles = set()
        for i in range(len(archivoPaises["location"])):
            paisesDisponibles.add(archivoPaises["location"][i])

        self.wind = window
        self.wind.title('Graficador Casos Covid')

        #Tab's creation

        tab_control = ttk.Notebook(self.wind)
        
        tab1 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Opción 1')
        tab_control.pack(expand=1, fill='both')        
        l1 = Label(tab1, text='Seleccione país a graficar')#.grid(row=0, sticky=W+E)
        tab1_country = Combobox(tab1, values= sorted(list(paisesDisponibles)), width=30)#.grid(row=1, sticky=W+E)
        tab1_graph_button = Button(tab1, command=tab1_plotter, text='Graficar')

        l1.pack()
        tab1_country.pack()
        tab1_graph_button.pack()

        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab2, text='Opción 2')
        tab_control.pack(expand=1, fill='both')
        l2 = Label(tab2, text='Seleccione paises a graficar')#.grid(row=0, sticky=W+E)
        label_frame_tab2 = ttk.Frame(tab2)
        l2_1 = Label(label_frame_tab2, text='Primer País:                                       ')
        l2_2 = Label(label_frame_tab2, text='       Segundo País:  ')
        combobox_frame_tab2 = ttk.Frame(tab2)
        tab2_country1 = Combobox(combobox_frame_tab2, values= sorted(list(paisesDisponibles)), width=30)#.grid(row=1, column=0, sticky=W+E)
        tab2_country2 = Combobox(combobox_frame_tab2, values= sorted(list(paisesDisponibles)), width=30)#.grid(row=1, column=1, sticky=W+E)
        l_optional = Label(tab2, text='Opcional:')
        text_entry_frame = ttk.Frame(tab2)
        entry_frame_help = ttk.Frame(tab2)
        txt_date1_help = Label(entry_frame_help, text='Primer fecha (AAAA-MM-DD):   ')
        txt_date2_help = Label(entry_frame_help, text='    Segunda fecha (AAAA-MM-DD):')
        txt_date1 = Entry(text_entry_frame, width=32)
        txt_date2 = Entry(text_entry_frame, width=32)
        tab2_graph_button = Button(tab2, command=tab2_date_verification, text='Graficar')
        
        l2.pack()
        label_frame_tab2.pack()
        l2_1.pack(side=LEFT)
        l2_2.pack(side=RIGHT)
        combobox_frame_tab2.pack()
        tab2_country1.pack(side=LEFT)
        tab2_country2.pack(side=RIGHT)
        l_optional.pack()
        entry_frame_help.pack()
        txt_date1_help.pack(side=LEFT)
        txt_date2_help.pack(side=RIGHT)
        text_entry_frame.pack()
        txt_date1.pack(side=LEFT)
        txt_date2.pack(side=RIGHT)
        tab2_graph_button.pack()

        tab3 = ttk.Frame(tab_control)
        buttons_frame = ttk.Frame(tab3)
        tab_control.add(tab3, text='Opción 3')
        tab_control.pack(expand=1, fill='both')
        l3 = Label(tab3, text='Seleccione paises a graficar')#.grid(row=0, sticky=W+E)
        aux3_paises = paisesDisponibles
        setPaises_tab3 = set()
        tab3_countries = Combobox(tab3, values= sorted(list(aux3_paises)), width=30)#.grid(row=1, column=0, sticky=W+E)
        b3_add = Button(buttons_frame, command=listbox_add, text='Agregar')#.grid(row=1, column=1, sticky=W+E)
        b3_delete = Button(buttons_frame, command=listbox_delete, text='Eliminar')
        tab3_listbox = Listbox(tab3)#.grid(row=2, sticky=W+E)
        l_tab3 = Label(tab3, text='Ingrese Fechas:')
        text_entry_frame_tab3 = ttk.Frame(tab3)
        entry_frame_help_tab3 = ttk.Frame(tab3)
        txt_date1_help_tab3 = Label(entry_frame_help_tab3, text='Primer fecha (AAAA-MM-DD):   ')
        txt_date2_help_tab3 = Label(entry_frame_help_tab3, text='    Segunda fecha (AAAA-MM-DD):')
        txt_date1_tab3 = Entry(text_entry_frame_tab3, width=32)
        txt_date2_tab3 = Entry(text_entry_frame_tab3, width=32)
        tab3_graph_button = Button(tab3, command=tab3_date_verification, text='Graficar')

        l3.pack()
        tab3_countries.pack()
        buttons_frame.pack()
        b3_add.pack(side=LEFT)
        b3_delete.pack(side=RIGHT)
        tab3_listbox.pack()
        l_tab3.pack()
        entry_frame_help_tab3.pack()
        txt_date1_help_tab3.pack(side=LEFT)
        txt_date2_help_tab3.pack(side=RIGHT)
        text_entry_frame_tab3.pack()
        txt_date1_tab3.pack(side=LEFT)
        txt_date2_tab3.pack(side=RIGHT)
        tab3_graph_button.pack()

        tab4 = ttk.Frame(tab_control)
        tab_control.add(tab4, text='Opción 4')
        tab_control.pack(expand=1, fill='both')
        l4 = Label(tab4, text='Paises que se graficarán:')#.grid(row=0, sticky=W+E)
        tab4_listbox = Listbox(tab4)#.grid(row=1, sticky=W+E)
        l_tab4 = Label(tab4, text='Fechas a graficar')
        text_entry_frame_tab4 = ttk.Frame(tab4)
        date1 = tkinter.StringVar()
        date1.set('2020-06-21')
        date2 = tkinter.StringVar()
        date2.set('2020-09-21')
        txt_date1_tab4 = Entry(text_entry_frame_tab4, width=32, textvariable=date1, state='readonly')
        txt_date2_tab4 = Entry(text_entry_frame_tab4, width=32, textvariable=date2, state='readonly')
        tab4_graph_button = Button(tab4, command=tab4_plotter, text='Graficar')

        l4.pack()
        tab4_listbox.pack()
        l_tab4.pack()
        text_entry_frame_tab4.pack()
        txt_date1_tab4.pack(side=LEFT)
        txt_date2_tab4.pack(side=RIGHT)
        tab4_graph_button.pack()

        setPaises_tab4 = {"Argentina", "Chile", "Bolivia", "Paraguay", "Brasil", "Uruguay"}        
        aux_setPaises = 1
        for i in sorted(setPaises_tab4):
            tab4_listbox.insert(aux_setPaises, i)
            aux_setPaises += 1        
        
        help_tab = ttk.Frame(tab_control)
        tab_control.add(help_tab, text='Ayuda')
        tab_control.pack(expand=1, fill='both')

        #Reading a .txt file with help for the help_tab
        t = open('help.txt', mode='r', encoding='UTF8').read()
        Label(help_tab, text=t).grid(row=0, sticky=W+E)
        
if __name__ == '__main__':
    window = Tk()
    window.geometry("1100x700")
    application = CovidDrawer(window)
    window.mainloop()