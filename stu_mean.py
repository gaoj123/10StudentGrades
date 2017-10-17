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

# Adds a record into the course table of all grades
def addGradeFor(id, course, grade):
   c.execute('INSERT INTO courses VALUES ("%s", %s, %s);' % (course, grade, id))
   db.commit()

createGradebook()
print getGrades(1)

db.commit()
db.close()
