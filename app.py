from flask import Flask
import os 
import time
import psycopg2

app=Flask(__name__)

def get_db_connection():
	conn=psycopg2.connect(
		host="db",
		database="mydb",
		user="postgres",
		password="secret"
	)
	return conn

@app.route('/')
def home():
	return 'Hello  Jaick Flash Running'

@app.route('/dbcheck')
def dbcheck():
	try:
		conn = get_db_connection()
		conn.close()
		return 'Database connection successful'
	except Exception as e:
		return f'Database connection failed: {str(e)}'
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)


			 
