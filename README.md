#Curso ITBA de Python
#Graficador de Casos COVID-19

Repositorio con archivos de resoluciones del proyecto integrador pedido por el Instituto Tecnologico de Buenos Aires.

Actividad:

Análisis y visualización de datos sobre los casos de coronavirus en distintos países.

En esta era de la desinformación puede resultar útil poder sacar uno mismo sus propias conclusiones acerca de los datos presentados. El objetivo de este trabajo es obtener datos de casos y muertes por el Coronavirus de un repositorio de datos online y graficar por país.

Funcionalidad mínima (requisito):

La aplicación debe recibir del usuario el nombre del país deseado y permitir graficar casos detectados y fallecimientos totales para ese país en función del tiempo.

El usuario debe poder ingresar 2 países y se permite graficar para dichos países la cantidad de casos y fallecimientos en dos gráficos con labels. El usuario debe poder ingresar el intervalo de tiempo a graficar. Calcular las intersecciónes entre gráficos si las hubiera y marcarlas con un punto de algún tipo.

El usuario debe poder ingresar n países y se permite graficar para dichos países la cantidad de casos en una escala logaritmica. El programa debe pedirle al usuario el intervalo de tiempo deseado.

Gráfico a entregar (requisito):

Gráficar sobre la misma imagen la cantidad de casos en una escala logaritmica de Argentina y todos sus países limítrofes (Chile, Bolivia, Paraguay, Brasil y Uruguay) durante los meses de invierno (21 de junio a 21 de septiembre). Debe quedar claro la curva que corresponde a cada país.


Funcionalidad opcional:

El programa debe permitir almacenar en un archivo excel los países ordenados de mayor cantidad de casos totales acumulados (al día de hoy) a menor cantidad de casos indicando en las distintas columnas el nombre del país, la cantidad de casos y los fallecimientos.

Almacenar en un archivo excel los países ordenados de mayor cantidad de casos totales acumulados a menor cantidad de casos indicando en las distintas columnas el nombre del país, la cantidad de casos y los fallecimientos colocando en distintas hojas del archivo excel (distintas pestañas) la evolución de este ranking, es decir armar una hoja distinta para cada día transcurrido. Defina los días a utilizar acorde a cuanta información se disponga, podría ser una entrada del usuario.

Para cada gráfico generado el usuario deberá poder ingresar un nombre de archivo y el programa genera un archivo .PNG del gráfico con el nombre indicado. (RESUELTO)

Crear una aplicación de consola que se ejecute continuamente recibiendo comandos del usuario, el usuario debe indicar el modo de operación que desea y el programa le pide los datos requeridos. Luego de finalizar la tarea el programa regresa al inicio y le pide al usuario el próximo comando. Incluír un comando de ayuda para que el programa indique al usuario cómo utilizarlo. Incluír un comando de salida que provoca la finalización del programa. (RESUELTO)