#!C:/Users/Vural/AppData/Local/Programs/Python/Python36/python
import cgi
import sqlite3
import http.cookies as Cookie
import os


def printHeader(title,css,js):
	print("Content-type: text/html")
	print("")
	print("<html><head><title>{}</title><link rel='stylesheet' type='text/css' href='{}'></link><script src='{}'></script></head><body id='operationBack'>".format(title,css,js))
    
def printBody(ptitle,control,db):
    
    #control for direct accessing
    if "HTTP_COOKIE" in os.environ:
        cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
        #control for direct accessing
        if "session" in cookie.keys():
            #connection into the db
            conn = sqlite3.connect("{}".format(db))
            c = conn.cursor()
            #find the user according to sessionid
            c.execute("SELECT * FROM USER WHERE sessionid = ?",(cookie["session"].value,))
            row = c.fetchone()
            #if the user
            if row!=None:
                print("<div><p>{}<p>".format(row[0]))
                print("<h1>{}</h1><form action='{}' method='POST'>".format(ptitle,control))
                print("Title <input type='text' name='title' required/><br/><br/>")
                print("Description <input type='text' name='description' required/><br/><br/>")
                #take the categor informations
                c.execute("SELECT * FROM CATEGORY")
                categories = c.fetchall()
                #print all categories as option
                print("Category <select name='categories' id='category'>")
                if categories!=None:
                    for i in range(0,len(categories)):
                        print("<option value='{}'>{}</option>".format(categories[i][1],categories[i][1]))
                print("</select>")
               
                print("<input type='submit' value='Submit'><br/>")
                print("<input type='reset' value='Clear'/>")
                print("</form>")
                print("<button type='back' onclick='goOperationPage()'> Back </button>")
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
title = "Create ADV Page"
ptitle = "New Advertisement"
#css and js files location
css = "/ads-at-northerncyprus/css/form.css"
js = "/ads-at-northerncyprus/js/myfile.js"
#database location
db = "C:/xampp/htdocs/ads-at-northerncyprus/db/advNC.db"
#control path
control = "/ads-at-northerncyprus/control/advControl.py"

printHeader(title,css,js)

printBody(ptitle,control,db)

printFooter()    
