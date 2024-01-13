import mysql.connector
from flask import Flask, jsonify, request
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
    cursor.execute("""CREATE TABLE Universities"""
    """(universityId INT PRIMARY KEY AUTO_INCREMENT,"""
    """name VARCHAR(255),""" 
    """ranking INT)""")
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
    database.close()
    return jsonify(json_data)

# Ruta para insertar datos automáticamente en la tabla Universities
@app.route('/insert')
def auto_insert_university():

    database = mysql.connector.connect(
        host="mysql-flask-app-container",
        user="root",
        password="1234",
        database="DBUniversities"
    )

    cursor = database.cursor()

    #Le pasamos los datos a insertar
    example_data = [
        ('MIT', 1),
        ('Boston College', 46),
    ]

    insert_query = "INSERT INTO Universities (name, ranking) VALUES (%s, %s)"
    cursor.executemany(insert_query, example_data)

    # Confirma la transacción
    database.commit()

    cursor.close()
    database.close()

    return 'Universities have been automatically inserted'



"""

Intentar hacer más adelante inserts con scraping de qsTopUniversities.com

"""     
