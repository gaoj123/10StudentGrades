import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


def insertCSV(cursor):
    # Deal with students
    peepsFile = open("peeps.csv", "r")
    students = csv.DictReader(peepsFile)
    command = "CREATE TABLE peeps (id INTEGER PRIMARY KEY, name STRING, age INTEGER);"
    cursor.execute(command)
    for row in students:
        values = '(' + row['id'] + ', "' + row['name'] + '", ' + row['age'] + ');'
        cursor.execute("INSERT INTO peeps VALUES " + values)
    # Deal with courses
    classFile = open("courses.csv", "r")
    classes = csv.DictReader(classFile)
    command = "CREATE TABLE courses (code STRING, mark INTEGER, id INTEGER);"
    cursor.execute(command) #create table
    for row in classes:
        values = '("' + row['code'] + '", ' + row['mark'] + ', ' + row['id'] + ');'
        cursor.execute("INSERT INTO courses VALUES " + values)
    peepsFile.close() #close file
    classFile.close() #close file


