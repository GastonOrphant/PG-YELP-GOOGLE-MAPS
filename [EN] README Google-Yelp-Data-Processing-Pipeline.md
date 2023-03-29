# **Data Processing**

One of the most important things on this project is the treatment and organization of the data. The following shows the data processing scheme. 

<img src="./src/Data_Warehouse.png" alt="Data Warehouse Process">

## Parts of the Process

- [Data Lake](#data-lake)
- [Cloud Functions](#cloud-functions)
- [Data Warehouse](#data-warehouse)
- [Technologies](#technologies)

## Data Lake

The beginning part of this project is to upload raw data that was given to us and store it into our Data Lake.
</br>
**What is a Data Lake ?**
</br>
A Data Lake is a data storage system that allows large amounts of data to be stored in its native format, without the need for prior structuring, allowing faster and more flexible access to data. We are going to use Google Cloud Storage to store the raw data of Google & Yelp.
</br>
**Why Google Cloud Storage ?**
</br>
We chosed Google Cloud Services in general, because they have an amazing UI, very easy to use and very complete. Also and important fact is their competitive prices, We found no reason to don't Google Cloud Services.
</br>

<p align=center><img src="./src/Data_Lake_Screenshot.PNG" alt="Data Lake"></p>


## Cloud Functions

Google Cloud Functions service will do the task of extracting the data from the Data lake, transforming/cleaning and loading it in our Data Warehouse, which will be explained in detail later.
</br>
**Why We used Google Cloud Functions?**
</br>
We used Cloud Functions because it will help us to automate the ETL process. The functions stored there will be associated to a trigger, that trigger consist into detect when a new file is uploaded into our Data Lake, after that the Transformation functions will do their job and will clean and transform the raw data and store the processed data into our Data Warehouse.
</br>
Also it will automate the add of new data. One of the functions will clean/transform this new external data and will run a query in Google BigQuery to update the currently data.

<p align=center><img src="./src/Cloud_Functions.PNG" alt="Cloud Functions"></p>

## Data Warehouse
**What is the Google BigQuery service?**
</br>
Google BigQuery is a Data Warehouse Google Service that We are going to use to store and struct our processed data. Using Google SQL We will be able to make our own queries. Data Scientist team and Data Analytics team will use this structured data for their different needs.
</br>
The Data Warehouse will be able to be updated with new data at anytime from external sources. In this project, to increase our data, We will extract new data from an API. This process will be addressed in the section referring to the API.

</br>

<p align=center><img src="./src/Data_Warehouse_Screenshot.PNG" alt="Data Warehouse"></p>

## Technologies

* Google Cloud Plataform (GCP)
* Google Cloud Storage
* Google Cloud Function
* Google BigQuery
* Pandas
* Python

# Añadir que también se cuenta con una función que actualizará la data de la tabla principál con la data nueva ingresada.


