# Dashboard Documentation

#### In this documentation you will find information relevant to the development of the interactive dashboard as part of the activities developed in this project.This information will be composed of a series of concepts plus a description of the data used, its structuring and the technologies used for this purpose. Finally, a detailed guide to the dashboard elements and their functionalities.

LINK Dashboard: https://app.powerbi.com/links/jU9zNSC0Ol?ctid=85430b7f-f12c-48f1-b10e-f34a99e68727&pbi_source=linkShare
___
<br>

## Index
1.   Technology stack
<br>

2.   What is a dashboard?
<br>

3.   Dashboard objectives
<br>

4.   What is Power Bi and why do we use it?
<br>

5.   Data collection and BigQuery connection.
<br>

6.   Table structure and data dictionary.
<br>

7.   Dashboard: Elements and functionality.  
<br>

## Technology stack

For the realization of the project, the Data Analytics department made use of the following technological stack:

**[Google colab](https://colab.research.google.com/)**: Google product. Colab allows everyone to write and execute arbitrary Python code in the browser.
Exploratory data analysis (EDA) was performed here.

**[Google Cloud Platform](https://cloud.google.com/?hl=es)**: It is a service offered by Google, is a set of cloud services that runs on the same infrastructure 
as Google.

**[Google Meet](https://meet.google.com/)**: It is a virtual meeting service developed by Google.

**[Trello](https://trello.com/create-first-team)**: Web-based project management software.

**[Discord](https://discord.com/)**: It is an instant messaging and voice chat service. It works through servers and is separated into text and voice channels.

**[Python](https://www.python.org/)**: Programming language, applied throughout the project.

**[Pandas](https://pandas.pydata.org/)**: Pandas is a library written for the Python language for data manipulation and analysis.

**[Matplotlib](https://matplotlib.org/)**: Matplotlib is a Python library for creating visualizations of our data.

**[Seaborn](https://seaborn.pydata.org/)**: Seaborn is a Python data visualization library based on matplotlib.



## What is a dashboard?

A dashboard is an interactive graphical interface that provides a view of key information and relevant metrics. It helps us to monitor and analyze the performance 
of a company. It can include graphs, tables, maps, key performance indicators (KPIs), diagrams, among other visual elements that are available, in order to have 
a quick and clear view of the information needed for better decision making.

## Dashboard objectives

The main objective of the Dashboard is to provide a visual and easy to understand view of a company's information in real time, it also serves to monitor 
the performance of a project, identify trends, opportunities and make strategic decisions. With the Dashboard we seek to improve the efficiency and effectiveness 
of a company's decision making. 

Some of the objectives we seek to achieve with the Dashboard are the following:

* **Visualize data**: Present information in a clear and concise manner through graphs, charts, maps and other visual elements.
* **Monitor performance**: Provide an overview of the company's performance in real time.
* **Communicate progress**: Show the company's progress against established objectives, allowing users to identify areas for improvement and make adjustments.
* **Identify problems**: Enable users to quickly spot problems and areas needing improvement, and take action to resolve them.


## What is Power Bi and why do we use it?

Power BI is a business intelligence platform developed by Microsoft that allows users to connect, analyze and visualize data quickly and easily. It provides 
interactive visualizations, dashboards to monitor information. 

Why we use it, the decision to use this software is because of our previous experience in the realization of Dashboard for old jobs, also for its interface 
since it is easy to use, intuitive and interactive.

## Data collection and BigQuery connection.

Once all the relevant transformations have been made to the data through the Data Engineer department, the data will be hosted in the DataWarehouse developed 
in Google Cloud Platform. Once there, the data will be ingested directly to Power BI through the connection that this software allows us to make with our database. 
Then we can start working on them and create the best possible product.


![Foto camino del dato ](https://user-images.githubusercontent.com/65837646/228283492-829ce4b3-9fb2-4027-a10d-3ae15ed79ae8.jpg)


## Table structure and data dictionary.

## Dashboard: Elements and functionality. 
<br>

### Our dashboard is divided into 2 pages. The first one has the mission of providing the user with the relevant information about the KPIs, as well as the visualization of the metrics that compose them through graphs.  
<br>
<br>
<br>

<img src="https://user-images.githubusercontent.com/109149292/228099508-57fccff2-8efd-45e9-ad75-8313ebfc7f2b.jpg" alt="Descripción de la imagen" width="75%"> 
<br>
<br>

### The second page is composed of graphic elements aimed at showing trends, through the comparison of historical metrics.<br>
<br>

<img src="https://user-images.githubusercontent.com/109149292/228101816-9f1577e4-e837-4f5b-8751-c05a2eecc2bb.jpg" alt="Descripción de la imagen" width="75%"> 
<br>

<br>

### We will now analyze the elements of these pages in detail.<br>
<br>
<br>

<img src="https://user-images.githubusercontent.com/109149292/228102033-9a46c8cc-d1cf-4834-af6c-bd572138f9dd.jpg" alt="Descripción de la imagen" width="75%">
<br>
<br>

## Number 1: KPIs
<br>

As can be seen in the figure above, at the top are 5 KPIs. The 5 show by way of example, the 6 month period between the dates 31/12/2018 and 30/06/2019.  
The elements within the 5 figures are the same. On one side the title of the metric to which reference is made, followed by the value of the metric, which is shown in green or red depending on whether the proposed objective has been met or not respectively.  
Immediately below the value is the target or objective, which is nothing more than the value of the metric at the beginning of the period plus a percentage to be reached at the end of the period.  
To the right of the target is a value that shows the numerical and percentage difference between the current value of the metric and the target, in this way we can specifically observe the deficit or superhabit achieved.  
Finally we will find the date to which the observed KPI value belongs.<br>
<br>

## Number 2: Top 10 companies filter.
<br>

On the far left below the KPIs is a bar chart showing the top 10 companies based on the number of reviews obtained from users.  
In addition to showing the most popular companies or those with the highest visibility, this graph has a built-in filter function, as can be seen in the following figures.
the following figures, where by clicking on the bar or (Ctrl + click) to select multiple companies, the other elements and graphs are updated, 
making visible the information pertaining to the company/companies.<br>
<br>

<img src="https://user-images.githubusercontent.com/109149292/228108996-c544fe6b-793b-4214-a358-c35d134fa3fe.jpg" alt="Descripción de la imagen" width="40%"> 
<br>

<img src="https://user-images.githubusercontent.com/109149292/228109094-a45894f2-96b9-478d-a2d3-01ef4ca92b46.jpg" alt="Descripción de la imagen" width="75%"> 

<br>
<br>

## Number 3: Map.
<br>

On the far right below the KPIs is a map with the locations of each company's stores classified by color according to the state to which they belong. 
they belong to.  
The size of the dots, also called bubbles, varies according to the number of reviews a specific location has. So it is an effective visual guide to choose locations strategically. 
when choosing locations strategically.
<br>
<br>

## Number 4: Graphics.
<br>

At the bottom you can see 3 graphs.  
A bar graph that shows the number of reviews per state. This graph allows us to select a state as a filter by clicking, and multiple states by clicking (Ctrl + click).
multiple states by clicking (Ctrl + click). In this way the other graphs are updated according to the selected states as shown in the following figures.
<br>
<br>
<br>

<img src="https://user-images.githubusercontent.com/109149292/228112153-3d6c2225-0755-4405-a3f8-2d6c82e1abab.jpg" alt="Descripción de la imagen" width="75%"> 
<br>
<br>

In addition to the above, we can also see two pie charts showing the percentages of the different values of the rating (1 to 5 stars) and feeling (positive, negative, neutral) fields. 
feeling (positive, negative, neutral).
<br>

## Page 2.
<br>
<br>

<img src="https://user-images.githubusercontent.com/109149292/228102988-00a3120d-36c1-4c4f-9cb7-a8358470af6e.jpg" alt="Descripción de la imagen" width="75%">

<br>
<br>

## Numbers 1 and 2 - Page 2:
<br>

On the second page we can see 4 new elements in addition to the KPIs and the Top 10.  
The first one is a line chart showing the trend of the average Rating over the last years, with a trend line, 
It has a trend line, plus historical minimum and maximum lines in red and green respectively.  
As shown in the following figure, it also has control bars with which it is possible to enlarge a range of values on both axes to be studied in detail. 
in detail.
<br>
<br>

<img src="https://user-images.githubusercontent.com/109149292/228109132-df3d038c-5dea-4436-b7fd-8a973a439085.jpg" alt="Descripción de la imagen" width="75%"> 

<br>
The second graph contains the same functionalities as the first one, and shows the trend of the number of reviews by date. 
<br>

## Numbers 3 and 4 - Page 2:
<br>

Items 3 and 4 are grouped bar charts.  
Number 3 shows the relationships between the number of reviews and the rate of response to them by locals over time. Number 4 shows the comparison between positive and negative reviews,
shows the comparison between positive and negative reviews by date.
