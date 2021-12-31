import os
import sys
from flask import render_template, redirect, url_for, request, abort, g
from flask.helpers import flash
from models.UserAD import Admin, Profesor, Salas, Horario
from flask_sqlalchemy import SQLAlchemy
from templates.UpdateTemplate import NameForm
from templates.UpdateTemplate1 import NameForm1
from templates.LoginTemplate import NameFormLogin
from templates.templateGestion import NameFormGestion
from templates.template1 import NameFormop
from templates.templateSalas import NameFormSalas
from templates.mostrarTemplate import NameFormMostrar
from templates.subirhorarioTemplate import NameFormsubirhorario
from templates.horarioTemplate import NameFormhorario
from templates.autorizoTemplate import NameFormautorizo
from flask import app, request
import psycopg2
from werkzeug.utils import secure_filename

db = SQLAlchemy()

def index():
    print('hola')

def store():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        user=Admin(
        rut=form.rut.data,
        nombre=form.nombre.data,
        email=form.email.data,
        contrasena=form.contrasena.data,
        departamento=form.departamento.data,
        oficina=form.oficina.data,
        cargo=form.cargo.data)
        db.session.add(user)
        db.session.commit()
        form.rut.data = ''
        form.nombre.data = ''
        form.email.data = ''
        form.contrasena.data = ''
        form.departamento.data = ''
        form.oficina.data = ''
        form.cargo.data = ''
    return render_template('ingresar.html', form=form, name=name)

def store2():
    name = None
    form = NameFormop()
    value = ''
    value = dict(form.operador.choices).get(form.operador.data)
    if form.validate_on_submit():
        if(value == "Administrador"):
            return redirect('ingresar')
        else:
            return redirect('ingresar2')
    return render_template('opcion.html', form=form, name=name)

def store3():
    name = None
    form = NameForm1()
    if form.validate_on_submit():
        user=Profesor(
        rut=form.rut.data,
        nombre=form.nombre.data,
        email=form.email.data,
        contrasena=form.contrasena.data,
        departamento=form.departamento.data)
        db.session.add(user)
        db.session.commit()
        form.rut.data = ''
        form.nombre.data = ''
        form.email.data = ''
        form.contrasena.data = ''
        form.departamento.data = ''
    return render_template('ingresar2.html', form=form, name=name)    

def login():
    name = None
    form = NameFormLogin()
    value = dict(form.operador.choices).get(form.operador.data)
    if form.validate_on_submit():
        if(value == "Administrador"):
            find = Admin.query.filter_by(rut=form.rut.data, contrasena =form.contrasena.data).first()
            if(find is None):
                return render_template('login.html', form=form, name=name)
            else: 
                flash("se inicio sesion exitosamente")
                return redirect(url_for('index'))
        else:
            find = Profesor.query.filter_by(rut=form.rut.data, contrasena =form.contrasena.data).first()
            if(find is None):
                return render_template('login.html', form=form, name=name)
            else:
                flash("se inicio sesion exitosamente")
                return redirect(url_for('index'))
    return render_template('login.html', form=form, name=name)

    
def gestion():
    name = None
    form = NameFormGestion()
    value = ''
    value = dict(form.operador.choices).get(form.operador.data)
    if form.validate_on_submit():
        if(value == "Agregar Salas"):
            return redirect('salas')
        elif(value == "Subir Horario"):
            return redirect('subirhorario')
        elif(value == "Administrar cuentas"):
            return redirect('autorizo')
    return render_template('gestion.html', form=form, name=name)


def update():
    name = None
    form = NameForm()
    if request.method == 'POST':
        print('post')
    else:
        print('get')
    return render_template('actualizar.html',form=form, name=name)

def delete(userId):
    pass

def salas():
    name = None
    form = NameFormSalas()
    if form.validate_on_submit():
        user=Salas(
        id=form.id.data,
        piso=form.piso.data,
        capacidad=form.capacidad.data,
        departamento=form.departamento.data)
        db.session.add(user)
        db.session.commit()
        form.id.data = ''
        form.piso.data = ''
        form.capacidad.data = ''
        form.departamento.data = ''   
    return render_template('salas.html', form=form, name=name)    

def mostrar():
    name = None
    form = NameFormMostrar()
    try: 
        con = psycopg2.connect(database="flask", user="postgres",  
        password="postgres123", host="localhost")
        print("connected")
    except:
        print ("I am unable to connect to the database")
    cur =con.cursor()
    find = Salas.query.filter_by(id = form.id.data).first()
    if(find is None):
        print("xd")
    else:
        cur.execute("SELECT * FROM salas WHERE id=%s",(form.id.data,))
        data = cur.fetchall()
        print(find)
        return render_template('mostrarsalas.html',form=form, data = data)
    return render_template('mostrarsalas.html', form=form, name=name)

def horario():
    name = None
    form = NameFormsubirhorario()
    if form.validate_on_submit():
        user=Horario(
        carrera=form.carrera.data,
        semestre=form.semestre.data)
        imagen = form.imagen.data
        nombre_imagen = secure_filename(form.carrera.data + '_' + form.semestre.data)
        ruta_imagen = os.path.abspath('static\{}'.format(nombre_imagen))
        ruta_html = '{}'.format(nombre_imagen)+'.jpg'
        imagen.save(ruta_imagen+'.jpg')
        if imagen.filename != '':
            user.imagen = ruta_html
        else:
            pass
        db.session.add(user)
        db.session.commit()
        form.carrera.data = ''
        form.semestre.data = ''
        form.imagen.data = '' 
        return render_template('subirhorario.html', form=form, name=name) 
    return render_template('subirhorario.html', form=form, name=name)    

def mostrarhorario():
    name = None
    form = NameFormhorario()
    if form.validate_on_submit():
        try: 
            con = psycopg2.connect(database="flask", user="postgres",  
            password="postgres123", host="localhost")
            print("connected")
        except:
            print ("I am unable to connect to the database")
        cur =con.cursor()
        find = Horario.query.filter_by(carrera = form.carrera.data, semestre = form.semestre.data).first()
        if(find is None):
            print("xd")
        else:
            cur.execute("SELECT * FROM horario WHERE carrera=%s AND semestre = %s",(form.carrera.data,form.semestre.data,))
            data = cur.fetchall()
            print(find)
            return render_template('horario.html',form=form, data = data)
    return render_template('horario.html',form=form, name=name)

def autorizo():
    name = None
    form = NameFormautorizo()
    try: 
        con = psycopg2.connect(database="flask", user="postgres",  
        password="postgres123", host="localhost")
        print("connected")
    except:
        print ("I am unable to connect to the database")
    cur =con.cursor()
    if form.validate_on_submit():
        
        find = Profesor.query.filter_by(rut = form.rut.data).first()
        if(find is None):
            print("xd")
        else:
            '''find = Profesor.query.filter(Profesor.rut == form.rut.data).one()
            db.session.delete(find)
            db.session.commit()'''
            deleted_objects = Profesor.__table__.delete().where(Profesor.rut.in_([form.rut.data]))
            db.session.execute(deleted_objects)
            db.session.commit()
            cur.execute("SELECT * FROM profesores")
            data = cur.fetchall()
            print(find)
            return render_template('autorizo.html',form=form, data = data)
    cur.execute("SELECT * FROM profesores")
    data = cur.fetchall()
    return render_template('autorizo.html',form=form, data = data)