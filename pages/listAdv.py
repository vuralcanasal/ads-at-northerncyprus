#!C:/Users/Vural/AppData/Local/Programs/Python/Python36/python
import cgi
import sqlite3
import http.cookies as Cookie
import os


def printHeader(title,css,js):
	print("Content-type: text/html")
	print("")
	print("<html><head><title>{}</title><link rel='stylesheet' type='text/css' href='{}'></link><script src='{}'></script></head><body id='operationBack'>".format(title,css,js))
    
def printBody(ptitle,db,activeCont):
    
    #control for direct accessing
    if "HTTP_COOKIE" in os.environ:
        cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
        #control for direct accessing
        if "session" in cookie.keys():
            conn = sqlite3.connect("{}".format(db))
            c = conn.cursor()
            #find the user according to the sessionid
            c.execute("SELECT * FROM USER WHERE sessionid = ?",(cookie["session"].value,))
            row = c.fetchone()
            #if the user
            if row!=None:
                
                print("<div><p>{}<p>".format(row[0]))
                print("<h1>{}</h1>".format(ptitle))
                #go back button
                print("<button onClick='goOperationPage()' type='button'> Back </button>")
                print("<table><tr><th>Title</th><th>Description</th><th>Category</th><th>Activate/Deactivate</th></tr>")
                #select the necessary values
                c.execute("SELECT ADVERTISEMENT.title, ADVERTISEMENT.description, CATEGORY.cname, ADVERTISEMENT.isactive, ADVERTISEMENT.aid  from ADVERTISEMENT join CATEGORY on ADVERTISEMENT.cid = CATEGORY.cid where ADVERTISEMENT.username = '{}' ORDER BY dateadded DESC".format(row[0]))
                elements = c.fetchall()
                #if the values 
                if len(elements)!=0:
                         
                    for i in range(0,len(elements)):
                        print("<tr>")
                        print("<td>{}</td>".format(elements[i][0]))
                        print("<td>{}</td>".format(elements[i][1]))
                        print("<td>{}</td>".format(elements[i][2]))
                        #active/deactive buttons
                        if elements[i][3] == 1:
                            print("<td>")
                            print("<form method='GET' action='{}'>".format(activeCont))
                            print("<button type='submit' value='{}' name='activation' style='background-color:green'> To Deactivate </button>".format(elements[i][4]))
                            print("</form>")
                            print("</td>")
                        else:
                            print("<td>")
                            print("<form method='GET' action='{}'>".format(activeCont))
                            print("<button type='submit' value='{}'  name='activation' style='background-color:red'> To Active </button>".format(elements[i][4]))
                            print("</form>")
                            print("</td>")
                        print("</tr>")
                    print("</table>")                    
                    print("</div>")
                else:
                    print("</table>")
                    print("<br/><p style='color:blue;'>No advertisement found!!<p>")
                    print("<br/><br/><button onClick='goOperationPage()' type='button'> Back </button>")
                    print("</div>")
            else:
                print("<h2>Login required!!</h2>")
                print("<br/><br/><button onClick='goLogin()' type='button'> Login </button>")
            conn.commit()
            conn.close()
        else:
            print("<h2>Login required!!</h2>")
            print("<br/><br/><button onClick='goLogin()' type='button'> Login </button>")
    else:
        print("<h2>Login required!!</h2>")
        print("<br/><br/><button onClick='goLogin()' type='button'> Login </button>")
    
    
def printFooter():
    print("</body></html>")

#titles
title = "List ADV Page"
ptitle = "List Advertisements"
#css and js files location
css = "/ads-at-northerncyprus/css/index.css"
js = "/ads-at-northerncyprus/js/myfile.js"
#database location
db = "C:/xampp/htdocs/ads-at-northerncyprus/db/advNC.db"
#activation path
activeCont = "/ads-at-northerncyprus/control/activationCont.py"

printHeader(title,css,js)

printBody(ptitle,db,activeCont)

printFooter()    
