# prueba Para Zemoga
### por Luis Alberto Chavez Castro
## Instrucciones para el funcionamiento de la prueba laboral

###### software:
        python 3.9
        flask 2.1.1
        html4.0
        mysql.connector 8.0.28
        Tweepy 4.8.0

###### pasos previos:
1. Instalar Docker

2. En una consola/terminal dentro de la carpeta app ejecutar el comando:

        docker build . -t api_rest_luis_chavez

3. Una vez terminado el proceso ejecute el comando:   
   
        docker ps -a
4. Determine el ID de contenedor de la lista proporcionada, aqui se deja un ejemplo del resultado esperado:
       
        CONTAINER ID   IMAGE          COMMAND            CREATED          STATUS                      PORTS     NAMES
        9814a7855e89   e8e1aaace99e   "python3 app.py"   4 minutes ago    Exited (0) 12 seconds ago             focused_boyd
5. Ejecute el comando de inicializacion del contenedor basado en la imagen que se creo en el paso 2 empleando el valor del  CONTAINER ID recien hallado en el paso 4 empleando el comando:
        
        docker run  9814a7855e89
6. Debera obtener una respuesta similar a:


        conexión exitosa
        información del servidor: 5.6.51-log
        * Serving Flask app 'app' (lazy loading)
        * Environment: production
          WARNING: This is a development server. Do not use it in a production deployment.
         Use a production WSGI server instead.
        * Debug mode: on
         * Running on all addresses (0.0.0.0)
           WARNING: This is a development server. Do not use it in a production deployment.
         * Running on http://127.0.0.1:8080
         * Running on http://172.17.0.3:8080 (Press CTRL+C to quit)
         * Restarting with stat
         * Debugger is active!
         * Debugger PIN: 128-724-481

En este caso la API REST estara exitosamente en linea en un servidor local y podra interactuar con ella a través del navegador web 


###### Pasos para interactuar con la app:
1. Abrir el navegador web

2. Ir a la URL: 

        http://localhost:8080

3. Leer el contenido de la pagina, 

4. Buscar el link de **reemplazar el profile**

5. Ingresar al link 

6. En este momento se lee toda la tabla "portfolio" de la base de datos "zemoga_test_db" y se imprime por consola

7. En la parte de abajo de la pagina diligencie los valores solicitados incluyendo un valor valido de usuario de twitter.

8. Posteriormente dar click en el boton de actualizar y observar el cambio en la pagina de inicio.

9. Puede consultar la documentacion en:
http://localhost:8080/api/docs/


De la misma forma se puede verificar que cada vez que se ingresa un valor para actualizarlo este se guarda en la base de datos con los items basicos, pero es posible diligenciar todos los campos de la tabla de la base de datos.

###### Tecnologias empleadas:
      Flask 	2.1.2	
      Jinja2	3.1.2	
      MarkupSafe	2.1.1	
      PyYAML	6.0	
      Routes	2.5.1	
      Werkzeug	2.1.2	
      apispec	5.2.1	
      apispec-webframeworks	0.5.2	
      attrs	21.4.0	
      certifi	2021.10.8	
      charset-normalizer	2.0.12	
      click	8.1.3	
      clickclick	20.10.2	
      connexion	2.13.1	
      flask-swagger	0.2.14	
      flask-swagger-ui	3.36.0	
      idna	3.3	
      importlib-metadata	4.11.3	
      importlib-resources	5.7.1	
      inflection	0.5.1	
      itsdangerous	2.1.2	
      jsonschema	4.5.1	
      marshmallow	3.15.0	
      mysql-connector	2.2.9	
      oauthlib	3.2.0	
      packaging	21.3	
      pip	20.0.2	
      pkg-resources	0.0.0	
      pyparsing	3.0.9	
      pyrsistent	0.18.1	
      repoze.lru	0.7	
      requests	2.27.1	
      requests-oauthlib	1.3.1	
      setuptools	44.0.0	
      six	1.16.0	
      tweepy	4.9.0	
      urllib3	1.26.9	
      wheel	0.34.2	
      zipp	3.8.0	

###### Documentación:
La documentación se encuentra en los siguientes medios:

    Swagger UI
    http://localhost:8080/api/docs/

    Archivo readme
        .app/Readme.MD

    Github:
    https://github.com/Rocosso/pruebaZEMOGA.git

Se especifican las versiones minimas de trabajo, en caso de que una actualizacion del sistema pueda cambiar al punto de dar de baja la app, se podra hacer funcionar con estas versiones de modo estable mientras se realiza el replatform.

###### Tiempo total: 

**Tiempo para realizar el codigo:** 18 horas para realizar el código funcional, llevando el control de versiones de git con cada avance, la estructuracion del proyecto ha sido realizada en paralelo con la implementacion de cada funcion, metodo y clase.

**Tiempo para la documentacion:** El desarrollo de Docker requirio mas tiempo al ser una tecnologia totalmente nueva y tener que aprenderla por completo de forma autodidacta, aun así, se logro implementar en 3 dias, iniciando con la seleccion de la imagen con un sistema operativo ligero (alpine) con el software requerido preinstalado (python) y requiriendo adaptaciones (creacion y selección de usuarios, puerto y ejecución) e instalaciones minimas (PIP install requirements.txt) para el funcionamiento de la app.

La documentación en Swagger ha requerido de 3 dias mas, debido a que he tenido que estudiarlo y aprenderlo sin ningun conocimiento previo y la gran cantidad de información no relevante sobre el mismo es abrumadora. 

###### Mejoras a realizar en el codigo:

Quedan muchas cosas por mejorar, me gustaria dilienciar mas datos de la tabla de la base de datos, tambien me gustaria extraer la imagen del perfil de twitter que se halla guardada en la base de datos y mostrarla en vez de la foto de la moto con cada actualizacion del perfil.

Tambien graficaria el contenido de los ultimos usuarios registrados en la base de datos, para asi imprimirla unos instantes antes de visualizar la segunda pagina.


Se podria hacer una valoracion de los textos de estos usuarios para analisar que tan positivos, negativos o neutrales son sus comentarios y darles una calificacion a modo de ver que cuentas son mas influenciables que otras respecto a un tema en especifico.


