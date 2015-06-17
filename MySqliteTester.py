import sqlite3
conn = sqlite3.connect('bar.db')
db = conn.cursor()
stock_list = ["glug of rum", "slice of orange"]

def updateInventory(list_of_Ingredients):
    conn = sqlite3.connect('bar.db')
    db = conn.cursor()
    print list_of_Ingredients
    db.execute("SELECT * FROM ingredients WHERE name in (?) ", (stock_list,)) 
    results = db.fetchall()
    print results
    for row in results:
        print 'you have ' + str(row[3])  + ' ' + row[1] + ' left'
        #print " got item"            
        
    conn.commit()
       	
        
updateInventory(stock_list)
conn.close()
