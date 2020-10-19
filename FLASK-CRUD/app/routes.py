from flask import render_template, redirect, request, url_for, flash
from app import app
import app.database as database

@app.route('/')
def index():
	data = database.Database.all()
	return render_template('index.html', crud_data = data)


@app.route('/add/', methods = ['GET','POST'])
def add():
	if request.method == 'POST':
		idno = request.form['idno']
		name = request.form['name']
		course = request.form['course']
		yrlvl = request.form['yrlvl']
		email = request.form['email']
		data = database.Database(idno = idno, name = name, course = course, yrlvl = yrlvl, email = email)
		data.add()
		flash("new information added!")
		return redirect(url_for('index'))
	else:
		return render_template('add.html')
	


@app.route('/update/<int:id_data>/')
def update(id_data):
	data = database.Database.get_data(id_data)
	return render_template('update.html', crud_data = data)


@app.route('/update_info/<int:id_data>/', methods=['POST'])
def update_info(id_data):
    if request.method == 'POST':
        idno = request.form['idno']
        name = request.form['name']
        course = request.form['course']
        yrlvl = request.form['yrlvl']
        email = request.form['email']
        data = database.Database(idno = idno, name = name, course = course, yrlvl = yrlvl, email = email, id_data = id_data)
        data.update_info(id_data)
        flash('Record Updated Successfully')
        return redirect(url_for('index'))


@app.route('/delete_info/<int:id_data>/')
def delete_info(id_data):
	data = database.Database(id_data = id_data)
	data.delete_info(id_data)
	flash("Record has been deleted successfully")
	return redirect(url_for('index'))


