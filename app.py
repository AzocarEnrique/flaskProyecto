from flask import Flask, render_template, redirect
from flask_migrate import Migrate
from models.UserAD import db
from routes.user_bp import user_bp
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')

Bootstrap(app)

db.init_app(app)
migrate = Migrate(app, db)
with app.app_context():
    db.create_all()

app.register_blueprint(user_bp, url_prefix='/users')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/users/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/users/ingresar', methods=['GET'])
def ingresar():
    return render_template('ingresar.html')

@app.route('/users/ingresar2', methods=['GET'])
def ingresar2():
    return render_template('ingresar2.html')

@app.route('/users/opcion', methods=['GET'])
def opcion():
    return render_template('opcion.html')

@app.route('/users/actualizar', methods=['GET','POST'])
def update():
    return render_template('actualizar.html')

@app.route('/users/listar', methods=['GET'])
def listar():
    return redirect('listar')

@app.route('/users/gestion', methods=['GET','POST'])
def gestion():
    return redirect('gestion')

@app.route('/users/salas', methods=['GET', 'POST'])
def salas():
    return redirect('salas')

@app.route('/users/mostrarsalas', methods=['GET', 'POST'])
def mostrarsalas():
    return redirect('mostrarsalas')

@app.route('/users/subirhorario', methods=['GET', 'POST'])
def subirhorario():
    return redirect('subirhorario')
    
@app.route('/users/horario', methods=['GET', 'POST'])
def horario():
    return redirect('horario')

@app.route('/users/autorizo', methods=['GET', 'POST'])
def autorizo():
    return redirect('autorizo')


if __name__ == '__main__':
    app.debug = True
    app.run()
