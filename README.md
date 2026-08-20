# Cyber Threat Tracker (Mini SIEM)

A lightweight Cyber Threat Intelligence tool built with Python & Flask. It deploys a honeypot to capture unauthorized login attempts, stores data in MySQL, and visualizes real-time metrics on a Chart.js dashboard.

## Features
- Honeypot Decoy: Traps malicious actors attempting brute-force logins.
- Threat Logging: Logs attacker IP addresses, submitted credentials, and attack timestamps.
- Visual Analytics: Interactive dashboard powered by Chart.js.

---

## Prerequisites
- Python (v3.x)
- MySQL Server / XAMPP (for local database management)

## Installation & Setup

1. Clone the repository:

   git clone [https://github.com/mfd-7/cyber-threat-tracker.git](https://github.com/mfd-7/cyber-threat-tracker.git)
   cd Cyber-Threat-Tracker

2. Create and activate a virtual environment:

For Windows (PowerShell):

python -m venv .venv
.\.venv\Scripts\Activate

For Linux / Mac:

python3 -m venv venv
source venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

## Database Setup

1. Start your MySQL server (e.g., via XAMPP Control Panel).

2. Open **phpMyAdmin** (`http://localhost/phpmyadmin`) and create a new database named:

threat_logger

3. Run the following SQL query to create the required table:

sql
CREATE TABLE attack_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ip_address VARCHAR(100),
    username VARCHAR(100),
    password VARCHAR(100),
    attack_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

## How to Run

1. Ensure your virtual environment is active and MySQL is running.

2. Run the application:
python app.py

3. Open your browser and access:
Honeypot Login Page: http://127.0.0.1:5000
Threat Dashboard: http://127.0.0.1:5000/dashboard