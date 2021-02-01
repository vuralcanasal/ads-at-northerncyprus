#!C:/Users/Vural/AppData/Local/Programs/Python/Python36/python
import cgi
import sqlite3
import http.cookies as Cookie
import random
import os


def printHeader(title,css,js):
	print("Content-type: text/html")
	print("")
	print("<html><head><title>{}</title><link rel='stylesheet' type='text/css' href='{}'></link><script src='{}'></script></head><body>".format(title,css,js))
    
def printBody(ptitle,db):
    
    #control for direct accessing
    if "HTTP_COOKIE" in os.environ:
        cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
        #control for user login
        if "session" in cookie.keys():
            #connect into the db
            conn = sqlite3.connect("{}".format(db))
            c = conn.cursor()
            #find the user with the sessionid
            c.execute("SELECT * FROM USER WHERE sessionid = ?",(cookie["session"].value,))
            row = c.fetchone()
            #if the user is exist
            if row!=None:
                #update the user statu with logout
                c.execute("UPDATE USER SET sessionid = -1 WHERE username = ? AND password = ?", (row[0], row[1]))
                #close the cookie
                print("<script>")
                print("document.cookie = 'session=;expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';")
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

#titles
title = "Logout Page"
ptitle = "LOGOUT"
#css and js files location
css = "/ads-at-northerncyprus/css/message.css"
js = "/ads-at-northerncyprus/js/myfile.js"
#next location
enteredPage = "/ads-at-northerncyprus/index.py"
#database location
db = "C:/xampp/htdocs/ads-at-northerncyprus/db/advNC.db"

printHeader(title,css,js)

printBody(ptitle,db)

printFooter()    
