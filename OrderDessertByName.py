import json
import gspread
from flask import Flask, render_template, request
from oauth2client.client import SignedJwtAssertionCredentials
json_key = json.load(open('spreadsheet_credentials.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
gc = gspread.authorize(credentials)


wsh = gc.open("Simple Sheet")
worksheet = wsh.sheet1
heroes_list = worksheet.col_values(1)
global default_name 
default_name = heroes_list[0]
print default_name


app = Flask(__name__) 



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=['POST'])
def submit():
    print request.form
    hero_name = request.form.get('hero name')
    print hero_name
    dessert = getDessertForHero(hero_name)
    return render_template("submit.html", name=hero_name, dessert=dessert)

def getDessertForHero(name):
    print "name= " + name 
    for row in worksheet.get_all_values():
        if row[0] == name:
            return row[1]        	
        
     


if __name__=='__main__':
    app.run(debug=True)