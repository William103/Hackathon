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

geolocator = Nominatim(user_agent="Hackathon")

# set up form
class LoginForm(FlaskForm):
    address = StringField('Enter your address here', validators=[DataRequired()])

# set up Flask app
app = Flask(__name__)
app.config.from_object(Config)
application = app

# set up Google Maps api key
GoogleMaps(
        app,
        key = "AIzaSyASdoTGdVwSsYkr_ir1sK3IWKuWSfSVeng"
)


location = (0, 0)
form = 0
state = 'PA'
@app.route('/', methods=['GET', 'POST'])
def getzip():
    global info
    global form
    global state
    form = LoginForm()
    if form.validate_on_submit():
        with open("csv_files\\Generalcomparison.csv", newline='') as f:
            reader = csv.reader(f)
            string = form.data['address'].split(' ')
            for row in reader:
                if row[0] == string[-1] or row[1] == string[-1] or row[2] == string[-1] or row[2] == string[-1]:
                    state = row[1]
                    info = row[-1]
            if info == 0:
                return render_template('index.html', title='Expungenation', form=form)
        return redirect('/info')
    return render_template('index.html', title='Expungenation', form=form)


# provide information
@app.route("/info", methods=['GET', 'POST'])
def index():
    global location
    global form
    global geolocator
    global state
    if form.validate_on_submit():
        getzip()
    location = geolocator.geocode(form.data['address'])
    location = (location.latitude, location.longitude)
    test = ''
    tests = []
    with open("csv_files\\StateAddresses2.csv", newline='') as f:
        reader = csv.reader(f)
        entities = []
        coords = []
        for row in reader:
            if row[0] == state:
                entities.append(row)
                coords.append((row[-2], row[-1]))
        distances = []
        for coord in coords:
            distances.append(geodesic(coord, location).miles)
        distances = zip(distances, entities)
        entities = [x for _, x in sorted(distances)]
        coords.append(location)
        return render_template('index.html', title='Expungenation', info=info,
                entities=entities, location=location, marker=coords, table=1,
                form=form)

if __name__ == "__main__":
    app.run()
