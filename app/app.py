from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='db',
        user='root',
        password='rootpassword',
        database='userdb'
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        cursor.execute('INSERT INTO users (name) VALUES (%s)', (name,))
        conn.commit()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

