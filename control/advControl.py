#!C:/Users/Vural/AppData/Local/Programs/Python/Python36/python
import cgi
import sqlite3
from datetime import datetime
import http.cookies as Cookie
import os

def printHeader(title,css,js):
	print("Content-type: text/html")
	print("")
	print("<html><head><title>{}</title><link rel='stylesheet' type='text/css' href='{}'></link><script src='{}'></script></head><body>".format(title,css,js))


def printBody(ptitle,form,db):
    print("<br/><h1>{}</h1>".format(ptitle))
    
    #control for direct accessing
    if "HTTP_COOKIE" in os.environ:
        cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
        #control for user login
        if "session" in cookie.keys():
            #connect into the db
            conn = sqlite3.connect("{}".format(db))
            c = conn.cursor()
            #find the user with the sessionid
            c.execute("SELECT username FROM USER WHERE sessionid = ?",(cookie["session"].value,))
            fusername = c.fetchone()
            #find the category values
            c.execute("SELECT cid FROM CATEGORY WHERE cname = ?",(form["categories"].value,))
            fcid = c.fetchone()
            #if the username exist
            if fusername!=None:
                #create the date for the adv
                date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                #create an id
                c.execute("SELECT COUNT(*) FROM ADVERTISEMENT")
                cid = c.fetchone()
                #insert the data into the db
                c.execute("INSERT INTO ADVERTISEMENT VALUES(?,?,?,?,?,?,?)", (cid[0]+1, fcid[0], fusername[0], form["title"].value.upper(), form["description"].value.upper(),date,1))
            conn.commit()
            conn.close()
            print("<h2 id='success'>ADVERTISEMENT was added successfully</h2>")
            print("<br/><br/><button class='back' onClick='goOperationPage()' type='button'> Back </button>")
        else:
            print("<h2>Login required!!</h2>")
            print("<br/><br/><button class='back' onClick='goLogin()' type='button'> Login </button>")
    else:
        print("<h2>Login required!!</h2>")
        print("<br/><br/><button class='back' onClick='goLogin()' type='button'> Login </button>")    
     
    

def printFooter():
	print("</body></html>")

#database location   
db = "C:/xampp/htdocs/ads-at-northerncyprus/db/advNC.db"
#titles
title = "Advertisement Operand"
ptitle = "Advertisement"
#css and js files location
css = "/ads-at-northerncyprus/css/message.css"
js = "/ads-at-northerncyprus/js/myfile.js"
#for form values
form = cgi.FieldStorage()


printHeader(title,css,js)
printBody(ptitle,form,db)
printFooter()
