#!C:/Users/Vural/AppData/Local/Programs/Python/Python36/python
import cgi
import sqlite3
import http.cookies as Cookie
import os


def printHeader(title,css,js):
	print("Content-type: text/html")
	print("")
	print("<html><head><title>{}</title><link rel='stylesheet' type='text/css' href='{}'></link><script src='{}'></script></head><body id='operationBack'>".format(title,css,js))
    
def printBody(ptitle,db):
    
    #control for direct accessing
    if "HTTP_COOKIE" in os.environ:
        cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
        #control for direct accessing
        if "session" in cookie.keys():
        #connect into the db
            conn = sqlite3.connect("{}".format(db))
            c = conn.cursor()
            #find the user according to the sessionid
            c.execute("SELECT * FROM USER WHERE sessionid = ?",(cookie["session"].value,))
            row = c.fetchone()
            #if the user 
            if row!=None:
                print("<div><p>{}<p>".format(row[0]))
                print("<h1>{}</h1>".format(ptitle))
                print("<button type='operation' onclick='createAdv()'> New Advertisement </button>")
                print("<button type='operation' onclick='listAdv()'> List Advertisements </button>")
                print("<br/><br/>")
                print("<button type='back' onclick='goHome()'> Back </button>")
                print("</div>")

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

#titles
title = "Operation Page"
ptitle = "Operations"
#css and js files location
css = "/ads-at-northerncyprus/css/form.css"
js = "/ads-at-northerncyprus/js/myfile.js"
#database location
db = "C:/xampp/htdocs/ads-at-northerncyprus/db/advNC.db"


printHeader(title,css,js)

printBody(ptitle,db)

printFooter()    
