import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
from flask import Flask, render_template

json_key = json.load(open('spreadsheet_credentials.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
gc = gspread.authorize(credentials)
 
#worksheet = wsh.sheet1 <-- this isnt needed

wsh = gc.open("Simple Sheet")
worksheet = wsh.sheet1
dessert_list = worksheet.col_values(2)
heroes_list = worksheet.col_values(1)
name = heroes_list[0]
dessert = dessert_list[0]
print name, dessert   
#mytable = worksheet.get_all_values()
#print mytable
global i, j
i = 0

for row in worksheet.get_all_values():
    i = i + 1
    #print str(i) + " " + "row"
    j = 0
    if row[0] == 'Red Guardian':
    	print row[0] +  " loves " + row[0]
	