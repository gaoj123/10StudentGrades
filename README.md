# 10StudentGrades
Work 10: Selecting Success<br>
This is a programming interface to the student gradebook database built in the last assignment.

## Documentation

+ `getGradesFor(studentID)`<br>
       Returns a list of numbers, representing all the grades that the student specified earned. `StudentID` should be a number.
+ `computeAverageFor(studentID)`<br>
       Returns a number representing the average of all the grades earned by the specified student given his/her `ID`.
+ `getAllAverages()`<br>
       Returns a list of dictionaries, one for each student. Each dictionary has a student's name, id, and average under those keys.
+ `createGradebook()`<br>
       Creates a table in the database to be used for storing averages for the very first time. Do not call more than once.
+ `updateAverages()`<br>
       Updates the averages in the database table named "peeps_avg."
+ `addGradeFor(studentID, courseName, grade)`<br>
       Adds a record to the database table named "classes." The `studentID` should be a number, `courseName` should be a string, and `grade` should be a number.
