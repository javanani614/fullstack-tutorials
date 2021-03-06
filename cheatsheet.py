from flask import Flask, render_template, request
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
app = Flask(__name__)
 
def get_spreadsheet_data():
    json_key = json.load(open('spreadsheet_credentials.json'))
    scope = ['https://spreadsheets.google.com/feeds']
 
    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
    gc = gspread.authorize(credentials)
 
    sh = gc.open("Simple Sheet")
    sh = sh.sheet1
    allval = sh.get_all_values()
    return allval
 
 
@app.route("/")
def index():
    return render_template("index.html")
 
 
@app.route("/templates/submit", methods=['POST'])
def submit():
    name = request.form.get('name')
    return render_template("submit.html", name=name)
 
if __name__=='__main__':
    app.run(debug=True)