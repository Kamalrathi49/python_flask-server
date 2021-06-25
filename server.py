from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def homePage():
    return render_template('./index.html')


@ app.route('/about.html')
def aboutPage():
    return render_template('./about.html')


@app.route('/contact.html')
def contactPage():
    return render_template('./contact.html')


@app.route('/works.html')
def worksPage():
    return render_template('./works.html')


@app.route('/works/work.html')
def workPage():
    return render_template('./work.html')
