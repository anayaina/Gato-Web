from flask import Flask, render_template, request, session
import gato, secrets
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.run(debug=True)

diccionario_blanco = { 'A':"/static/images/blanco.png",
                        'B':"/static/images/blanco.png",
                        'C':"/static/images/blanco.png",
                        'D':"/static/images/blanco.png",
                        'E':"/static/images/blanco.png",
                        'F':"/static/images/blanco.png",
                        'G':"/static/images/blanco.png",
                        'H':"/static/images/blanco.png",
                        'I':"/static/images/blanco.png"
                    }

tablero_gato = gato.Tablero()

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        valor = request.form['pos']
        if(valor=="nuevo"):
            tablero_gato.limpia_tablero()
            return render_template("index.html", celda=diccionario_blanco)
        
        if (valor in tablero_gato.lista_celdas):
            diccionario,ganador = tablero_gato.jugar(valor)
            #diccionario,ganador = tablero_gato.jugar_computadora()
            if ganador == None:
                diccionario, ganador = tablero_gato.jugar_computadora()
            print(ganador)
            return render_template("index.html",celda=diccionario, winner=ganador)
        else:
            print(request.form['pos'])
            return render_template("index.html", celda=diccionario_blanco)
    else:
        return render_template("index.html", celda=diccionario_blanco)