import sqlite3
import csv

f="discobandit.db"
db=sqlite3.connect(f)
c=db.cursor()

def getGrades(id):
   temp=[]
   c.execute("SELECT * FROM classes WHERE id = "+str(id)+";")
   for row in c:
       temp.append(row[1])
   return temp
    
##command=""
##c.execute(command)
print(getGrades(1))

db.commit()
db.close()
