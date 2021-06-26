from flask import Flask, render_template
app = Flask(__name__)


@app.route('/<string:page_name>')
def homePage(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return "form submited"



