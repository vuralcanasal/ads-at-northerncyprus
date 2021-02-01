#!C:/Users/Vural/AppData/Local/Programs/Python/Python36/python
import http.cookies as Cookie
import random
import cgi
import sqlite3

def printHeader(title,css,js):
	print("Content-type: text/html")
	print("")
	print("<html><head><title>{}</title><link rel='stylesheet' type='text/css' href='{}'></link><script src='{}'></script></head><body>".format(title,css,js))


def printBody(ptitle,form,db):
    print("<br/><h1>{}</h1>".format(ptitle))
    error = True
    #control for direct accessing
    if "uname" in form.keys() and "pwd" in form.keys():
        #connet into the db
        conn = sqlite3.connect("{}".format(db))
        c = conn.cursor()
        #check the user and password are correct
        c.execute("SELECT * FROM USER WHERE username = ? AND password = ?", (form["uname"].value, form["pwd"].value))
        row = c.fetchone()
        #if the user is found
        if row!=None:
            #create a uniq sessionid for the user
            sessionF=True
            #create the cookie for the user
            cookie = Cookie.SimpleCookie()
            #search a session id until finding a uniq one
            while(sessionF): 
                cookie["session"]=random.randint(1,1000000)
                c.execute("SELECT * FROM USER WHERE sessionid = ?",(cookie["session"].value,))
                row = c.fetchone()
                if row==None:
                    sessionF=False
            #set cookie values
            cookie["session"]["domain"] = "localhost"
            cookie["session"]["path"] = "/"
            #update the user's sessionid to be online
            c.execute("UPDATE USER SET sessionid = ? WHERE username = ? AND password = ?", (cookie["session"].value, form["uname"].value, form["pwd"].value))
            
            conn.commit()
            conn.close()
                        
            print("<h2 id='success'>Login is succesfull!</h2>")
            #set the cookie
            print("<script>")
            print("document.cookie = '{}';".format(cookie.output().replace("Set-Cookie: ", "")))
            print("window.location='{}';".format(enteredPage))
            print("</script>")
        else:
            print("<h2>The username or password is wrong! Try again please..</h2>")
            
    else:
            print("<h2>The username or password is wrong! Try again please..</h2>")
    print("<br/><br/><button class='back' onClick='goLogin()' type='button'> Back </button>")

def printFooter():
	print("</body></html>")


db = "C:/xampp/htdocs/ads-at-northerncyprus/db/advNC.db"
#titles
title = "Login Message"
ptitle = "Login Message"
#css and js files location
css = "/ads-at-northerncyprus/css/message.css"
js = "/ads-at-northerncyprus/js/myfile.js"
#next location
enteredPage = "/ads-at-northerncyprus/index.py"
#database location
form = cgi.FieldStorage()

printHeader(title,css,js)
printBody(ptitle,form,db)
printFooter()
