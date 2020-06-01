from flask import Flask, render_template, url_for, request, flash, redirect
from markupsafe import escape
# pip install mysql-connector-python
import mysql.connector
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="learn_mysql"
)

mycursor = mydb.cursor(dictionary=True)



@app.route('/')
def index(): 
    mycursor.execute("SELECT * FROM Employees")
    employees = mycursor.fetchall()   
    return render_template('home.html', employees=employees)

@app.route('/employee/', methods=['GET'])
def show_employee_create_form():
    return render_template('create-employee.html')

@app.route('/employee/create', methods=['POST'])
def create_employee():
    FirstName = escape(request.form['FirstName'])
    LastName = escape(request.form['LastName'])
    Age = escape(request.form['Age'])
    Salary = escape(request.form['Salary'])
    Designation = escape(request.form['Designation'])
    sql = """INSERT INTO Employees(FirstName, LastName, Age, Salary, Designation)
    VALUES(%s, %s, %s, %s, %s)"""
    val = (FirstName, LastName, Age, Salary, Designation)
    mycursor.execute(sql, val)
    mydb.commit()
    if mycursor.rowcount > 0:
       message = "Insert success"
    else:
        message = None
    flash(message)
    return redirect(url_for('index'))

@app.route('/employee/edit/<id>', methods=['GET', 'POST'])
def edit_employee(id):
    ID = int( escape(id) )
    if request.method == 'GET':        
        return show_employee_edit_form(ID)
    FirstName = escape(request.form['FirstName'])
    LastName = escape(request.form['LastName'])
    Age = escape(request.form['Age'])
    Salary = escape(request.form['Salary'])
    Designation = escape(request.form['Designation'])
    sql = """UPDATE Employees 
    SET FirstName = %s,
    LastName = %s,
    Age = %s,
    Salary = %s,
    Designation = %s
    WHERE ID = %s"""
    val = (FirstName, LastName, Age, Salary, Designation, ID)
    mycursor.execute(sql, val)
    mydb.commit()
    if mycursor.rowcount > 0:
       message = "Employee Records updated successfully."
       flash(message)
    else:
        message = None    
    return redirect(url_for('index'))

def show_employee_edit_form(ID):
    sql = "SELECT * FROM Employees WHERE ID = %s"
    val = (ID,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    return render_template('edit-employee.html', employee = myresult)
