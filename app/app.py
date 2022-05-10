from flask import *
from ProfileTwitter import getTweets
from db import db
app = Flask(__name__, template_folder='templates')


@app.route('/') #crear la pagina de bienvenida
def home():
    tweets = getTweets("twitterapi")
    return print_home(tweets)

@app.route('/modificar') #crear la segunda pagina para introducir la informacion a buscar
def modificar():
    read_db = db.get_all()
    for x in read_db:
        print(x)
    return render_template('modificar.html')


@app.route('/', methods=["GET", "POST"]) #capturar la informacion de busqueda
def gfg():
    if request.method == "POST":

        nombre = request.form.get("nombre")           # obtener el texto de "nombre" nuevo = "nombre" en el formulario HTML
        experiencia = request.form.get("experiencia") # obtener el texto de "experiencia" nuevo = "experiencia" en el formulario HTML
        twitter = request.form.get("twitter")         # obtener el texto de "twitter" nuevo = "twitter" en el formulario HTML
        tweets = getTweets(twitter)
        new_profile = print_home(tweets)
        return new_profile

    return render_template("modificar.html")

def print_home(tweets):
    templateData = {
        'titulo': "Prueba Zemoga",
        'nombre': tweets['name'],
        'experiencia': tweets['experience'],
        'imagenPerfil': tweets['image'],
        'Tweet1': tweets['T1'],
        'Tweet2': tweets['T2'],
        'Tweet3': tweets['T3'],
        'Tweet4': tweets['T4'],
        'Tweet5': tweets['T5']
    }
    db.create([tweets['id'], tweets['experience'], tweets['image'],  "luischavezcastro84@gmail.com",
               "About me:  I'm mechatronic Engineer, I've develop mainly in Hardware, building machines and control process automation, I like python and i want to be a data engineer in 5 years",
                "Chavez Castro","Luis Alberto"])
    return render_template('home.html', **templateData)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

