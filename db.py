import sqlite3

def create_tables():
    #If the tables is not in the db create them
    
    # Create CATEGORY table  
    c.execute("""CREATE TABLE IF NOT EXISTS CATEGORY (
                cid INTEGER PRIMARY KEY,
                cname TEXT NOT NULL)""")
    # Create USER table
    c.execute("""CREATE TABLE IF NOT EXISTS USER (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                fullname TEXT NOT NULL,
                email TEXT NOT NULL,
                telno TEXT NOT NULL,
                sessionid TEXT NOT NULL)""")
    #Create ADVERTISEMENT table
    c.execute("""CREATE TABLE IF NOT EXISTS ADVERTISEMENT (
                aid INTEGER PRIMARY KEY,
                cid INTEGER NOT NULL,
                username TEXT NOT NULL,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                dateadded TEXT NOT NULL,
                isactive INTEGER NOT NULL,
                
                FOREIGN KEY(cid) REFERENCES CATEGORY(cid),
                FOREIGN KEY(username) REFERENCES USER (username))""")
                                
def addCategoryInitial():
    #Initial values for category table
    categories = ['Clothes', 'Technology', 'Car', 'Food', 'Drink']
    #Add the values into the category table
    for i in range (0,len(categories)):
        c.execute("INSERT INTO CATEGORY (cid,cname) VALUES(?,?)", (c.lastrowid+1,categories[i]))
    
if __name__ == "__main__":
    #Create connection with the db
    conn = sqlite3.connect("C:/xampp/htdocs/ads-at-northerncyprus/db/advNC.db")
    c = conn.cursor()
    #Create tables into the db and add initial values
    create_tables()
    addCategoryInitial()
    
    conn.commit()
    conn.close()
    