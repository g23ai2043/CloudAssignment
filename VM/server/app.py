from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db_config = {
    'host': 'VM_RollNumber_2_IP',   # Replace with actual IP address of VM_RollNumber_2
    'user': 'testuser',
    'password': 'password',
    'database': 'testdb',
    'auth_plugin': 'mysql_native_password'  # For MySQL 8.0+
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Connect to MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert data into MySQL
        sql = "INSERT INTO records (name, email) VALUES (%s, %s)"
        val = (name, email)
        cursor.execute(sql, val)
        conn.commit()

        cursor.close()
        conn.close()

        return 'Data inserted successfully'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
