#!C:/Users/Vural/AppData/Local/Programs/Python/Python36/python
import cgi
import sqlite3
import http.cookies as Cookie
import os
from datetime import datetime

def printHeader(title,css,js):
	print("Content-type: text/html")
	print("")
	print("<html><head><title>{}</title><link rel='stylesheet' type='text/css' href='{}'></link><script src='{}'></script></head><body>".format(title,css,js))

def printBody(ptitle,form,db):
    print("<br/><h1>{}</h1>".format(ptitle))
    
    #control for direct accessing
    if "HTTP_COOKIE" in os.environ:
        cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
        #control for direct accessing
        if "session" in cookie.keys():
            conn = sqlite3.connect("{}".format(db))
            c = conn.cursor()
            #find the adv's activation value
            c.execute("SELECT isactive FROM ADVERTISEMENT WHERE aid = ?",form["activation"].value)
            row = c.fetchone()
            if row!=None:
                #if deactive make it active
                if row[0] == 0:
                    date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                    c.execute("UPDATE ADVERTISEMENT SET isactive = 1, dateadded = ? WHERE aid = ?",(date,form["activation"].value),)
                else:
                    c.execute("UPDATE ADVERTISEMENT SET isactive = 0 WHERE aid = ?",(form["activation"].value),)
                #go to next page
                print("<script>")
                print("window.location='{}';".format(enteredPage))
                print("</script>")
            else:
                print("<h2>Login required!!</h2>")
                print("<br/><br/><button class='back' onClick='goLogin()' type='button'> Login </button>")
            
            conn.commit()
            conn.close()
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
title = "Activation Message"
ptitle = "Activation"
#css and js files location
css = "/ads-at-northerncyprus/css/message.css"
js = "/ads-at-northerncyprus/js/myfile.js"
#next location
enteredPage = "/ads-at-northerncyprus/pages/listAdv.py"
#for form values
form = cgi.FieldStorage()

printHeader(title,css,js)
printBody(ptitle,form,db)
printFooter()
    