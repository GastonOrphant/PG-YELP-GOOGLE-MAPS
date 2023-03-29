# Sistema de recomendación

## Indice

- [Introducción](#introducción)
- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Instrucciones de instalación](#instrucciones-de-instalación)
- [Características](#características)
    - [Conexión con Google Big Query](#conexión-entre-google-big-query-y-azure-data-factory)
    - [Azure Databricks](#conexion-entre-azure-databricks-y-azure-blob-storage)
    - [Modelo de Machine Learning (ALS)](#modelo-de-machine-learning-y-su-entrenamiento-als)
    - [Sistema de recomendación](#sistema-de-recomendacic3b3n-1)
- [Uso](#modo-de-uso)    
- [Contribuciones](#contribuciones)


# **Introducción**

Se desarrolló un sistema de recomendación para consumidores finales, es decir, usuarios de las plataformas de Yelp y Google Maps. Este sistema tomará el id del usuario registrado en alguna de las plataformas y basado en sus reseñas y la localización de las mismas se le recomendará un total de 5 restaurantes todos cercanos al usuario en cuestión.

# **Tecnologías utilizadas**

Para realizar el sistema de recomendación utilizamos generalmente **Azure Databricks** y librerias de **Spark** (dataframes y modelos de machine learning entre otras). Sin embargo utilizamos distintos servicios de **Azure** para conectarnos con nuestro datawarehouse de Google Big Query tales como **Azure Data Factory** y **Azure Blob Storage** donde, además, realizamos un backup de los datos del datawarehouse que son necesarios (y tambien de otros que no lo son) para nuestro sistema de recomendación.
Además para realizar la demo del sistema utilizamos las librerias de Python **gradio** y **plotly**. La primera para la demo en sí y la segunda para generar un mapa con las geolocalizaciones de los restaurantes recomendados al usuario.

# **Instrucciones de instalación**

Para instalar y utilizar el sistema de recomendación es necesario importar el notebook Recommendation System.ipynb dentro del servicio de [Azure Databricks](https://azure.microsoft.com/es-es/products/databricks) o similar.
En caso de utilizar Azure Databricks los pasos son los siguientes:

1) En caso de no poseer una cuenta de Azure crear una cuenta desde el siguiente link: https://portal.azure.com/#home

2) Dentro del portal de Azure buscar el servicio Azure Databricks.

3) Dentro de Azure Databricks darle click a **Crear** para crear un nuevo servicio de Azure Databricks.
![Creación de Servicio de Databricks](/src/databricks.JPG)
    > **Nota:** A la hora de crear el servicio no es necesaria ninguna configuración especifica por lo que esta configuración queda a criterio y/o capacidad monetaria del usuario.

4) Una vez creado el servicio hacerle click y luego hacer click en **Iniciar espacio de trabajo**. ![Espacio de Trabajo](/src/databricks2.JPG)

5) Deberemos crear un nuevo Cluster, para esto nos dirigimos a **New** y luego seleccionamos la opción **Cluster**.
![New Cluster](/src/databricks3.jpg)

6) Dejamos en la siguiente imagen la configuración utilizada en nuestro Cluster, sin embargo no duden en probar utilizar mejores tipos de nodos ya que para nuestro proyecto utilizamos el nodo mas barato. Una vez finalizada la configuración hacemos click en Create Cluster.
![Create Cluster](/src/databricks4.jpg)

7) Una vez creado el Cluster volvemos al apartado de la izquierda, clickeamos en **New** y seleccionamos la opción **Notebook**

8) Ponemos el nombre que queramos al notebook ya que solo lo creamos para importar el que bajamos y de Cluster elegimos el creado en el paso numero 6.

9) Una vez creado nuestro notebook vamos a **File** arriba a la izquierda (1) y luego hacemos click en **import**. ![Import Notebook](/src/databricks5.jpg)

10) Para **abrir** nuestro Notebook nos dirigimos a la izquierda de la pagina, hacemos click en workspace y deberá aparecernos nuestro notebook de nombre Recommendation System. Hacemos doble click para abrirlo. ![Open Notebook](/src/databricks6.jpg)
    >**Nota:** Es necesario reemplazar en la primer variable **SECRET_KEY** con un valor que debe ser pedido por mail a gaston.orphant@hotmail.com

11) Una vez abierto el notebook solo nos quedá darle click al botón superior izquierdo llamado **Run all** y esperar unos minutos. 

12) Si bajamos hasta el final de la notebook veremos una Demo del sistema de recomendación similar a la siguiente: ![Demo](/src/databricks7.jpg)
Recomiendo copiar el link marcado con rojo en una nueva pestaña del navegador para verlo mejor.
    >**Nota:** Este link solo funcionará mientras el cluster este encendido.

# Características

Es esta sección describiremos las caracteristicas claves del sistema de recomendación. Tales como algunas tecnologías utilizadas para la realización del sistema de recomendación, la conexión entre Google y Azure, la creación de un backup de datos entre otras.

## **Conexión entre Google Big Query y Azure Data Factory**

Para la conexión con nuestro Datawarehouse, el cual se encuentrá en Google Big Query, utilizamos el servicio de **Azure Data Factory** en pos de transformar y copiar las tablas necesarias para el sistema de recomendación en **Azure Blob Storage**. Además esto nos servirá tambien de **Backup** ante cualquier eventualidad que pueda pasar con el servicio de Google Cloud.

La conexión se da generando **credenciales OAuth 2.0** en el repositorio de Google Cloud para Azure las cuales se utilizan desde Azure Data Factory para realizar la conexión con Big Query.

Desde Azure Data Factory, además, se necesitaba una **clave de actualización** de los datos. Para esto se utilizó el programa **POSTMAN** en donde ingresando a una web especifica de autorización de Google se generaron claves que, una vez ingestadas en **POSTMAN**, nos devolvió la **clave de actualización** que necesitabamos.

### ¿Pero que son todas estas tecnologías/servicios que nombramos? Pasemos a ver un poco de ellas:

- **Azure Data Factory:** Es una solución para cuando se trata de construir tuberías híbridas (o pipelines) de extracción-transformación-carga (ETL) o de ELT.

- **Azure Blob Storage:** Provee almacenamiento para crear potentes aplicaciones nativas de la nube a la vez que optimiza costos de almacenamiento y permite una escalabilidad de los datos flexible.

- **POSTMAN:** Es una plataforma API para que los desarrolladores diseñen, construyan, prueben e iteren sus API. En nuestro caso nos comunicamos con la API de Google Cloud para poder obtener una clave de actualización y no mucho mas que eso.


### **¿Comó realizamos la conexión?**

Para realizar la conexión se creó un pipeline en Azure Data Factory en el cual se leen los datos de Google Big Query de forma diaria (cada 24 horas) De esta manera nos aseguramos que tanto nuestro modelo de recomendación como nuestro backup esten actualizados con los ultimos datos ingestados en el Datawarehouse.

Podemos dividir el funcionamiento de nuestro Pipeline en 3 pasos:

1) **Origen de los datos:** En este paso tomamos los datos desde Google Big Query. ![](/src/pipeline-origen.png)

2) **Receptor de los datos:** Aquí creamos un archivo que será el receptor de nuestros datos. En nuestro caso sera un archivo llamado ML_Reviews de tipo *parquet*.
![](/src/pipeline-receptor.png)

3) **Asignación de los datos:** Una vez que tenemos origen y receptor de datos solo nos queda asignar los datos del origen al receptor, además podemos realizar transformaciones de columnas en caso de que los formatos de datos entre Big Query y Azure Blob Storage sean distintos.
![](/src/pipeline-asignacion.png)

Por ultimo solo nos quedó crear un Trigger o desencadenador. Este lo configuramos en la seccion de Triggers de nuestro Pipeline para que tenga una perioricidad de 1 día.
![](/src/pipeline-timer.png)

## **Azure Databricks**

**Azure Databricks** es una plataforma de análisis de datos. Es la versión optimizada de Databricks para el servicio cloud de Microsoft. Utilizando Apache Spark permite lanzar potentes algoritmos analíticos sobre grandes cantidades de datos y en tiempo real. 
 
### **Conexion entre Azure Databricks y Azure Blob Storage**

La conexión entre Google Big Query y Azure Blob Storage si bien es suficiente para tener un Backup del datawarehouse en otro servicio cloud, no es suficiente para nuestro sistema de recomendación ya que ahora nos queda un ultimo pasito, conectar **Azure Blob Storage** con **Azure Databricks**. Para esto solo tuvimos que agregar unas pocas lineas de codigo a nuestro notebook en Databricks:

En las pocas lineas de codigo que veremos a continuación tenemos la configuración de nuestra conexión con Blob Storage. Podemos observar que no es mas que pasar ciertos links y credenciales para finalmente poder crear un dataframe dentro de nuestro Databricks para poder realizar nuestro modelo de machine learning.

![Conexion](/src/blob-storage-databricks-conexion.png)
>**Nota:** Hemos tapado datos sencibles en esta imagen. 

### **En conclusión nuestra conexión es algo así:**

![conexion](/src/bigquery-datafactory.png)

Ahora que ya aclaramos esto, es hora de entrenar nuestro modelo.

## **Modelo de Machine Learning y su entrenamiento (ALS)**
Para nuestro sistema de recomendación hemos optado por un modelo de **Collaborative Filtering** o filtrado colaborativo.
En este tipo de modelos se comparan dos usuarios similares A y B, en nuestro caso según sus reviews a restaurantes similares, para recomendarle al usuario A restaurantes que el usuario B visitó y recomienda o viceversa.

![collaborative filtering](/src/collaborative-filtering.png)

### **ALS**

**ALS** o **Alternating Least Square** es la implementación de Machine Learning que utilizamos para entrenar nuestro sistema de recomendación.
Se tratá de un algoritmo de factorización matricial los cuales funcionan descomponiendo la matriz de interacción usuario-elemento en el producto de dos matrices rectangulares de menor dimensionalidad.
Esté tipo de algoritmo es el que hoy en día utilizan empresas como **Netflix** para recomendarle a sus usuarios peliculas ya que cuenta con una amplia escalabilidad y permite agregarle al modelo diversos factores que influyen en la recomendación.

Como **ALS** solo puede utilizar ids en formato numerico fue necesario realizar un hash de algunas de nuestras columnas, **user_id** y **business_id**, las cuales se encontraban en formato *string*

Esto lo realizamos con la función .hash de Spark functions.

![hashing](/src/hashing-strings.png)

Una vez realizado todo esto procedimos a entrenar el modelo con nuestros hashed id's y hashed business id's.

Una vez entrenado el modelo procedimos a realizar una evaluación del **RMSE** o error cuadratico medio de nuestro modelo. En una primera instancia obtuvimos un RMSE de aproximadamente **8.81** un RMSE bastante alto para nuestro criterio por lo cual decidimos realizar una optimización de los hiper-parametros utilizando las funciones de **CrossValidator** y **ParamGridBuilder** de Spark. Una vez hecho esto y con algunas optimizaciones en nuestro dataset llegamos a un RMSE final de **0.56** aproximadamente.

## **Sistema de recomendación**

Para el sistema de recomendación se realizaron unas cuantas funciones en Python las cuales luego son utilizadas por **Gradio** en una **DEMO** funcional del sistema. De esta manera podemos mostrar como funcionaría el modelo con una interfaz grafica simple pero efectiva.

Vamos a explicar cada una de estas funciones sin entrar en detalles demasiado tecnicos:

- **id_hashed:** Como el usuario ingresará su id de usuario en formato string es necesario encontrar su id previamente hasheada, para eso utilizamos esta funcion.

- **name_retriever:** Ya sabemos que **ALS** solo funciona con numeros, por lo tanto ALS nos devolverá el id del restaurante hasheado, con esta función lo que hacemos es encontrar el nombre, la latitud y la longitud del restaurante que nuestro modelo recomendó para poder mostrarselo al usuario.

- **random user:** Está función simplemente devuelve un id de usuario aleatorio de nuestra base de datos. (Más adelante veremos que se utiliza en un botón de nuestra **demo**)

- **mapped_coor:** Utilizando las coordenadas de latitud y longitud devueltas por **name_retriever** las utilizamos para geolocalizar en un mapa los distintos restaurantes recomendados. Esto tambien lo veremos utilizado en nuestra **demo**


# **Modo de Uso**

Podemos utilizar la **Demo** de dos maneras. La primera utilizando el boton **"Get a Random User ID"** de manera que se obtendrá automaticamente un id de usuario en la base de datos ó ingresando un id de usuario ya conocido de las plataformas de Google Maps o Yelp que hayan hecho alguna review previo al 2021.

Una vez ingresada la id podemos utilizar el botón de **"Get recommendations!"** para obtener 5 restaurantes a los cuales ir basados en las reviews anteriores del usuario y a su geolocalización.

Además podemos ver un mapa con estos 5 mismos restaurantes si damos click al botón **"Show on map"**
![Demo](/src/demo.jpg)
>**Nota:** Si no se da click en "Show on map" se verá un cartel de **ERROR**. Realmente no se trata de un error sino de que el mapa no se está mostrando ni se mostrará hasta no hacer click en Show on map.


# Contribuciones

Si quieres contribuir en este proyecto no dudes en escribirme a mí o a cualquiera de nuestro equipo.

Mi mail es gaston.orphant@hotmail.com estoy a disposición por cualquier duda que tengas.
