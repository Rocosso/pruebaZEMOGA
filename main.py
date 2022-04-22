from flask import *


app = Flask(__name__, template_folder='templates')


@app.route('/') #crear la pagina de bienvenida
def home():
    nombre = jsonify({'name':'Jacob!'})
    templateData = {
        'titulo': "Prueba Zemoga",
        'imagenPerfil': "si,aunque no parezca esto es una imagen",
        'nombre': nombre,
        'experiencia': "pos mi experiencia no es mucha la verdad ",
        'Tweet1': "Tweet 1",
        'Tweet2': "Tweet 2",
        'Tweet3': "Tweet 3",
        'Tweet4': "Tweet 4",
        'Tweet5': "Tweet 5"
    }
    return render_template('home.html', **templateData)


@app.route('/modificar') #crear la segunda pagina para introducir la informacion a buscar
def modificar():
    #<!-- ir a la API de twitter con los datos de GCG y extraer esa info -->
    return render_template('modificar.html')


@app.route('/', methods=["GET", "POST"]) #capturar la informacion de busqueda
def gfg():
    if request.method == "POST":
        # obtener el texto de "nombre" nuevo = "nombre" en el formulario HTML
        nombre = request.form.get("nombre")
        # obtener el texto de "experiencia" nuevo = "experiencia" en el formulario HTML
        experiencia = request.form.get("experiencia")
        # obtener el texto de "twitter" nuevo = "twitter" en el formulario HTML
        twitter = request.form.get("twitter")

        # <!-- falta buscar los tweets -->
        return jsonify({"profile": {"name" : nombre, "experience" : experiencia, "twitter" : twitter }})

    return render_template("modificar.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
