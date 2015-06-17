import json
import gspread
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


from flask import Flask, render_template
app = Flask(__name__) 


@app.route('/')
def index():
    return 'Hello %s' % default_name
    #return render_template("index_html")

@app.route('/hello')
def hello1():
    return render_template('hello_name.html',name=default_name)

@app.route('/hello/<name>')
def hello2(name):
	#return name
    return render_template('hello_name.html',name=name)

if __name__=='__main__':
    app.run(debug=True)