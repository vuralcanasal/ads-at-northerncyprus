#!C:/Users/Vural/AppData/Local/Programs/Python/Python36/python
import os
import cgi
import sqlite3

#database location
db = "C:/xampp/htdocs/ads-at-northerncyprus/db/advNC.db"

print("Content-type: text/html")
print("")

query = os.environ["QUERY_STRING"]
#check the username is uniq, and inform the user before registration part
if(len(query)== 0):
    print("")
else:
    pairs = cgi.parse_qs(query)
    if "q" in pairs.keys():
        #connect into the db
        conn = sqlite3.connect("{}".format(db))
        c = conn.cursor()
        #check the username is uniq
        c.execute("SELECT * FROM user WHERE username = ?",(pairs["q"][0],))
        row = c.fetchone()
        if row == None:
            print("Valid")
        else:
            print("Invalid!!")
        conn.close()