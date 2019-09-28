import csv
from flask import Flask, render_template

app = Flask(__name__)
application = app

@app.route('/<item>')
def put(item):
    return render_template('index.html', title='Hi', user={'username':item})

@app.route("/")
def index():
    user = {'username': 'World'}
    return render_template('index.html', title='Hi', user=user)

if __name__ == "__main__":
    app.run()
