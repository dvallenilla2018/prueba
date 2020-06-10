from flask import Flask , render_template	,request,url_for,redirect,flash
from flask_mysqldb import MySQL  
app=Flask(__name__)
"""
app.config['MYSQL_HOST'] = 'locaus-cdbr-east-05.cleardb.net'
app.config['MYSQL_USER'] = 'bd5d239587a483'
app.config['MYSQL_PASSWORD'] = '8379a9b5'
app.config['MYSQL_DB'] = 'heroku_ccf4416d7712962'
mysql=MySQL(app)
"""


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskcontacts'
"""
app.config['MYSQL_HOST'] = 'sq65ur5a5bj7flas.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'fted2jlw2tvej1v1'
app.config['MYSQL_PASSWORD'] = 'qf9s1wpu7sf2c7l1'
app.config['MYSQL_DB'] = 'aw34tmngqqrydm8z'
"""

app.secret_key='mysecretkey'
mysql=MySQL(app)
@app.route('/')
def home():
	cur=mysql.connection.cursor()
	cur.execute('SELECT * FROM contacts')
	data=cur.fetchall()
	print(data)
	mysql.connection.commit()
	return render_template('home.html',contactos=data)





@app.route('/add_contact',methods=['POST'])
def add_contact():
	if request.method=='POST':
		fullname=request.form['fullname']
		phone=request.form['phone']
		email=request.form['email']
		
		cur=mysql.connection.cursor()
		cur.execute('INSERT INTO contacts(fullname,phone,email) VALUES(%s,%s,%s)', (fullname,phone,email))
		mysql.connection.commit()
		flash('Registro agregado Satisfactoriamente')
		return redirect(url_for('home'))

@app.route('/edit/<string:id>')
def get_contact(id):
	cur=mysql.connection.cursor()

	cur.execute('SELECT * FROM contacts WHERE ID={0}'.format(id))
	data=cur.fetchall()
	return render_template('edit-contact.html',contactos=data[0])
	
@app.route('/update/<id>',methods=['POST'])
def get_update_contact(id):	

   if request.method=='POST':
	   fullname=request.form['fullname']
	   phone=request.form['phone']
	   email=request.form['email']
	   cur=mysql.connection.cursor()
	   cur.execute("""
	   UPDATE  contacts 
	   SET FULLNAME = %s,
	   email  = %s,
	   phone  = %s
	   WHERE ID= %s""",(fullname,email,phone,id))
	   mysql.connection.commit()
	   flash('Registro actualizado Satisfactoriamente')

   return redirect(url_for('home'))	

@app.route('/delete/<string:id>')
def delete_contact(id):
	cur=mysql.connection.cursor()
	cur.execute('DELETE FROM contacts WHERE ID={0}'.format(id))
	mysql.connection.commit()
	flash('Registro Eliminado Satisfactoriamente')
	return redirect(url_for('home'))
	



if __name__=='__main__':
		app.run(port=3000, debug=True)