# app.py

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'saket',
}

# Database connection
def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print("Error connecting to MySQL:", err)
        return None

# Route to display "Hello, World!"
@app.route('/hello')
def hello():
    return 'Hello, World!'

# Route to display the list of users
@app.route('/users')
def users():
    connection = get_db_connection()
    if connection is not None:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        connection.close()
        return render_template('users.html', users=users)
    else:
        return "Error connecting to the database"

# Route to add a new user
@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']

        connection = get_db_connection()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (id,name,email,role) VALUES (%s, %s, %s, %s)", (id,name,email,role ))
            connection.commit()
            connection.close()
            return redirect(url_for('users'))
        else:
            return "Error connecting to the database"
    return render_template('new_user.html')

# Route to display a specific user's details
@app.route('/users/<int:user_id>')
def user_details(user_id):
    connection = get_db_connection()
    if connection is not None:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        connection.close()
        if user:
            return render_template('user_details.html', user=user)
        else:
            return "User not found"
    else:
        return "Error connecting to the database"

if __name__ == '__main__':
    app.run(debug=True)
