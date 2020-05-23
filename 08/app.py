from flask import Flask, render_template, url_for, request
from markupsafe import escape
# pip install mysql-connector-python
import mysql.connector
app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root1234",
  database="learn_mysql"
)

mycursor = mydb.cursor(dictionary=True)



@app.route('/')
def index():    
    mycursor.execute("SELECT * FROM Employees")
    employees = mycursor.fetchall()

    return render_template('home.html', employees= employees)

