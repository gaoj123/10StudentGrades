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
    listGrades=getAllAverages() #list of dictionaries
    for dict in listGrades:
        c.execute("INSERT INTO peeps_avg VALUES(%s, %s)"%(dict["id"],dict["average"]))
    db.commit()

# Returns a list of grades for a student
def getGrades(id):
   c.execute("SELECT mark FROM courses WHERE id = %s;" % (str(id),))
   grades = []
   for grade in c:
      grades.append(grade[0])
   return grades

#Compute average using grades obtained from the list returned in getGrades()
def computeAverageFor(id):
   grades=getGrades(id)
   sum=0.0;
   gradeAverage=0.0;
   for grade in grades:
      sum+=grade
   gradeAverage = float(sum) / len(grades)
   return gradeAverage
      
#Returns a list of dictionaries, one for each student. Each dictionary has a student's name, id, and average under those keys.
def getAllAverages():
    students = []
    c.execute("SELECT id, name FROM peeps;")
    for row in c:
        dictToAdd = {}
        dictToAdd["id"] = row[0]
        dictToAdd["name"] = row[1]
        students.append(dictToAdd)
    #This is a roundabout way of evading the transient nature of SELECT statements
    for student in students:
        student["average"] = computeAverageFor(student["id"])
    return students
    """
    toReturn=[]
    for id in range(1,11):
        c.execute("SELECT name FROM peeps WHERE id="+str(id)+";")
        for row in c:
            dictToAdd={}
            dictToAdd["name"]=row[0]
            dictToAdd["id"]=id
            dictToAdd["average"]=float(computeAverageFor(id))
            toReturn.append(dictToAdd)
    return toReturn
    """

# Adds a record into the course table of all grades
def addGradeFor(id, course, grade):
    c.execute('INSERT INTO courses VALUES ("%s", %s, %s);' % (course, grade, id))
    db.commit()

#Updates averages in the db table "peeps_avg"
def updateAverages():
    records = getAllAverages()
    for student in records:
        if existsInTable("peeps_avg", student["id"]):
            c.execute("UPDATE peeps_avg SET average = %s;" % (student["average"],))
        else:
            c.execute("INSERT INTO peeps_avg VALUES (%d, %s);" % (student["id"], student["average"]))
    return 0

def existsInTable(table, id):
    id = str(id)
    c.execute("SELECT * FROM %s WHERE id = %s;" % (table, id))
    for record in c:
        return True
    return False


createGradebook()
print getGrades(1)
print computeAverageFor(1)
updateAverages()
db.commit()
db.close()
