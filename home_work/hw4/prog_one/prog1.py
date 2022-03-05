'''
Author      Jonathan Hogan
Class       Dr.Das - CMPS 4143 Contemporary Programming Languages
Due         11/10/21                                                   
 
Program for Question 1: (35 points) Write a Python program using file operation.  You will open an input file 
“students.dat” that will contain a list of student names, classification, and grade in the 
class. (All student info is completely made up) You should read through the entire input 
file.  After reading in all information, do operations (No built-in functions like Average, 
min, max, count, etc.), close the input file and write that following information with 
labels to an output file “student_statistics.txt” 
    • Highest grade in the class 
    • Lowest grade in the class 
    • Class average grade (rounded to one decimal place) 
    • Number of freshmen students 
    • Number of sophomore students 
    • Number of junior students 
    • Number of senior students

input file: Students.dat
'''

highGrade = -1      #Sentinal value, as, in theory, you shouldn't be able to score lower than 0 on a grade
lowGrade = 999      #High sentinal value, you may be able to score better than 100 with extra credit
gradeSum = 0
gradeCount = 0
freshman = 0
sophomore = 0
junior = 0
senior = 0

validFile = False
#Loop to get a file name from the users, and verify that a valid file was entered
while validFile == False:
  fileOpen = True
  try:
    inFile = open(input('Enter the name of the file you want to open: '))
  
  #Invalid file name check
  except FileNotFoundError:
    print('Invalid file name. Please check the name and path of the file you are trying to read from.')
    print('Default file name is Students.dat')
    #Flag to run the if statement to flip the validFile bool and exit the loop
    fileOpen = False
  if fileOpen:
    validFile = True


#read each line in the file
for line in inFile: #read line 
        
  lineList = line.split()
  #Read in each line
  firstName = lineList[0]
  lastName = lineList[1]
  year = lineList[2]
  gradeCount += 1
        
  grade = int(lineList[3])
  gradeSum += grade
  if grade > highGrade:
    highGrade = grade
    highGradeFirstName = firstName
    highGradeLastName = lastName
    highGradeYear = year

  elif grade < lowGrade:
    lowGrade = grade
    lowGradeFirstName = firstName
    lowGradeLastName = lastName
    lowGradeYear = year

  if year.lower() == 'freshman':
    freshman += 1
  elif year.lower() == 'sophomore':
    sophomore += 1
  elif year.lower() == 'junior':
    junior += 1
  elif year.lower() == 'senior':
    senior += 1

#Create the output file
outFile = open("OutFile.txt", "w")

#Start writing to the output file
outFile.write('From the input file we see:\n\nHighest grade was: ')
outFile.write(highGradeFirstName + ' ' + highGradeLastName +' a ' + highGradeYear + ' with a grade of ' + str(highGrade))
outFile.write('\nLowest grade was: ')
outFile.write(lowGradeFirstName + ' ' + lowGradeLastName + ' a ' + lowGradeYear + ' with a grade of '+ str(lowGrade))

outFile.write('\nAverage grade is: %.1f'%(gradeSum/gradeCount))
outFile.write('\n_________________________________________________\n')
#Print the number of students by year
outFile.write('\nTotal Freshmen  :\t' + str(freshman))
outFile.write('\nTotal Sophomores:\t' + str(sophomore))
outFile.write('\nTotal Juniors   :\t' + str(junior))
outFile.write('\nTotal Seniors   :\t' + str(senior))

inFile.close()
outFile.close()