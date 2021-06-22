from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html') 

@app.route('/2')
def page2():
    return "this is 2nd page"