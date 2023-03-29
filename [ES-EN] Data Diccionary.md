# **Spanish**

## **Diccionario de Datos**

### **Plataforma Google Maps**:


**Platform_reviews**

//user_id: String, id de usuario que realiza la reseña.

//business_id: String, id del local.

//local_name: String, nombre del local.

//latitude: Float, latitud del local.

//longitude: Float, longitud del local.

//num_of_reviews: Int, número total de reseñas de un local.

//state: String, estado donde se encuentra el local.

//main_category: String, categoría principal del local.

//rating: Int, calificación otorgada por el usuario de 1 a 5.

//opinion: String, reseña del usuario.

//feeling: String, comentario etiquetado como positivo o negativo.

//platform: String, plataforma origen de los datos.






**Reviews**

//user_Id: String, id de usuario que realiza la reseña.

//date: Timestamp, fecha de publicación de la reseña en formato YYYY/MM/DD.

//rating: Int, calificación otorgada por el usuario de 1 a 5.

//opinión: String, reseña del usuario.

//resp: String, respuesta del local.

//gmap_id: String, ubicación geográfica del local.

//feeling: String, comentario etiquetado como positivo o negativo.

//state: String, estado donde se encuentra el local.





**Google**

//user_id: String, id de usuario que realiza la reseña.

//business_id: String, id del local. 

//local_name: String, nombre del local.

//latitude: latitud del local.

//longitude: longitud del local.

//state: String, abreviatura de dos letras del estado donde ubica el local. Ejemplo: TX.

//main_category: String, categoría principal del local.

//num:of_reviews: Int, número total de reseñas de un local.

//rating: Int, calificación otorgada por el usuario de 1 a 5.

//opinion: String, reseña del usuario.

//feeling: String, comentario etiquetado como positivo o negativo.

//platform: String, plataforma origen de los datos.





**Metadata**

//local_name: String, nombre del local.

//gmap_id: String, ubicación geográfica del local.

//latitude: Float, latitud del local.

//longitude: Float, longitud del local.

//category: String, sub-categoría del local.

//avg_rating: Float, promedio de rating de cada local. 

//num_of_reviews: Int, número total de reseñas de un local.

//main_category: String, categoría principal del local.






### **Plataforma Yelp**:




**Review**

//review_id: String, id de cada reseña.

//user_id: String, id del usuario que realizo la reseña.

//business_id: String, id del local

//rating: Int, puntaje dado por el usuario a un local.

//useful: Int, número de votos como reseña útil.

//opinion: String, reseña del usuario.

//date: Timestamp, fecha que se realizó la reseña.

//feeling: String, comentario etiquetado como positivo o negativo.





**Yelp**

//user_id: String, id del usuario que realizo la reseña.

//business_id: String, id del local.

//local_name: String, nombre del local.

//latitude: Float, latitud del local.

//longitude: Float, longitud del local.

//num_of_reviews: Int, número total de reseñas de un local

//state: String, estado donde se encuentra el local.

//main_category: String, categoría principal del local.

//rating: Int, puntaje dado por el usuario a un local.

//opinion: String,  reseña del usuario.

//feeling: String, comentario etiquetado como positivo o negativo.

//platform: String, plataforma origen de los datos.




**Business**

//business_id: String, id del local.

//local_name: String, nombre del local.

//city: String, ciudad donde se ubica el local.

//state: String, estado donde se encuentra el local.

//latitude: Float, latitud del local.

//longitude: Float, longitud del local.

//stars: Float, cantidad de estrellas que recibió el local.

//num_of_reviews: Int, número total de reseñas de un local.

//category: String, sub-categoría del local.

//main_category: String, categoría principal del local.



------------------------------------------------------------------------------------------------------------------------------------------------------------------

# **English**


## **data dictionary **

### **Google Maps Platform**:

**Platform_reviews**

//user_id: String, id of the user doing the review.

//business_id: String, id of the store.

//local_name: String, name of the local.

//latitude: Float, local latitude.

//longitude: Float, longitude of the local.

//num_of_reviews: Int, total number of reviews of a local.

//state: String, state where the venue is located.

//main_category: String, main category of the venue.

//rating: Int, rating given by the user from 1 to 5.

//opinion: String, user review.

//feeling: String, comment labeled as positive or negative.

//platform: String, data source platform.



**Reviews**

//user_Id: String, id of the user who made the review.

//date: Timestamp, date of publication of the review in YYYY/MM/DD format.

//rating: Int, rating given by the user from 1 to 5.

//opinion: String, user's review.

//resp: String, local response.

//gmap_id: String, geographic location of the venue.

//feeling: String, comment labeled as positive or negative.

//state: String, state where the store is located.



**Google**

//user_id: String, id of the user who made the review.

//business_id: String, id of the store. 

//local_name: String, name of the local.

//latitude: local latitude.

//longitude: Longitude of the local.

//state: String, abbreviation of two letters of the state where the local is located. Example: TX.

//main_category: String, main category of the store.

//num:of_reviews: Int, total number of reviews of a venue.

//rating: Int, rating given by the user from 1 to 5.

//opinion: String, user review.

//feeling: String, comment labeled as positive or negative.

//platform: String, data source platform.



**Metadata**

//local_name: String, name of the local.

//gmap_id: String, geographic location of the local.

//latitude: Float, latitude of the local.

//longitude: Float, longitude of the local.

//category: String, sub-category of the room.

//avg_rating: Float, average rating of each venue. 

//num_of_reviews: Int, total number of reviews of a venue.

//main_category: String, main category of the venue.




### **Yelp platform**:


**Review**

//review_id: String, id of each review.

//user_id: String, id of the user who made the review.

//business_id: String, id of the business.

//rating: Int, score given by the user to a store.

//useful: Int, number of votes as useful review.

//opinion: String, user review.

//date: Timestamp, date the review was made.

//feeling: String, comment labeled as positive or negative.



**Yelp**

//user_id: String, id of the user who made the review.

//business_id: String, id of the business.

//local_name: String, name of the local.

//latitude: Float, local latitude.

//longitude: Float, longitude of the local.

//num_of_reviews: Int, total number of reviews of a local.

//state: String, state where the venue is located.

//main_category: String, main category of the venue.

//rating: Int, score given by the user to a venue.

//opinion: String, user review.

//feeling: String, comment labeled as positive or negative.

//platform: String, data source platform.




**Business**

//business_id: String, id of the local.

//local_name: String, name of the local.

//city: String, city where the local is located.

//state: String, state where the local is located.

//latitude: Float, latitude of the local.

//longitude: Float, longitude of the local.

//stars: Float, number of stars the venue received.

//num_of_reviews: Int, total number of reviews of a venue.

//category: String, sub-category of the venue.

//main_category: String, main category of the venue.








