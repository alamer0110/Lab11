import sqlite3
import base64
import webbrowser

db = sqlite3.connect("week11.db")
ID = input("Enter the ID: ")
Stop = False
if ID == "q":
    Stop = True
while int(ID)<1 or int(ID)>24:
    if Stop:
        break
    ID = input("Enter the ID: ")
    if ID == "q":
        Stop = True
        break
if not Stop:
    Data = db.execute("select link from Lab10 where id = ?",(ID,))
    Data = list(Data)
    Link = Data[0][0]
    #print(Link)
    URL = base64.b64decode(Link)
    #print(URL)
    webbrowser.open(URL)
    City = input("Enter the City: ")
    Country = input("Enter the Country: ")
    db.execute("update Lab10 set city = ?,country = ? where id = ?",(City,Country,ID))
    db.commit()
    