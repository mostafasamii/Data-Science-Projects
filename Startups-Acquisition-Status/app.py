from flask import Flask, render_template, request
import startups as startup
from geopy.geocoders import Nominatim
import numpy as np

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        founded_at = int(request.form['founded_at'])

        #Assume company is operating
        isClosed = 0
        activedays = (2021 - founded_at)*365

        #get the latitude and magnitude from the user using GeoPy
        geolocator = Nominatim(user_agent='startup status prediction')
        location = geolocator.geocode(request.form['location'])
        lat, lng = location.latitude, location.longitude
       
        funding_rounds = request.form['funding rounds']
        funding_total_usd = request.form['funding total usd']
        milestones = request.form['milestones']
        relationships = request.form['relationships']
        category_code = request.form['category code']
        country_code = request.form['country code']

        user_input = []
        user_input.append(founded_at)
        user_input.append(funding_rounds)
        user_input.append(funding_total_usd)
        user_input.append(milestones)
        user_input.append(relationships)
        user_input.append(lat)
        user_input.append(lng)
        user_input.append(isClosed)
        user_input.append(activedays)
        user_input.append(category_code.lower)
        user_input.append(country_code.capitalize)

        user_input_y = np.asarray(user_input)
        startup_pred = startup.startup_prediction(user_input_y).title()

        #you will be passing user_startup in index.html to show the result
        return render_template("sub.html", startup_pred=startup_pred)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)