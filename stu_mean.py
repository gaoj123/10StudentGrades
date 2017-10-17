import sqlite3
import csv

f="discobandit.db"
db=sqlite3.connect(f)
c=db.cursor()

def getGrades(id):
   c.execute("SELECT * FROM classes WHERE id = "+str(id)+";")
   for row in c:
       print row
    
##command=""
##c.execute(command)
getGrades(1)

db.commit()
db.close()
