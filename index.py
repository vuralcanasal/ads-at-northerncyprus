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
    
def printBody(ptitle,db,form):
    
    #connect into the db
    conn = sqlite3.connect("{}".format(db))
    c = conn.cursor()
    row = []
    #if the user online
    if "HTTP_COOKIE" in os.environ:
        cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
        #if the user online
        if "session" in cookie.keys():
            #find the user according to the sessionid
            c.execute("SELECT * FROM USER WHERE sessionid = ?",(cookie["session"].value,))
            row = c.fetchone()
            #if the user
            if row != None:
                print("<br/><p style='color:white;'> Welcome {}<p>".format(row[0]))
                print("<button class='login' onClick='goOperationPage()' type='button'> Operation </button>");
                print("<button class='registration' onClick='goLogoutControl()' type='button'> Logout </button>");
            #in chrome, sometimes session can be in cookie but row is none
            #although session must not be in cookie
            else:
                print("<br/><button class='login' onClick='goLogin()' type='button'> Login </button>");
                print("<button class='registration' onClick='goRegistration()' type='button'> Registration </button>");
    #if the user offline
    else:
        print("<br/><button class='login' onClick='goLogin()' type='button'> Login </button>");
        print("<button class='registration' onClick='goRegistration()' type='button'> Registration </button>");
    
    
    print("<h1>{}</h1>".format(ptitle))
    #form for search box
    print("<form class='search' action='/ads-at-northerncyprus/index.py'>")
    print("<input type='text' placeholder='Search..' name='search'>")
    print("<button type='submit'> Search </i></button>")
    print("</form>")
    
    #find the number of category
    c.execute("SELECT COUNT(*) FROM CATEGORY")
    numberOFcategory = c.fetchone()
    if numberOFcategory!=None:
        #create the table for every category
        for i in range(0,numberOFcategory[0]):
            #find the category
            c.execute("SELECT cname FROM CATEGORY WHERE cid = ?",(i+1,))
            cname = c.fetchone()        
            print("<div>")
            print("<h2>{}</h2>".format(cname[0]))
            print("<table><tr><th>Title</th><th>Description</th><th>Contact Full name</th><th>Contact Email</th><th>Contact Telephone Number</th></tr>")
            #if used the search button show all advs if the title or description includes the keyword
            if("search" in form.keys()):
                c.execute("SELECT title, description,fullname,email, telno from ADVERTISEMENT INNER JOIN USER ON ADVERTISEMENT.username = USER.username where cid = ? and isactive = 1 and (title like ? or description like ?)",(i+1,'%'+form["search"].value.upper()+'%','%'+form["search"].value.upper()+'%',))
            else:
                c.execute("SELECT title, description,fullname,email, telno from (SELECT * FROM ADVERTISEMENT where isactive = 1 order by dateadded DESC LIMIT 5) limited INNER JOIN USER ON limited.username = USER.username where cid = ?",(i+1,))
            
            #show the values of the table    
            adv = c.fetchall()
            if adv!=[]:
                for j in range(0,len(adv)):
                    print("<tr>")
                    print("<td>{}</td>".format(adv[j][0]))
                    print("<td>{}</td>".format(adv[j][1]))
                    print("<td>{}</td>".format(adv[j][2]))
                    print("<td>{}</td>".format(adv[j][3]))
                    print("<td>{}</td>".format(adv[j][4]))
                    print("</tr>")
                
                print("</table>")
                print("</div><br/>")
            else:
                print("</table>")
                print("<br/><p style='color:black; text-align:center;'>No Active Advertisement found !!<p>")
                print("</div><br/>")
        
    
    conn.close()
    
    
def printFooter():
    print("</body></html>")

#titles
title = "Advertisment North Cyprus"
ptitle = "Advertisments in North Cyprus"
#css and js files location
css = "/ads-at-northerncyprus/css/index.css"
js = "/ads-at-northerncyprus/js/myfile.js"
#database location
db = "C:/xampp/htdocs/ads-at-northerncyprus/db/advNC.db"
#for form values
form = cgi.FieldStorage()

printHeader(title,css,js)

printBody(ptitle,db,form)

printFooter()    
