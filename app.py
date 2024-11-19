from flask import Flask, request, render_template, url_for, abort, session
from werkzeug.utils import redirect


app = Flask(__name__)
app.secret_key = '50ee6def18a0af7cb5271194656519317732b6867da284e942c0dbfdabe276e4'

@app.route('/')
def inicio():
    if 'username' in session:
        return f'El usuario inicio sesión {session["username"]}'
    return 'No inicio sesión'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('inicio'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('inicio'))

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

@app.route('/error')
def error():
    return abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404