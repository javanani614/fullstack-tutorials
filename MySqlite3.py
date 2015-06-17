import sqlite3
conn = sqlite3.connect('bar.db')
db = conn.cursor()
db.execute("SELECT * FROM ingredients;")
new_stock_level = 8
item_id =1
results = db.fetchall()
for row in results:
    print row[0], row[1], row[2], row[3]
my_command = "UPDATE ingredients SET stock={} WHERE id={}".format(new_stock_level, item_id)
db.execute(my_command)
db.execute("SELECT * FROM ingredients;")
results = db.fetchall()
for row in results:
    print row[0], row[1], row[2], row[3]

#print results
#conn.commit()
conn.close()
