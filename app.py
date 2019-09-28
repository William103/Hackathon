<<<<<<< HEAD
<iframe src="https://www.google.com/maps/d/u/0/embed?mid=1NP8CSmjn-Vj4kiPdoxYZ7Yk2cGLy9Zfp" width="640" height="480"></iframe>
=======
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
>>>>>>> 39b61ed6c2d6fec06cb5c06e4d92eb6dd320ae90
