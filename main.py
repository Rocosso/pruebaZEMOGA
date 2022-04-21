from flask import *

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
   templateData = {
      'titulo': "Prueba Zemoga",
      'imagenPerfil': "si,aunque no parezca esto es una imagen",
      'nombre': "jorgelito paredon",
      'experiencia': "pos mi experiencia no es mucha la verdad ",
      'Tweet1': "Tweet 1",
      'Tweet2': "Tweet 2",
      'Tweet3': "Tweet 3",
      'Tweet4': "Tweet 4",
      'Tweet5': "Tweet 5"
   }
   return render_template('home.html', **templateData)

@app.route('/modificar')
def modificar():
   return render_template('modificar.html')

@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # obtener el texto de "nombre" nuevo = "nombre" en el formulario HTML
       nombre = request.form.get("nombre")
       # obtener el texto de "experiencia" nuevo = "experiencia" en el formulario HTML
       experiencia = request.form.get("experiencia")
       # obtener el texto de "twitter" nuevo = "twitter" en el formulario HTML
       twitter = request.form.get("twitter")
       #<!-- falta buscar los tweets -->
       return "tu nueva identidad es: "+ nombre + " " + experiencia + " " + twitter
    return render_template("modificar.html")


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080, debug=True)