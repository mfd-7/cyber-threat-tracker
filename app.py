from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password='',
        database="threat_logger"
    )

@app.route('/', methods=['GET', 'POST'])
def honeypot():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        attacker_ip = request.remote_addr 

        print(f"\n🔥 ATTACK DETECTED! IP: {attacker_ip} | User: {username} | Pass: {password}\n")

        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO attack_logs (ip_address, username, password) VALUES (%s, %s, %s)"
        val = (attacker_ip, username, password)
        cursor.execute(sql, val)
        conn.commit()

        cursor.close()
        conn.close()

    return """
    <h1>Admin Control Panel</h1>
    <p>Unauthorized access is strictly prohibited!</p>
    <form method='POST'>
        Username: <input type='text' name='username'><br><br>
        Password: <input type='password' name='password'><br><br>
        <button type='submit'>Login</button>
    </form>
    """

@app.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attack_logs ORDER BY id DESC")
    logs = cursor.fetchall()

    cursor.execute("SELECT ip_address, COUNT(*) FROM attack_logs GROUP BY ip_address")
    ip_counts = cursor.fetchall()

    ips = [row[0] for row in ip_counts]
    counts = [row[1] for row in ip_counts]

    cursor.close()
    conn.close()

    return render_template('dashboard.html', logs=logs, ips=ips, counts=counts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)