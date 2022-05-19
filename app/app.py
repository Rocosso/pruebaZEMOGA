#! /usr/bin/python3
from flask import *
from src.ProfileTwitter import getTweets
from src.db import db
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.exceptions import HTTPException
from settings import *

app = Flask(__name__, template_folder='swagger/templates')
SWAGGER_URL = '/api/docs'  # URL para exponer Swagger UI (sin finalizar en '/')
API_URL = '/swagger/static/swagger.json'  # nuestra API url (puede ser un recurso local)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(403)
def forbiden(e):
    return render_template('304.html')


class CustomErr(HTTPException): # Define error
    code = 304
    description = "<h1>Custom error</h1>"

@app.route("/304")
def user_not_found():
    return render_template('304.html')

@app.route('/swagger/static/<path:path>')
def send_static(path):
    return send_from_directory('swagger/static', path)

@app.route('/')  # crear la pagina de bienvenida
def home():
    tweets = getTweets("twitterapi")
    return print_home(tweets)

@app.route('/modificar')  # crear la segunda pagina para introducir la informacion a buscar
def modificar():
    read_db = db.get_all()
    for x in read_db:
        print(x)
    return render_template('modificar.html')

@app.route('/', methods=["GET", "POST"])  # capturar la informacion de busqueda
def gfg():
    if request.method == "POST":
        nombre = request.form.get("nombre")  # obtener el texto de "nombre" nuevo = "nombre" en el formulario HTML
        experiencia = request.form.get(
            "experiencia")                     # obtener el texto de "experiencia" nuevo = "experiencia" en el formulario HTML
        twitter = request.form.get("twitter")  # obtener el texto de "twitter" nuevo = "twitter" en el formulario HTML
        if getTweets(twitter):
            tweets = getTweets(twitter)
        else:
            abort(404)
        new_profile = print_home(tweets)
        return new_profile
    return render_template("modificar.html")


def print_home(tweets):
    templateData = {
        'titulo': "Prueba Zemoga",
        'nombre': tweets['name'],
        'imagenPerfil': tweets['image'],
        'experiencia': tweets['experience'],
        'Tweet1': tweets['T1'],
        'Tweet2': tweets['T2'],
        'Tweet3': tweets['T3'],
        'Tweet4': tweets['T4'],
        'Tweet5': tweets['T5']
    }
    db.create([tweets['experience'],
               tweets['image'],
               tweets['name'],
               "luischavezcastro84@gmail.com",
               "About me:  I'm mechatronic Engineer, I've develop mainly in Hardware, "
               "building machines and control process automation, I like python and"
               " i want to be a data engineer in 5 years",
               "Chavez Castro",
               "Luis Alberto"]
              )
    return render_template('home.html', **templateData)

# Inicia documentacion Swagger
# llamado a la funcion para crear nuestro blueprint

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI dirección estática, puede ser [API URL]/dist
    API_URL,      # direccion para ubicar la documentación
    config={  # Swagger UI config overrides
        'app_name': "Zemoga Test application"
    }
)

app.register_blueprint(swaggerui_blueprint,url_prefix=SWAGGER_URL)
# creación del blueprint


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
