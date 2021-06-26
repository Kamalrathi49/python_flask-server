from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/<string:page_name>')
def homePage(page_name):
    return render_template(page_name)


def store_data(data):
    with open("database.txt", 'a') as database:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file =  database.write(f"\n name:{name}, email:{email}, subject{subject}, message:{message}")
    


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        store_data(data)
        return "form submited"
    else:
        return 'something went wrong, try again later'
