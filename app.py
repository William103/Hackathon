import csv
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from config import Config

# set up form
class LoginForm(FlaskForm):
    zipcode = StringField('Zip Code', validators=[DataRequired()])

app = Flask(__name__)
app.config.from_object(Config)
application = app

GoogleMaps(
        app,
        key = "AIzaSyASdoTGdVwSsYkr_ir1sK3IWKuWSfSVeng"
)


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
