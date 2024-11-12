from flask import Flask, request, render_template, url_for
from werkzeug.utils import redirect


app = Flask(__name__)

@app.route('/')
def inicio():
    app.logger.info(f'Entramos al path {request.path}')
    return 'Hola mundo desde Flask'

@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Hola {nombre.upper()}'

@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tu edad es: {edad + 5}'

@app.route('/datos/<valor>', methods=['GET', 'POST'])
def mostrar(valor):
    #return f'El dato es: {valor}'
    return render_template('mostrar.html', valor=valor)

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('mostrar', valor='Pablo'))