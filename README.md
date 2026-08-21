# Cyber Threat Tracker (Mini SIEM) with Machine Learning

# What is this project actually doing ?
Imagine you set up a fake 'Admin Login' page (a Honeypot) on the internet. Hackers and malicious bots think it's a real vault and try to break in by guessing passwords. 

This project acts as that fake vault. It secretly catches the attacker's IP address, the username and the password they tried to use. On top of that, we have added an "AI Security Guard (Machine Learning)"! The ML model instantly analyzes their input size and behavior to predict if the attack is a 'High Threat' (done by a fast automated bot/hacker) or a 'Low Threat' (just a normal human typo). You can watch all these attacks happening in real-time on a beautifully visualized Dashboard!

---

# Features
- **Honeypot Decoy:** Traps malicious actors attempting brute-force logins.
- **Smart Threat Logging:** Logs attacker IP addresses, submitted credentials, and attack timestamps into a MySQL database.
- **Machine Learning Integration (Decision Tree):** Automatically analyzes the login data and flags the incident as "High Threat 🚨" or "Low Threat ✅".
- **Visual Analytics:** Interactive dark-themed SOC dashboard powered by Chart.js with Threat Level badges.

---

# Prerequisites
- Python (v3.x)
- MySQL Server / XAMPP (for local database management)
- Required Python Libraries: `Flask`, `mysql-connector-python`, `scikit-learn`, `pandas`

---

# Installation & Setup

1. **Clone the repository:**
   ```bash
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

# Database Setup

1. Start your MySQL server (e.g., via XAMPP Control Panel).

2. Open **phpMyAdmin** (`http://localhost/phpmyadmin`) and create a new database named:

threat_logger

3. Run the following SQL query to create the required table:

SQL
CREATE TABLE attack_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ip_address VARCHAR(100),
    username VARCHAR(100),
    password VARCHAR(100),
    threat_level VARCHAR(50) DEFAULT 'Unknown',
    attack_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

# How to Run

1. Ensure your virtual environment is active and MySQL is running.

2. Train the ML Model: Before running the server, you need to train the AI model. Run this command once:

python train_model.py

3. Run the application:
python app.py

4. Open your browser and access:

Honeypot Login Page: http://127.0.0.1:5000
Threat Dashboard: http://127.0.0.1:5000/dashboard