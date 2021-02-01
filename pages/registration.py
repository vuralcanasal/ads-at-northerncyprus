#!C:/Users/Vural/AppData/Local/Programs/Python/Python36/python

def printHeader(title,css,js):
	print("Content-type: text/html")
	print("")
	print("<html><head><title>{}</title><link rel='stylesheet' type='text/css' href='{}'></link><script src='{}'></script></head><body>".format(title,css,js))

def printBody(control):

    print("<div><h1>Registration Form</h1><form action='{}' method='POST'>".format(control))
    print("User name <span style='color:green' id='checker'></span>")
    print("<input type='text' name='uname' onfocusout='checkusername(this.value)' placeholder='Your user name..' required /><br/><br/>")
    print("Password  <input type='password' name='pwd' placeholder='Your password..' required/><br/><br/>")
    print("Password again: <input type='password' name='pwd2' placeholder='Your password again..' required/><br/><br/>")
    print("Full name <input type='text' name='fullname' placeholder='Your full name..' required/><br/><br/>")
    print("E-mail <input type='text' name='email' placeholder='Your e-mail address..' required/><br/><br/>")
    print("Phone number <input type='tel' name='phone' placeholder='5554443322' pattern='[0-9]{10}' required><br><br>")
    print("<input type='submit' value='Submit'><br/>")
    print("<input type='reset' value='Clear'/>")
    print("</form>")
    print("<button type='back' onclick='goHome()'> Back </button>")
    print("</div>")

    
def printFooter():
    print("</body></html>")

#titles
title = "Registration Form"
#css and js files location
css = "/ads-at-northerncyprus/css/form.css"
js = "/ads-at-northerncyprus/js/myfile.js"
#control path
control = "/ads-at-northerncyprus/control/registrationControl.py"

printHeader(title,css,js)
printBody(control)
printFooter()