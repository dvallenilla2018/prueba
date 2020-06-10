from flask import Flask , render_template	,request,url_for,redirect,flash
from flask_mysqldb import MySQL  
app=Flask(__name__)

app.config['MYSQL_HOST'] = 'sq65ur5a5bj7flas.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'fted2jlw2tvej1v1'
app.config['MYSQL_PASSWORD'] = 'qf9s1wpu7sf2c7l1'
app.config['MYSQL_DB'] = 'aw34tmngqqrydm8z'
app.secret_key='mysecretkey'
mysql=MySQL(app)


@app.route('/')

def home():
    cur=mysql.connection.cursor()
    cur.execute('''
    CREATE TABLE  USUARIOS(
        ID 			INTEGER 		PRIMARY KEY 	,
        NOMBRE_USUARIO 		VARCHAR(50)								,
        APELLIDO 	VARCHAR(50)								,
        PASSWORD 	VARCHAR(250) 								,
        DIRECCION 	VARCHAR(50) 								,
        COMENTARIO 	VARCHAR(100) 								
        )
        ''')
    mysql.connection.commit()
    flash('Registro actualizado Satisfactoriamente')




if __name__=='__main__':
		app.run(port=3306, debug=True)