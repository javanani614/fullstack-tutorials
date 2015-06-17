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
    #drink_type.append(request.form.get('drink_type'))
    drink_choices = request.form.getlist('my_choice')
    for choice in drink_choices:
        drink_type.append(choice)
        #drink.append = ingredients(choice)
        #print drink
    
    for item in drink_type:
        print "item = see line below"
        print item
        print ingredients.get(item)
        drink_ingredients.extend(ingredients.get(item))
        print drink_ingredients

    count_left_message = updateInventory(drink_ingredients)  #; break
    

    #drink_ingredients.append = ["rum"]
    return render_template("Bar.html", name=drink_type,ingredient_list=drink_ingredients,message=count_left_message)

def  updateInventory(list_of_Ingredients):
    conn = sqlite3.connect('bar.db')
    db = conn.cursor()
    print list_of_Ingredients
    out_message = []
    for eachIngredient in list_of_Ingredients:
        db.execute("SELECT * FROM ingredients WHERE name == ? ", (eachIngredient,)) 
        select_results = db.fetchall()
        print select_results
        for row in select_results:
            print row
            new_stock_level = row[3] + -1
            if new_stock_level > -1:
                out_message.append('Thars ' + str(new_stock_level)  + ' ' + row[1] + ' left')
                print " got " + eachIngredient +" item.  " + " Prior stck was " + str(row[3]) + "New stock = " + str(new_stock_level)
                my_command = "UPDATE ingredients SET stock={} WHERE id={}".format(new_stock_level, row[0])
                db.execute(my_command)
                conn.commit()
            else:
                out_message.append('sorry thars no more ' + eachIngredient )    
            #update_results = db.fetchall()
    return out_message
    
    conn.close()

if __name__=='__main__':
    app.run(debug=True)