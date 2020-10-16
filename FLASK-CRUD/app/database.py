from app import app, mysql

class Database(object):

	def __init__(self, id_data = None, idno = None, name = None, course = None, phone = None, email = None):
		self.id_data = id_data
		self.idno = idno
		self.name = name
		self.course = course
		self.phone = phone
		self.email = email

	@classmethod
	def all(cls):
		cur = mysql.connection.cursor()
		cur.execute('SELECT * FROM crud_data')
		data = cur.fetchall()
		cur.close()
		return data

	def add(self):
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO crud_data(idno, name, course, phone, email) VALUES(%s, %s, %s, %s, %s)",(self.idno, self.name, self.course, self.phone, self.email))
		mysql.connection.commit()


	@classmethod
	def get_data(cls,self):
		cur = mysql.connection.cursor()
		cur.execute('SELECT * FROM crud_data WHERE id_data = %s', [self])
		data = cur.fetchall()
		cur.close()
		return data


	def update_info(self, id_data = None):
		cur = mysql.connection.cursor()
		cur.execute("UPDATE crud_data SET idno = %s, name = %s, course = %s, phone = %s, email = %s WHERE id_data = %s",(self.idno, self.name, self.course, self.phone, self.email, self.id_data))
		mysql.connection.commit()


	def delete_info(self, id_data = None):
		cur = mysql.connection.cursor()
		cur.execute("DELETE FROM crud_data WHERE id_data = %s",[self.id_data])
		mysql.connection.commit()