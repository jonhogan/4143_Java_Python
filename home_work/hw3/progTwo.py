'''
Author      Jonathan Hogan
Class       Dr.Das - CMPS 4143 Contemporary Programming Languages
Due         10/27/21                                                   
 
Program for Question 2: Write a program where it asks to enter
the number of people, then based on this number iterate that amount
of time where each time get single person’s information like First
Name, Last Name, Age, Occupation and Address. Make sure you validate
all users’ input. Included but not limited to like age cannot be a
non-numeric value should be between 0-150, name can only be non-numeric.
You need to think how you can validate the occupation and address field.
Finally show (print) user details one by one. For your input validation,
make sure you can’t proceed next step/value without inserting valid
input on current phase. (35 points)
'''


i = 0  #Counter
isInvalid = True

#Prompt user for number of people to add
peopleCount=int(input('How many people to enter? '))

#Loop to add all the people
while i < peopleCount:


    #Input information about people
    while(isInvalid):
        j = 1
        if (j == 1 and peopleCount > 1):
           firstName=str(input('What is the first person\'s first name?'))
           j += 1
        elif (peopleCount == 1):
            firstName=str(input('What is the person\'s first name?'))
        elif (j == 2):
            firstName=str(input('What is the second person\'s first name?'))
            j += 1
        elif (j == 3):
            firstName=str(input('What is the third person\'s first name?'))
            j += 1
        else:
            firstName=str(input('What is the ' +str(j)+'th person\'s first name?'))
            j += 1

        for idx in range(len(firstName)):
            if (firstName[idx].isnumeric == False):
                print('Invalid Input: Alpha charaters only')

        '''
        except:
            raise nameError('Invalid Name: Please enter a valid first name')
        if firstName.isnumeric(): #check if the name is entered as a number
            ErrorWarning= nameError('Invalid Input: Alpha characters only')
            print(ErrorWarning)
        else: 
            isInvalid = False
        '''
        
    while(True):
        try:
            LastName=str(input('What is the persons last  name?'))# user prompt
        except:
            raise ValueError('Last Name  is not valid')
        if LastName.isnumeric(): #chek if occupation contains only numeric value or not
            ErrorWarning= ValueError('Invalid input, insert correct Last Name using non numeric values')
            print(ErrorWarning)
        else: #else if the occupation is correct
            break
    

    # start try catch block that will catch invalid data  whcih consists of nums between 0 and 150
    
    while True:
        try:
            Age= int((input(' Enter the person Age(must be less than 150).  ')))
        except ValueError:
           raise ValueError('Age Entered Was Not Valid')
        if Age > 150 or Age<0:# age must be between 0 and 150 anything else is error
            ErrorMessage = ValueError('Age Must Be less that 150 and larger than 0.')
            print(ErrorMessage)
        else:
            break # once the input is valid, break through the while loop

    # try catch to read in valid non numeric occupation
    while(True):
        try:
            Occupation= str(input('What is their occupation?'))# prompt the user
        except:
            raise ValueError('Occupation is not valid')# if invalid say invalid
        if Occupation.isnumeric(): #chek if occupation contains only numeric value or not
            ErrorWarning= ValueError('Invalid input, insert correct occupation using non numeric values')
            print(ErrorWarning)# printing the error warning
        else: #else if the occupation is correct
            break
    
    # try catch me to get valid address
    while(True):
        try:
            Address=str(input(' What is this persons Address?'))
        except:
            raise ValueError('address  is not valid')
        if Address.isnumeric(): #chek if address contains only numeric value or not
            ErrorWarning= ValueError('address was invalid')
            print(ErrorWarning)
        else: #else if the occupation is correct
            break

    # format the output for each individual person to be this  formatted
    print(FirstName, LastName, ' aged', Age,' years, worked as a ',Occupation,
             ' and currently lives at ',Address,'.\n')
    i+=1# increment the ocunter variable go back to loop begining until satisfied
# end of the program exitting out