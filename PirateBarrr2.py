from flask import Flask, render_template, request
import sqlite3
#conn = sqlite3.connect('bar.db')
#db = conn.cursor()




app = Flask(__name__) 
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

#start


#db.execute("SELECT * FROM ingredients;")
#results = db.fetchall()
#   print row
#    print ""
#end
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
    drink_ingredients = []
    drink_type.append(request.form.get('drink_type'))
    drink_choices = request.form.getlist('my_choice')
    for choice in drink_choices:
        drink_type.append(choice)
        #drink.append = ingredients(choice)
        #print drink
    
    for item in drink_type:
        print "item = see line below"
        print item
        print ingredients.get(item)
        drink_ingredients = ingredients.get(item)
        print drink_ingredients
        #for eachIngredient in drink_ingredients:
            #print eachIngredient
            #updateInventory(eachIngredient); break
    

    #drink_ingredients.append = ["rum"]
    return render_template("Bar.html", name=drink_type,ingredient_list=drink_ingredients)

def updateInventory(inv_item):
    conn = sqlite3.connect('bar.db')
    db = conn.cursor()
    print inv_item
    db.execute("SELECT * FROM ingredients WHERE name == ? ", (inv_item,)) 
    results = db.fetchall()
    print results
    for row in results:
        print 'you have ' + row['stock'] 
        #print " got item"            
        
    conn.commit()
    conn.close()

if __name__=='__main__':
    app.run(debug=True)