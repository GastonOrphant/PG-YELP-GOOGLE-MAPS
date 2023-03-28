# Documentación Dashboard

#### En la presente documentación encontrarán información pertinente a la elaboración del dashboard interactivo como parte de las actividades desarrolladas en este proyecto. Dicha información estará compuesta por una serie de conceptos más una descripción de los datos utilizados, su estructuración y las tecnologías empleadas para tal fin. Finalmente, una guía detallada de los elementos del dashboard y sus funcionalidades.

LINK Dashboard: https://app.powerbi.com/links/jU9zNSC0Ol?ctid=85430b7f-f12c-48f1-b10e-f34a99e68727&pbi_source=linkShare
___
<br>

## Índice:
1.   Stack Tecnologico
<br>

2.   ¿Que es un Dashboard?
<br>

3.   Objetivos del Dashboard.
<br>

4.   ¿Que es Power Bi y porqué lo usamos?
<br>

5.   Obtención de los datos y Conexión Big Query.
<br>

6.   Estructura de las tablas y Diccionario de datos.
<br>

7.   Dashboard: Elementos y funcionalidades.  
<br>

## Stack Tecnológico

Para la realización del proyecto, el departamento de Data Analytics hizo uso del siguiente stack tecnológico:

**[Google colab](https://colab.research.google.com/)**: Producto de Google. Colab permite que todos puedan escribir y ejecutar código arbitrario de Python en el navegador. Aqui se realizo el anlisis exploratorio de datos (EDA)

**[Google Cloud Platform](https://cloud.google.com/?hl=es)**: Es un servicio ofrecido por Google , es un conjunto de servicios en la nube que se ejecuta en la misma infraestructura que Google.

**[Google Meet](https://meet.google.com/)**: Es un servicio de reuniones virtuales desarrollado por Google.

**[Power BI](https://powerbi.microsoft.com/en-au/)**: Es un producto de software de visualización de datos interactivo desarrollado por Microsoft.

**[Trello](https://trello.com/create-first-team)**: Software de organización de proyectos en la web.

**[Discord](https://discord.com/)**: Es un servicio de mensajería instantánea y chat de voz. Funciona a través de servidores y está separado en canales de texto o de voz.

**[Python](https://www.python.org/)**: Lenguaje de programación, aplicado a lo ancho y largo del proyecto.

**[Pandas](https://pandas.pydata.org/)** : Pandas es una libreria escrita para el lenguaje Python para la manipulación y el análisis de datos.

**[Matplotlib](https://matplotlib.org/)**: Matplotlib es una libreria en Python  para crear visualizaciones de nuestros datos.

**[Seaborn](https://seaborn.pydata.org/)**: Seaborn es una libreria de visualización de datos de Python basada en matplotlib.



## ¿Que es un Dashboard?

Un dashboard es una interfaz gráfica interactiva que proporciona una vista a la información clave y métricas relevantes. Nos ayuda para monitorear y analizar el       desempeño de una empresa. Puede incluir gráficos, tablas, mapas, indicadores clave (KPI), diagramas, entre otros elementos visuales que se disponen, esto para         tener una vista rápida y clara de la información que se necesita para una mejor toma de decisiones. 


## Objetivos del Dashboard

El objetivo principal del Dashboard es proporcionar una vista visual y facil de entender de la información de una empresa en tiempo real, también nos sirve para monitorear el desesmpeño de un proyecto, identificar tendencias, oportunidades y tomar decisiones estrategicas. Con el Dashboard buscamos mejorar la eficiencia y efectividad en la toma de decisiones de una empresa. 

Algunos objetivos que buscamos alcanazar con el Dashboard son los siguientes:

* **Visualizar los datos**: Presentar información de manera clara y concisa a través de gráficos, tablas, mapas y otros elementos visuales.
* **Monitorear el desempeño**: Proporcionar una visión general del rendimiento de la empresa en tiempo real.
* **Comunicar el progreso**: Mostrar el progreso de la empresa en relación con los objetivos establecidos, permitiendo a los usuarios identificar áreas de mejora y hacer ajustes.
* **Identificar problemas**: Permitir a los usuarios detectar rápidamente los problemas y las áreas que necesitan mejoras, y tomar medidas para resolverlos.



## Que es Power Bi y porqué lo usamos?

Power BI es una plataforma de inteligencia de negocios desarrollada por Microsoft que permite a los usuarios conectar, analizar y visualizar datos de manera rápida y fácil. Proporciona visulizaciones interactivas, paneles de control para monitorear la información. 

¿Porque lo usamos?, la decisión de usar este software es por nuestra experiencia previa en la realización de Dashboard para antiguos trabajos, también por su interfaz dado que es de un uso facil, intuitiva e interactiva.


## Obtención de los datos y Conexión BigQuery

Una vez realizada todas las tranformaciones pertinentes a los datos a través del departamento de Data Engineer, alojaran los datos en el DataWarehouse desarrollado en Google Cloud Platform. Una vez ahi Los datos se ingestaran directamente hacia Power BI a través de la conección que nos deja realizar este software con nustra base de datos. Para luego comenzar a trabajarlos y poder crear el mejor producto posible.

![Foto camino del dato ](https://user-images.githubusercontent.com/65837646/228130436-3e91a743-82e4-44aa-8edc-d56ce0d84043.jpg)





## Estructura de tablas y Diccionario de datos

* **Estructura de tablas**
* **Diccionario de datos**








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

Como se observa en la figura de arriba, en la parte superior se encuentran 5 KPIs. Los 5 muestran a modo de ejemplo, el periódo de 6 meses comprendido entre las fechas 31/12/2018 y 30/06/2019.  
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

