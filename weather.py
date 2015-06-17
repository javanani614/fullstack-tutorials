from flask import Flask, render_template
import requests

app = Flask(__name__)

#list = requests.get('http://api.wunderground.com/api/438861bec6f3a82d/conditions/q/CA/San_Francisco.json')

 
# Set up the SQLAlchemy Database to be a local file 'desserts.db'
def weather(city,state):
    weather_report = requests.get('http://api.wunderground.com/api/438861bec6f3a82d/conditions/q/city/state.json')
    print weather_report.json()



if __name__ == "__main__":

    # We need to make sure Flask knows about its views before we run
    # the app, so we import them. We could do it earlier, but there's
    # a risk that we may run into circular dependencies, so we do it at the
    # last minute here.
    city = "Cleveland"
    state = "OH"
    weather(city, state)
   

    app.run(debug=True)