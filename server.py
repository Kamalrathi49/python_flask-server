from flask import Flask, render_template, request
import csv
app = Flask(__name__)


@app.route('/<string:page_name>')
def homePage(page_name):
    return render_template(page_name)


def store_data_txt(data):
    with open("database.txt", 'a') as database:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        txtfile =  database.write(f"\n[ \n   name: {name}, \n   email: {email}, \n   subject: {subject}, \n   message: {message} \n]")

def store_data_csv(data):
    with open("database.csv", 'a') as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csvfile =  csv.writer(database2, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL, newline='')
        csvfile.writerow([name, email, subject, message]) 


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        store_data_txt(data)
        return "form submited"
    else:
        return 'something went wrong, try again later'
