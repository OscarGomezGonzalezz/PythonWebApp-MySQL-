import mysql.connector
from flask import Flask
import json

app = Flask(__name__)

#Definimos la ruta inicial
@app.route('/')
def hello_world():
    return 'Hello World ;)'

#Esta ruta crea la database 
@app.route('/initdb')
def initdb():
    database = mysql.connector.connect(
        host="mysql-flask-app-container",
        user="root",
        password="1234"        
    )
    cursor = database.cursor()
    cursor.execute("DROP DATABASE IF EXISTS DBUniversities")
    cursor.execute("CREATE DATABASE DBUniversities")
    cursor.close()    
    return 'Database has been initialited'     
#Crea la tabla
@app.route('/init_tables')
def init_tables():
    database = mysql.connector.connect(
        host="mysql-flask-app-container",
        user="root",
        password="1234",
        database="DBUniversities"
    )
    cursor = database.cursor()

    cursor.execute("DROP TABLE IF EXISTS Universities")
    cursor.execute("""CREATE TABLE Universities """
    """(UniversityId INT PRIMARY KEY AUTO_INCREMENT,"""
    """name VARCHAR(255),""" 
    """Ranking VARCHAR(255),"""
    """Country VARCHAR(255))""")
    cursor.close()    
    return "Tables have been initialized"

#Nos devuelve la tabla Universities creada anteriormente
@app.route('/universities')
def get_products():
    database = mysql.connector.connect(
        host="mysql-flask-app-container",
        user="root",
        password="1234",
        database="DBUniversities"
    )
    cursor = database.cursor()
    cursor.execute("SELECT * FROM Universities")
    
    #Creamos una representacion JSON de la informacion de "Universidades" para que lo devuelva como respuesta http
    nombre_columnas =[x[0] for x in cursor.description]
    universities = cursor.fetchall()
    json_data=[]
    for u in universities:
        json_data.append(dict(zip(nombre_columnas,u)))
    cursor.close()
    return json.dumps(json_data)

"""
INSERT INTO Universities()
Intentar hacerlo con scraping de qsTopUniversities.com

"""    