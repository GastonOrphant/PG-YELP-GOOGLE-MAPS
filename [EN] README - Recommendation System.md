# Recommendation System

## Index

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Installation Instructions](#installation-instructions)
- [Features](#features)
    - [Connection with Google Big Query](#conexión-entre-google-big-query-y-azure-data-factory)
    - [Azure Databricks](#conexion-entre-azure-databricks-y-azure-blob-storage)
    - [Machine Learning Model (ALS)](#modelo-de-machine-learning-y-su-entrenamiento-als)
    - [Recommendation System](#)
- [Usage](#Usage)    
- [Contributing](#Contributing)


# **Introduction**

The recommendation system was developed for end-consumers, i.e. users of Yelp and Google Maps platforms. This system takes the user ID registered on either platform and based on their reviews and location data, recommends a total of 5 restaurants all located near the user in question.

# **Technologies Used**

We generally used **Azure Databricks** and **Spark** libraries (dataframes and machine learning models among others) to develop the recommendation system. However, we use various **Azure** services to connect to our **Google Big Query data warehouse**, such as **Azure Data Factory** and **Azure Blob Storage** where we also backup the necessary (and unnecessary) data for our recommendation system.

Additionally, for the system demo, we use Python libraries such as **gradio** and **plotly**. The former is used for the demo itself, and the latter is used to generate a map with the geolocations of the recommended restaurants to the user.

# **Installation Instructions**

To install and use the recommendation system it is necessary to import the notebook Recommendation System.ipynb into the [Azure Databricks](https://azure.microsoft.com/es-es/products/databricks) service or similar.
In case of using Azure Databricks the steps are as follows:

1) If you do not have an Azure account, create an account from the following link: https://portal.azure.com/#home

2) Within the Azure portal, search for the Azure Databricks service.

3) Within Azure Databricks, click on **Create** to create a new Azure Databricks service.
![Creation of Databricks Service](/src/databricks.JPG)
    >**Note:** When creating the service, no specific configuration is required, so this configuration is left to the user's discretion and/or monetary capacity.

4) Once the service is created, click on it and then click on **Launch Workspace**. ![Workspace](/src/databricks2.JPG)

5) We will need to create a new cluster, for this we go to **New** and then select the option **Cluster**.
![New Cluster](/src/databricks3.jpg)

6) We leave in the following image the configuration used in our Cluster, however, do not hesitate to try using better types of nodes since for our project we used the cheapest node. Once the configuration is finished, click on Create Cluster.
![Create Cluster](/src/databricks4.jpg)

7) Once the Cluster is created, we go back to the left section, click on **New** and select the **Notebook** option.

8) We put the name we want to the notebook since we only create it to import the one we downloaded and select the Cluster created in step number 6.

9) Once we have created our notebook, we go to **File** at the top left (1) and then click on **Import**. ![Import Notebook](/src/databricks5.jpg)

10) To **open** our Notebook, we go to the left of the page, click on workspace, and our notebook named Recommendation System should appear. Double-click to open it. ![Open Notebook](/src/databricks6.jpg)
    >**Note:** It is necessary to replace the first variable **SECRET_KEY** with a value that must be requested by email to gaston.orphant@hotmail.com

11) Once the notebook is opened, we just have to click on the upper left button called **Run all** and wait a few minutes.

12) If we scroll down to the end of the notebook, we will see a demo of the recommendation system similar to the following: ![Demo](/src/databricks7.jpg)
I recommend copying the link marked in red in a new browser tab to view it better.
    >**Note:** This link will only work while the cluster is on.

# Features

In this section, we will describe the key features of the recommendation system, such as some technologies used to build the recommendation system, the connection between Google and Azure, data backup creation, among others.

## **Connection between Google Big Query and Azure Data Factory**

For the connection with our Datawarehouse, which is located in **Google Big Query**, we use the **Azure Data Factory** service to transform and copy the necessary tables for the recommendation system in **Azure Blob Storage**. Additionally, this will also serve as a **Backup** in case of any eventuality that may occur with the Google Cloud service.

The connection is made by generating **OAuth 2.0 credentials** for Azure in the Google Cloud repository, which are used from Azure Data Factory to make the connection with Big Query.

From Azure Data Factory, we also needed an **update key** for the data. For this, we used the **POSTMAN** program where by accessing a specific Google authorization website, keys were generated that, once ingested into **POSTMAN**, returned us the **update key** we needed.

### But what are all these technologies/services that we mentioned? Let's take a look at them:

- **Azure Data Factory:** It is a solution for building hybrid extraction-transformation-load (ETL) or extract-load-transform (ELT) pipelines.

- **Azure Blob Storage:** Provides storage for building powerful cloud-native applications while optimizing storage costs and allowing flexible data scalability.

- **POSTMAN:** It is an API platform for developers to design, build, test, and iterate their APIs. In our case, we communicate with the Google Cloud API to obtain an update key and not much more than that.


### **How did we establish the connection?**

To establish the connection, a pipeline was created in Azure Data Factory to read the data from Google Big Query on a daily basis (every 24 hours). This ensures that both our recommendation model and backup are up-to-date with the latest data ingested in the data warehouse.

We can divide the functioning of our pipeline into 3 steps:

1) **Data source:** In this step, we take the data from Google Big Query. ![](/src/pipeline-origen.png)

2) **Receiver of data:** Here we create a file that will receive our data. In our case, it will be a file called **ML_Reviews** of type *parquet*.
![](/src/pipeline-receptor.png)

3) **Data Mapping:** Once we have the source and destination of the data, we only need to assign the data from the source to the destination. Additionally, we can perform column transformations in case the data formats between Big Query and Azure Blob Storage are different.
![](/src/pipeline-asignacion.png)

Finally, we only had to create a **Trigger**. We configured it in the Triggers section of our Pipeline to have a frequency of 1 day.
![](/src/pipeline-timer.png)

## **Azure Databricks**

**Azure Databricks** is a data analysis platform. It is the optimized version of Databricks for Microsoft's cloud service. Using Apache Spark, it allows powerful analytical algorithms to be launched on large amounts of data in real-time.
 
### **Connection between Azure Databricks and Azure Blob Storage**

The connection between **Google Big Query** and **Azure Blob Storage**, although sufficient to have a backup of the data warehouse in another cloud service, is not enough for our recommendation system. We need to connect **Azure Blob Storage** with **Azure Databricks**. To do this, we only had to add a few lines of code to our notebook in Databricks:

In the few lines of code that we will see below, we have the configuration of our connection with Blob Storage. We can see that it is nothing more than passing certain links and credentials to finally be able to create a dataframe within our Databricks to perform our machine learning model.

![Conection](/src/blob-storage-databricks-conexion.png)
>**Note:** We have covered sensitive data in this image. 

### **In conclusion, our connection looks like this:**

![conection](/src/bigquery-datafactory.png)

Now that we've cleared this up, it's time to train our model.

## **Machine Learning Model(ALS) and Training it**
For our recommendation system, we opted for a **Collaborative Filtering** model.
In this type of model, two similar users A and B are compared, in our case based on their reviews of similar restaurants, to recommend to user A restaurants that user B visited and recommended, or vice versa.

![collaborative filtering](/src/collaborative-filtering.png)

### **ALS**

**ALS** or **Alternating Least Square** is the Machine Learning implementation that we use to train our recommendation system. It is a matrix factorization algorithm that works by decomposing the user-item interaction matrix into the product of two rectangular matrices of lower dimensionality. This type of algorithm is what companies like Netflix currently use to recommend movies to their users, as it has great scalability and allows various factors that influence the recommendation to be added to the model.

As **ALS** can only use IDs in numeric format, it was necessary to hash some of our columns, **user_id** and **business_id**, which were in string format.

We did this with the .hash function from Spark functions.

![hashing](/src/hashing-strings.png)

We proceeded to train the model with our hashed user ids and hashed business ids after all of this.

After training the model, we proceeded to evaluate the **root mean square error** (RMSE) of our model. Initially, we obtained an **RMSE** of approximately **8.81**, which was quite high in our opinion, so we decided to optimize the hyperparameters using the **CrossValidator** and **ParamGridBuilder** functions of Spark. Once this was done, along with some optimizations in our dataset, we arrived at a final RMSE of approximately **0.56**.

## **Recommendation system**

For the recommendation system, a few Python functions were developed, which are then used by **Gradio** in a functional **DEMO** of the system. In this way, we can show how the model would work with a simple but effective graphical interface.

We will explain each of these functions without going into too much technical detail:

- **id_hashed:** As the user will enter their user id in string format, it is necessary to find their previously hashed id, for which we use this function.

- **name_retriever:** We already know that ALS only works with numbers, therefore **ALS** will return the hashed restaurant id, with this function we find the name, latitude, and longitude of the restaurant that our model recommended so that we can show it to the user.

- **random user:** This function simply returns a random user id from our database. (Later we will see that it is used in a button of our **demo**)

- **mapped_coor:** Using the latitude and longitude coordinates returned by **name_retriever**, we use them to geolocate the different recommended restaurants on a map. This will also be seen used in our **demo**.


# **Usage Mode**

We can use the **Demo** in two ways. The first is by using the **"Get a Random User ID"** button, which will automatically obtain a user ID in the database, or by entering a known user ID from platforms such as Google Maps or Yelp that have made a previous review before 2021.

Once the ID is entered, we can use the **"Get recommendations!"** button to obtain 5 restaurants to go to based on the user's previous reviews and geolocation.

In addition, we can see a map with these same 5 restaurants by clicking on the **"Show on map"** button.
![Demo](/src/demo.jpg)
>**Note:** If you don't click "Show on map", an **ERROR** message will appear. It's not actually an error, but rather the map won't be displayed until you click on "Show on map".


# **Contributions**

If you want to contribute to this project, don't hesitate to write to me or any member of our team.

My email is gaston.orphant@hotmail.com, and I'm available for any questions you may have.
