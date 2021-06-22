from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Kamal!' 

@app.route('/2')
def page2():
    return "this is 2nd page"