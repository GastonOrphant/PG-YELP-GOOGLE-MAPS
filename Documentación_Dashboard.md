# Documentación Dashboard

#### En la presente documentación encontrarán información pertinente a la elaboración del dashboard interactivo como parte de las actividades desarrolladas en este proyecto.Dicha información estará compuesta por una serie de conceptos más una descripción de los datos utilizados, su estructuración y las tecnologías empleadas para tal fin. Finalmente, una guía detallada de los elementos del dashboard y sus funcionalidades.

LINK Dashboard: https://app.powerbi.com/links/jU9zNSC0Ol?ctid=85430b7f-f12c-48f1-b10e-f34a99e68727&pbi_source=linkShare
___
<br>

## Índice:
1.   ¿Que es un Dashboard?
<br>

2.   Objetivos del Dashboard.
<br>

3.   ¿Que es Power Bi y porqué lo usamos?
<br>

4.   Obtención de los datos y Conexión Big Query.
<br>

5.   Estructura de las tablas y Diccionario de datos.
<br>

6.   Dashboard: Elementos y funcionalidades.  
<br>

## ¿Que es un Dashboard?

## Objetivos del Dashboard

## Que es Power Bi y porqué lo usamos?

## Obtención de los datos y Conexión BigQuery

## Estructura de tablas y Diccionario de datos

## Dashboard: Elementos y funcionalidades.
<br>

### Nuestro dashboard está dividido en 2 páginas. La primera posee la misión de darle al usuario la información pertinente a los KPIs, así también como la visualización a través de gráficas, de las métricas que los componen.  
<br>
<br>
<br>

<img src="https://user-images.githubusercontent.com/109149292/228099508-57fccff2-8efd-45e9-ad75-8313ebfc7f2b.jpg" alt="Descripción de la imagen" width="75%"> 
<br>
<br>

### La segunda página está compuesta por elementos gráficos orientados a evidenciar tendencias, a través de la comparativa de métricas históricas.<br>
<br>

<img src="https://user-images.githubusercontent.com/109149292/228101816-9f1577e4-e837-4f5b-8751-c05a2eecc2bb.jpg" alt="Descripción de la imagen" width="75%"> 
<br>

<br>

### A continuación analizaremos en detalles los elementos de dichas páginas.<br>
<br>
<br>

<img src="https://user-images.githubusercontent.com/109149292/228102033-9a46c8cc-d1cf-4834-af6c-bd572138f9dd.jpg" alt="Descripción de la imagen" width="75%">
<br>
<br>

## Número 1: KPIs
<br>

Como se obserba en la figura de arriba, en la parte superior se encuentran 5 KPIs. Los 5 muestran a modo de ejemplo, el periódo de 6 meses comprendido entre las fechas 31/12/2018 y 30/06/2019.  
Los elementos dentro de las 5 figuras son los mismos. Por un lado el título de la métrica a la cual se hace referencia, seguido por el valor de la misma, el cual figura en verde o rojo dependiendo de si se ha cumplido con el objetivo propuesto o no respectivamente.  
Inmediatamente por debajo del valor se encuentran el target u objetivo el cual no es otra cosa que el valor de la métrica al inicio del periodo mas un porcentaje que se pretenda alcanzar al finalizar el mismo.  
A la derecha del target se encuentra un valor que muestra la diferencia numérica y porcentual entre el valor actual de la métrica y el target, de esta manera se puede observar específicamente el déficit o superhabit alcanzado.  
Finalmente nos encontraremos con la fecha a la cual pertenece el valor del KPI observado.<br>
<br>

## Número 2: Filtro Top 10 empresas.
<br>

En el extremo izquierdo por debajo de los KPIs nos encontramos con un gráfico de barras que nos muestra el top 10 de empresas en función de la cantidad de reviews obtenidas de los usuarios.  
Además de evidenciar aquellas empresas más populares o con mayor visibilidad, dicha gráfica tiene incorporada una funcionalidad de filtro, tal y como se puede ver en las siguientes figuras, donde al hacer click sobre la barra o (Ctrl + click) para elegir múltiples empresas, los demás elementos y gráficas se actualizan, haciendo visible la información perteneciente a la/las mismas.<br>
<br>

<img src="https://user-images.githubusercontent.com/109149292/228108996-c544fe6b-793b-4214-a358-c35d134fa3fe.jpg" alt="Descripción de la imagen" width="40%"> 
<br>

<img src="https://user-images.githubusercontent.com/109149292/228109094-a45894f2-96b9-478d-a2d3-01ef4ca92b46.jpg" alt="Descripción de la imagen" width="75%"> 

<br>
<br>

## Número 3: Mapa.
<br>

En el extremo derecho por debajo de los KPIs se encuentra un mapa con las ubicaciones de los locales de cada empresa clasificados por colores según el estado al cual pertenezcan.  
El tamaño de los puntos, también llamados burbujas, varía según la cantidad de reviews que posea dicho local en específico. Por lo que es una guía visual eficaz a la hora de elegir locaciones estrategicamente.
<br>
<br>

## Número 4: Gráficas.
<br>

En el extremo inferior se pueden visualizar 3 gráficos.  
Un gráfico de barras que nos muestra la cantidad de reviews por estado. Este mismo a su vez nos permite seleccionar un estado a modo de filtro al hacer click, y múltiples estados al hacer (Ctrl + click). De esta manera las demas gráficas se actualizan según los estados seleccionados como se muestra en las siguientes figuras.
<br>
<br>
<br>

<img src="https://user-images.githubusercontent.com/109149292/228112153-3d6c2225-0755-4405-a3f8-2d6c82e1abab.jpg" alt="Descripción de la imagen" width="75%"> 
<br>
<br>

Sumado a lo anterior también podemos ver dos gráficos circulares que muestran los porcentajes de los distintos valores de los campos rating (1 a 5 estrellas), y feeling (positivo, negativo, neutro).
<br>

## Página 2.
<br>
<br>

<img src="https://user-images.githubusercontent.com/109149292/228102988-00a3120d-36c1-4c4f-9cb7-a8358470af6e.jpg" alt="Descripción de la imagen" width="75%">

<br>
<br>

## Números 1 y 2 - Pág2:
<br>

En la segunda página podemos ver 4 nuevos elementos además de los KPIs y el Top 10.  
El primero de ellos es un gráfico de líneas que nos muestra la tendencia del promedio de Rating a lo largo de los últimos años, cuenta con una línea de tendencia, sumado a líneas de mínima y máxima histórica en rojo y verde respectivamente.  
Como se muestra en la siguiente figura, también posee barras de control con las cuales es posible agrandar un rango de valores en ambos ejes que se quiera estudiar en detalle.
<br>
<br>

<img src="https://user-images.githubusercontent.com/109149292/228109132-df3d038c-5dea-4436-b7fd-8a973a439085.jpg" alt="Descripción de la imagen" width="75%"> 

<br>
El segundo gráfico contiene las mismas funcionalidades que el primero, y muestra la tendencia de la cantidad de reviews según la fecha. 
<br>

## Números 3 y 4 - Pág2:
<br>

Los elementos 3 y 4 son gráficos de barras agrupadas.  
El número 3 muestra las relaciones entre cantidad de reviews y la tasa de respuestas a las mismas por parte de los locales, a lo largo del tiempo. El 4 por su parte, muestra la comparativa entre comentarios positivos y negativos según la fecha.

