#!C:/Users/Vural/AppData/Local/Programs/Python/Python36/python
import cgi
import sqlite3

def printHeader(title,css,js):
	print("Content-type: text/html")
	print("")
	print("<html><head><title>{}</title><link rel='stylesheet' type='text/css' href='{}'></link><script src='{}'></script></head><body>".format(title,css,js))


def printBody(ptitle,form,db):
    print("<br/><h1>{}</h1>".format(ptitle))
    error = True
    #control for direct accessing to the page
    if "uname" in form.keys() and "pwd" in form.keys():
        #check username
        if len(form["uname"].value) < 5:
            print("<h2>The username length should be at least 5!</h2>")
        #check password
        elif len(form["pwd"].value) < 5:
            print("<h2>The password length should be at least 5!</h2>")
        elif form["pwd"].value != form["pwd2"].value:
            print("<h2>The password should be re-entered correctly!</h2>")
        else:
            #connet into the db
            conn = sqlite3.connect("{}".format(db))
            c = conn.cursor()
            #check the username is valid
            c.execute("SELECT * FROM USER WHERE username = ?", (form["uname"].value,))
            row = c.fetchone()
            if row!=None:
                print("<h2>Username exists! Try new one please..</h2>")
            #if every things are fine
            else:
                error=False
                #insert the data into the db
                c.execute("INSERT INTO USER VALUES(?,?,?,?,?,?)", (form["uname"].value, form["pwd"].value, form["fullname"].value.upper(), form["email"].value.upper(), form["phone"].value,'-1'))
                print("<h2 id='success'>Successfully added</h2>")
                print("<br/><br/><button class='back' onClick='goHome()' type='button'> Home Page </button>")
    
    if error:
        print("<br/><br/><button class='back' onClick='goRegistration()' type='button'> Registration </button>")
    
    conn.commit()
    conn.close()

def printFooter():
	print("</body></html>")

#database location    
db = "C:/xampp/htdocs/ads-at-northerncyprus/db/advNC.db"
#titles
title = "Registration Message"
ptitle = "Registration Message"
#css and js files location
css = "/ads-at-northerncyprus/css/message.css"
js = "/ads-at-northerncyprus/js/myfile.js"
#for form values
form = cgi.FieldStorage()


printHeader(title,css,js)
printBody(ptitle,form,db)
printFooter()
