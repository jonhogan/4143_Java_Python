'''
Author      Jonathan Hogan
Class       Dr.Das - CMPS 4143 Contemporary Programming Languages
Due         11/24/21

(30 points) Given the expression as strs str, find the duplicate parenthesis from the
expression. Your program will output whether or not finding the duplicates, that is true of
false

'''


def paren_dupes(strs):
 
    #Create a stack for chars
    charstack = []
 
    #Read through the string
    for chars in strs:
     
        #Check for a close paren
        if chars == ')':
            top = charstack.pop()
            parens = 0

            while top != '(':
                parens += 1
                top = charstack.pop()

            #If dupes are found 
            if parens < 1:
                return True

        else:
            charstack.append(chars)
     
    #If no dupes are found
    return False
 

 
validFile = False
#Loop to get a file name from the users, and verify that a valid file was entered
while validFile == False:
  fileOpen = True
  try:
    inFile = open(input('Enter the name of the file you want to open: '))
  
  #Invalid file name check
  except FileNotFoundError:
    print('Invalid file name. Please check the name and path of the file you are trying to read from.')
    print('Default file name is input.dat')
    #Flag to run the if statement to flip the validFile bool and exit the loop
    fileOpen = False
  if fileOpen:
    validFile = True

for line in inFile: #read line 
    strs = line
 
    print(paren_dupes(strs))