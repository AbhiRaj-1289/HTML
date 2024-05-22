from flask import Flask, render_template, request, redirect
import mysql.connector  # Use psycopg2 for PostgreSQL or pyodbc for SQL Server

app = Flask(__name__, template_folder='C:/HTML/Project1/Login Page')

# Database configuration
db_config = {
    'user': 'root',
    'password': 'Abhi@161891',
    'host': 'localhost',  # Or your database server's IP address
    'database': 'companydb'
}

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    email = request.form['Email']
    password = request.form['Password']

    # Connect to the database
    connection = mysql.connector.connect(**db_config)  # Use psycopg2.connect for PostgreSQL or pyodbc.connect for SQL Server
    cursor = connection.cursor(dictionary=True)

    # Check if the user exists
    cursor.execute("SELECT * FROM validation WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()

    cursor.close()
    connection.close()

    if user:
        return redirect('/Success')
    else:
        return 'Invalid email or password'

@app.route('/Success')
def success():
    return render_template('Success.html')

if __name__ == '__main__':
    app.run(debug=True)
