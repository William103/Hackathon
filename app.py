<<<<<<< HEAD
<iframe src="https://www.google.com/maps/d/u/0/embed?mid=1NP8CSmjn-Vj4kiPdoxYZ7Yk2cGLy9Zfp" width="640" height="480"></iframe>
=======
import csv
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from config import Config

class LoginForm(FlaskForm):
    zipcode = StringField('Zip Code', validators=[DataRequired()])

app = Flask(__name__)
app.config.from_object(Config)
application = app

@app.route('/', methods=['GET', 'POST'])
def getzip():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/info')
    return render_template('index.html', title='Hi', form=form)

@app.route('/<item>')
def put(item):
    return render_template('index.html', title='Hi', user={'username':item})

@app.route("/info")
def index():
    test_legal = [
            {
                'state': 'CA',
                'service': 'representation',
                'name': 'California Representation'
            },
            {
                'state': 'PA',
                'service': 'expungements',
                'name': 'PLSE'
            }
    ]
    return render_template('index.html', title='Hi', legal=test_legal)

if __name__ == "__main__":
    app.run()
>>>>>>> 39b61ed6c2d6fec06cb5c06e4d92eb6dd320ae90
