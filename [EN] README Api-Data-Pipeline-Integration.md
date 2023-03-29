# Api-Data-Pipeline-Integration
One of the main objectives of this project is the enrichment of static data from Google Maps and Yelp, through API.
<br>
<br>
<p align=center><img width="80%" src="https://github.com/hikikae/Api-Data-Pipeline-Integration/blob/main/src/API-Data-Pipeline-Integration.png"></p><br>

## ✨ Process Elements
- [Cloud Scheduler1](#Cloud-Scheduler1)
- [Cloud Function (Get_API_Data)](#Cloud-Function-(Get_API_Data))
- [Cloud Storage (Data Lake)](#Cloud-Storage-(Data-Lake))
- [Segunda Cloud Function (ETL_API_Function)](#Segunda-Cloud-Function-(ETL_API_Function))
- [Cloud Scheduler2](#Cloud-Scheduler2)
- [Cloud Storage (Data Warehouse)](#Cloud-Storage-(Data-Warehouse))
- [Slack API (Notificación)](#Slack-API-(Notificación))

<div id='Cloud-Scheduler1'/>

### Cloud Scheduler
Cloud Scheduler is used to define a data update schedule for automatic loading of the data. An HTTP endpoint is called to execute the Cloud Function responsible for loading data from the API. The triggers section contains the URL for this purpose.

<br>
<p align=center><img width="80%" src="https://github.com/hikikae/Api-Data-Pipeline-Integration/blob/main/src/Cloud_Scheduler.gif"></p><br>

<div id='Cloud-Function-(Get_API_Data)'/>

### <a href="https://github.com/GastonOrphant/PG-YELP-GOOGLE-MAPS/tree/main/Api-Data-Pipeline-Integration/Get_API_Data"> Cloud Function (Get_API_Data)</a>
The first Cloud Function obtains and stores relevant restaurant information. It uses the Geocoding API to obtain the coordinates of certain cities in the five most densely populated states in the United States. Then, the Places API extracts the restaurant data. 

<br>
<p align=center><img width="80%" src="https://github.com/hikikae/Api-Data-Pipeline-Integration/blob/main/src/details_review_data.gif"></p><br>

An HTTP request triggers the Cloud Function.

<br>
<p align=center><img width="80%" src="https://github.com/hikikae/Api-Data-Pipeline-Integration/blob/main/src/details_review_data_trigger.png"></p><br>

It is important to note that both the Geocoding API and the Places API are provided by Google and require valid API credentials to function correctly.
<br>

<div id='Cloud-Storage-(Data-Lake)'/>

### Cloud Storage (Data Lake)
The data is collected in its original form, without prior processing, in a JSON format and stored together with the static data in the Cloud Storage bucket, that is, the Data Lake.

<br>
<p align=center><img width="80%" src="https://github.com/hikikae/Api-Data-Pipeline-Integration/blob/main/src/datalake.png"></p> <br>

<div id='Segunda-Cloud-Function-(ETL_API_Function)'/>

### <a href="https://github.com/GastonOrphant/PG-YELP-GOOGLE-MAPS/tree/main/Api-Data-Pipeline-Integration/ETL_API_function"> Cloud Function (ETL_API_Function) </a>
The second Cloud Function carries out the transformation, cleaning, and loading of the original data using the Pandas library. Once the process is complete, the data is sent to a Cloud Storage Bucket, and a notification is issued in Slack to inform about the completion of the process.

<br>
<p align=center><img width="80%" src="https://github.com/hikikae/Api-Data-Pipeline-Integration/blob/main/src/ETL_function.gif"></p> <br>

<div id='Cloud-Scheduler2'/>

### Cloud Scheduler
An hour after the ETL process, a query is executed to add the new data to the main table that already contains the static data.

<br>
<p align=center><img width="80%" src="https://github.com/hikikae/Api-Data-Pipeline-Integration/blob/main/src/scheduler_query.png"></p> <br>

<div id='Cloud-Storage-(Data-Warehouse)'/>

### Cloud Storage (Data Warehouse)
Once the data transformation processes are complete, the data is made available in a bucket that serves as our Data Warehouse. This approach facilitates collaboration and the sharing of valuable information between teams and contributes to making informed decisions based on accurate and up-to-date data.

<br>
<p align=center><img width="80%" src="https://github.com/hikikae/Api-Data-Pipeline-Integration/blob/main/src/datawarehouse.png"></p> <br>

<div id='Slack-API-(Notificación)'/>

### Slack API
The Slack integration is used to send a notification about the data upload process to avoid the need to constantly monitor the GCP platform. The URL of the webhook to execute the notification is unique and specific to each project.

<br>
<p align=center><img width="80%" src= "https://github.com/hikikae/Api-Data-Pipeline-Integration/blob/main/src/slack_api.gif"></p><br>

##  🛠️ Technologies 
- Google Cloud Plataform (GCP)
- Cloud Scheduler
- Cloud Function
- Cloud Storage
- Pandas
- Slack API
- Python

