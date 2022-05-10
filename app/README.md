# pruebaZemoga
## instrucciones para el funcionamiento de la prueba laboral

###### software:
python 3.9
flask 2.1.1
virtualenv 2.0+
html4.0
mysql.connector 8.0.28
Tweepy 4.8.0

###### pasos previos:
    pip install virtualenv           instala entorno virtual
    python3 -m venv env              configura el entorno virtual
    pip install flask                instala la libreria de microframeworks recomendada
    pip install psycopg2-binary      instala la libreria PostgreSQL que adapta SQL a Python
    python3 -m pip install mysql-connector-python      instala la libreria para manejar SQL usando MySQL
    pip install tweepy               instala la libreria para conectarse con la API de twitter


###### pasos para construir la app:
1.   ejecutar en una terminal de Python3: **python3 main.py**

2.   abrir el navegador web e ir a la URL: **localhost:8080**

3. leer el contenido de la pagina, 

4. buscar el link de editar el profile

5. ingresar al link 

6. en este momento se lee toda la tabla "portfolio" de la base de datos "zemoga_test_db" y se imprime por consola

7. proporcionar los valores solicitados incluyendo un valor valido de usuario de twitter.

8. posteriormente dar click en el boton de actualizar y observar el cambio en la pagina de inicio.

de la misma forma se puede verificar que cada vez que se ingresa un valor para actualizarlo este se guarda en la base de datos con los items basicos, pero es posible diligenciar todos los campos de la tabla de la base de datos.

###### tecnologias empleadas:
    python, flask, html4, mysql.connector, Tweepy

###### tiempo total: 

**Tiempo para realizar el codigo:** 18 horas para realizar el código funcional, llevando el control de versiones de git con cada avance.

**tiempo para la documentacion:**

###### mejoras a realizar en el codigo:

quedan muchas cosas por mejorar, me gustaria dilienciar mas datos de la tabla de la base de datos, tambien me gustaria extraer la imagen del perfil de twitter que se halla guardada en la base de datos y mostrarla en vez de la foto de la moto con cada actualizacion del perfil.

tambien graficaria el contenido de los ultimos usuarios registrados en la base de datos, para asi imprimirla unos instantes antes de visualizar la segunda pagina.


tambien se podria hacer una valoracion de los textos de estos usuarios para analisar que tan positivos, negativos o neutrales son sus comentarios y darles una calificacion a modo de ver que cuentas son mas influenciables que otras respecto a un tema en especifico.


