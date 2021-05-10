from flask import Flask, render_template, redirect, request
import json
import os
from cs50 import SQL

db = SQL("sqlite:///moovie.db")

#Archivos que no me interesa ver en el menu
nomostrar = [ "index.html","layout.html","resultados.html","actualizador.html"]

app = Flask(__name__)

@app.route("/")
def index():
    x = os.listdir('templates')
    
    #elimina las view que no quiero mostrar
    for i in nomostrar:
        x.remove(i)

    #define las rutas (solo elimina el ".html" )
    functions = []
    
    for i in x:
        functions.append(i.split('.')[0])

    return render_template("index.html",funciones = functions)

#esto funciona como menu de las view similar al switch de C
@app.route("/views/<string:option>")
def hacer(option):
    return redirect('/'+option)

@app.route("/agregar",methods=["GET","POST"])
def insert():
    return "TODO"
   

@app.route("/buscar",methods=["GET","POST"])
def select():
    return "TODO"
    
    
@app.route("/mostrar")
def selectall():
    response = db.execute("SELECT * FROM movies")

    return render_template("mostrar.html",response = response)
  

@app.route("/actualizar",methods=["GET","POST"])
def update():
    return "TODO"

@app.route("/actualizador",methods=["GET","POST"])
def actualizador():
    return "TODO"


@app.route("/eliminar",methods=["GET","POST"])
def delete():
    return "TODO"