import db_builder
import sqlite3
import csv

f="discobandit.db"
db = sqlite3.connect(f)
c = db.cursor()

# Creates database and tables from CSV
def createGradebook():
   db_builder.insertCSV(c)
   c.execute("CREATE TABLE peeps_avg (id INTEGER, average REAL);")
   db.commit()

# Returns a list of grades for a student
def getGrades(id):
   c.execute("SELECT mark FROM courses WHERE id = "+str(id)+";")
   grades = []
   for grade in c:
      grades.append(grade[0])
   return grades

#Compute average using grades obtained from the list returned in getGrades()
def computeAverageFor(id):
   grades=getGrades(id)
   sum=0.0;
   gradeAverage=0;
   for grade in grades:
      sum+=grade
   gradeAverage=sum/len(grades)
   return gradeAverage
      
#Returns a list of dictionaries, one for each student. Each dictionary has a student's name, id, and average under those keys.
def getAllAverages():
   toReturn=[]
   c.execute("SELECT * FROM peeps"+";")
   for row in c:
      print(row)
      dictToAdd={}
      dictToAdd["name"]=row[1]
      dictToAdd["id"]=row[0]
      dictToAdd["average"]=computeAverageFor(int(row[0]))
      toReturn.append(dictToAdd)
   #for element in toReturn:
      #for key in element:
         #print key, element[key]
   

# Adds a record into the course table of all grades
def addGradeFor(id, course, grade):
   c.execute('INSERT INTO courses VALUES ("%s", %s, %s);' % (course, grade, id))
   db.commit()

createGradebook()
print getGrades(1)
print computeAverageFor(1)
getAllAverages()
db.commit()
db.close()
