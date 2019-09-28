import os
import csv
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from config import Config
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

state = 'PA'

# set up geolocator
geolocator = Nominatim(user_agent="Hackathon")
location = geolocator.geocode("500 College Avenue PA")
print((location.latitude, location.longitude))

# set up distance measurements
newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(geodesic(newport_ri, cleveland_oh).miles)

# set up form
class LoginForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired()])

# set up Flask app
app = Flask(__name__)
app.config.from_object(Config)
application = app

# set up Google Maps api key
GoogleMaps(
        app,
        key = "AIzaSyASdoTGdVwSsYkr_ir1sK3IWKuWSfSVeng"
)


# get address
info = 0
@app.route('/', methods=['GET', 'POST'])
def getzip():
    global info
    form = LoginForm()
    if form.validate_on_submit():
        with open("csv_files\\Generalcomparison.csv", newline='') as f:
            reader = csv.reader(f)
            string = form.data['address'].split(' ')
            for row in reader:
                if row[0] == string[-1] or row[1] == string[-1] or row[2] == string[-1]:
                    info = row[-1]
            if info == 0:
                location = geolocator.geocode(form.data['address'])
                location = (location.longitude, location.latitude)
                return render_template('index.html', title='Hi', form=form, location=location)
        return redirect('/info')
    return render_template('index.html', title='Hi', form=form)


# provide information
@app.route("/info")
def index():
    return render_template('index.html', title='Hi', info=info)
if __name__ == "__main__":

    # run app
    app.run()
