from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def homePage():
    return render_template("index.html")


def store_data_txt(data):
    with open("database.txt", 'a') as database:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        txtfile =  database.write(f"\n[ \n   name: {name}, \n   email: {email}, \n   subject: {subject}, \n   message: {message} \n]")

def store_data_csv(data):
    with open("database.csv", "a", newline="") as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csvfile =  csv.writer(database2, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        csvfile.writerow([name, email, subject, message]) 


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        store_data_txt(data)
        return render_template("thankyou.html", thankyou="Thank you ,", msg="I will be in touch with you shortly")
    else:
        return render_template("thankyou.html", thankyou=None, msg="'something went wrong, try again later'")
