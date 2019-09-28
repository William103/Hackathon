import csv
import gmaps
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from config import Config

# set up google maps api
with open('apikey.txt') as f:
    api_key = f.readline()
gmaps.configure(api_key=api_key)
new_york_coordinates = (40.75, -74.00)
gmaps.figure(center=new_york_coordinates, zoom_level=12)


# set up form
class LoginForm(FlaskForm):
    zipcode = StringField('Zip Code', validators=[DataRequired()])

app = Flask(__name__)
app.config.from_object(Config)
application = app


# get zip code
@app.route('/', methods=['GET', 'POST'])
def getzip():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/info')
    return render_template('index.html', title='Hi', form=form)


# provide information
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
