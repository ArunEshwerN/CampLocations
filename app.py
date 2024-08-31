from flask import Flask, redirect, render_template, url_for, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Function to establish a connection to the SQLite database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_users'

mysql = MySQL(app)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/viewpage')
def viewpage():
    return render_template('view.html')

@app.route('/indexpage')
def indexpage():
    return render_template('index.html')

@app.route('/newcomment')
def newcomment():
    return render_template('new_comment.html')

@app.route('/new_camp')
def new_camp():
    return render_template('new_camp.html')


# Route to render the registration page
@app.route('/register')
def register():
    return render_template('register.html')

# Route to render the login page back from register page
@app.route('/loginagain')
def loginagain():
    return render_template('login.html')

@app.route('/searchpage')
def searchpage():
    return render_template('search.html')



# Route to handle registration
@app.route('/checkloginagain', methods=['POST'])
def checkloginagain():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        # Check if username already exists in the database
        cur.execute("SELECT * FROM tbl_users WHERE username = %s", (username,))
        existing_user = cur.fetchone()
        if existing_user:
            # If username already exists, render registration template with error message
            return render_template('register.html')
        else:
            # Insert new user into the database
            cur.execute("INSERT INTO tbl_users (username, password) VALUES (%s, %s)", (username, password))
            mysql.connection.commit()
            cur.close()
            # Redirect to login page after successful registration
            return redirect(url_for('login'))
    else:
        # Render registration template
        return render_template('register.html')
    

# Route to handle form submission
@app.route('/signin', methods=['POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT username, password FROM tbl_users WHERE username = '{username}' AND password = '{password}'")
        user = cur.fetchone()
        cur.close()
        if user is not None and password == user[1]:
            return render_template('index.html')
        else:
            # If user does not exist or password is incorrect, render login template with error message
            return render_template('login.html', error='Invalid username or password')
    else:
        render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
