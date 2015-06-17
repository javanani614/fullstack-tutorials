from flask import Flask, render_template, request
import sqlite3
#conn = sqlite3.connect('bar.db')
#db = conn.cursor()




app = Flask(__name__) 



@app.route("/")
def index():
    return render_template("index5.html")

@app.route("/Pirate", methods=['POST'])
def Pirate():
    return render_template("PirateRequest.html")


@app.route("/Bar", methods=['POST'])
def Bar():
    #print request.form
    drink_type = []
    drink_type.append(request.form.get('drink_type'))
    drink_choices = request.form.getlist('my_choice')
    #drink_type = drink_choices
    #print drink_type[0] + " " + drink_type[1]
    for choice in drink_choices:
        drink_type.append(choice)
        print drink_type
 
    return render_template("Bar.html", name=drink_type)

#def getIngredient(drink_type):
#    print "name= " + name 
#    for row in worksheet.get_all_values():
#        if row[0] == name:
#            return row[1]        	
        
     


if __name__=='__main__':
    app.run(debug=True)