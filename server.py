from flask import Flask, render_template
app = Flask(__name__)


@app.route('/<username>/<int:post_id>')
def hello_world(username=None):
    return render_template('./index.html', name=username)


@ app.route('/2')
def page2():
    return "this is 2nd page"
