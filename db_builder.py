import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f = "discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

# Deal with students
peepsFile = open("peeps.csv", "r")
students = csv.DictReader(peepsFile)
command = "CREATE TABLE peeps (id INTEGER PRIMARY KEY, name STRING, age INTEGER);"
c.execute(command)    #run SQL statement
for row in students:
    values = '(' + row['id'] + ', "' + row['name'] + '", ' + row['age'] + ');'
    c.execute("INSERT INTO peeps VALUES " + values)


# Deal with courses
classFile = open("courses.csv", "r")
classes = csv.DictReader(classFile)
command = "CREATE TABLE courses (code STRING, mark INTEGER, id INTEGER);"
c.execute(command) #create table
for row in classes:
    values = '("' + row['code'] + '", ' + row['mark'] + ', ' + row['id'] + ');'
    c.execute("INSERT INTO courses VALUES " + values)


#==========================================================
db.commit() #save changes
db.close()  #close database
peepsFile.close() #close file
classFile.close() #close file


