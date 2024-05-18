from flask import Flask, render_template, request, redirect  # Import redirect
from pymongo import MongoClient

app = Flask(__name__, template_folder='C:/HTML/Projects/Login Page')

client = MongoClient('mongodb+srv://abhiraj61002:Abhi@161891clusterdb.tr5lyq3.mongodb.net/Authentication')

db = client['Authentication']
collection = db['Values']

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    email = request.form['Email']
    password = request.form['Password']

    user = collection.find_one({'Email': email, 'Password': password})

    if user:
        return redirect('/Success')  # Redirect to success.html upon successful login
    else:
        return 'Invalid email or password'

@app.route('/Success')  # Define the /success route
def success():
    return render_template('Success.html')

if __name__ == '__main__':
    app.run(debug=True)
