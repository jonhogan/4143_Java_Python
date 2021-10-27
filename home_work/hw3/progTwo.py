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

#Prompt user for number of people to add
peopleCount=int(input('How many people to enter? '))
firstName = []
lastName = []
occupation = []
address = []
age = []
j = 1
#Loop to add all the people
while i < peopleCount:
    
    #Set the initial Bool value
    isValid = False
    while(not isValid):
        
        #Gets the first name
        if (j == 1 and peopleCount > 1):
           fname = input('What is the first person\'s first name? ')
           j += 1

        elif (peopleCount == 1):
            fname = input('What is the person\'s first name? ')

        elif (j == 2):
            fname = input('What is the second person\'s first name? ')
            j += 1

        elif (j == 3):
            fname = input('What is the third person\'s first name? ')
            j += 1

        else:
            fname = input('What is the ' +str(j)+'th person\'s first name? ')
            j += 1

        for idx in range(len(fname)):
            # Error check to ensure the name is alpha only
            #Prints a message and lets the user re-enter the name 
            if (fname[idx].isnumeric() == True):
                print('Invalid Input: Alpha charaters only')
                break
            elif (idx == len(fname) - 1):
                isValid = True
                firstName.append(fname)
    
    #Reset the initial Bool value
    isValid = False
    while(not isValid):
        
        #Gets the last name
        if (j == 1 and peopleCount > 1):
           lname = input('What is the first person\'s last name? ')

        elif (peopleCount == 1):
            lname = input('What is the person\'s last name? ')

        elif (j == 2):
            lname = input('What is the second person\'s last name? ')
     
        elif (j == 3):
            lname = input('What is the third person\'s last name? ')
       
        else:
            lname = input('What is the ' +str(j)+'th person\'s last name? ')
        

        for idx in range(len(lname)):
            # Error check to ensure the name is alpha only
            #Prints a message and lets the user re-enter the name 
            if (lname[idx].isnumeric() == True):
                print('Invalid Input: Alpha charaters only')
                break

            elif (idx == len(lname) - 1):
                isValid = True
                lastName.append(lname)

    #Reset the initial Bool value
    isValid = False
    while(not isValid):

        #Gets the age
        if (j == 1 and peopleCount > 1):
            getAge = input('What is the first person\'s age? ')

        elif (peopleCount == 1):
            getAge = input('What is the person\'s age? ')

        elif (j == 2):
            getAge = input('What is the second person\'s age? ')
     
        elif (j == 3):
            getAge = input('What is the third person\'s age? ')
       
        else:
            getAge = input('What is the ' +str(j)+'th person\'s age? ')
        

        for idx in range(len(getAge)):
            # Error check to ensure the age is numeric only
            #Prints a message and lets the user re-enter the age 
            if (getAge[idx].isnumeric() == False):
                print('Invalid Input: Numeric charaters only')
                break
            if (int(getAge) < 0 or int(getAge) > 150):
                print('Invalid input: Age should be between 0 and 150')

            elif (idx == len(getAge) - 1):
                isValid = True
                age.append(getAge)

    #Reset the initial Bool value
    isValid = False
    while(not isValid):
        
        #Gets the occupation name
        if (j == 1 and peopleCount > 1):
           getJob = input('What is the first person\'s occupation? ')

        elif (peopleCount == 1):
            getJob = input('What is the person\'s occupation? ')

        elif (j == 2):
            getJob = input('What is the second person\'s occupation? ')
     
        elif (j == 3):
            getJob = input('What is the third person\'s occupation? ')
       
        else:
            getJob = input('What is the ' +str(j)+'th person\'s occupation? ')
        

        for idx in range(len(getJob)):
            # Error check to ensure the occupation is alpha only
            #Prints a message and lets the user re-enter the job 
            if (getJob[idx].isnumeric() == True):
                print('Invalid Input: Alpha charaters only')
                break

            elif (idx == len(getJob) - 1):
                isValid = True
                occupation.append(getJob)

    #Reset the initial Bool value
    isValid = False
    while(not isValid):
        
        #Gets the street number
        if (j == 1 and peopleCount > 1):
           strtNum = input('What is the first person\'s street number? ')

        elif (peopleCount == 1):
            strtNum = input('What is the person\'s street number? ')

        elif (j == 2):
            strtNum = input('What is the second person\'s street number? ')
     
        elif (j == 3):
            strtNum = input('What is the third person\'s street number? ')
       
        else:
            strtNum = input('What is the ' +str(j)+'th person\'s street number? ')
        

        for idx in range(len(strtNum)):
            # Error check to ensure the number is numeric only
            #Prints a message and lets the user re-enter the street number 
            if (strtNum[idx].isnumeric() == False):
                print('Invalid Input: Numeric charaters only')
                break

            elif (idx == len(strtNum) - 1):
                isValid = True

    
        
    #Gets the street name
    if (j == 1 and peopleCount > 1):
           strtName = input('What is the first person\'s street name? ')

    elif (peopleCount == 1):
        strtName = input('What is the person\'s street name? ')

    elif (j == 2):
        strtName = input('What is the second person\'s street name? ')
     
    elif (j == 3):
        strtName = input('What is the third person\'s street name? ')
       
    else:
        strtName = input('What is the ' +str(j)+'th person\'s street name? ')
        
        #Alpha numeric error checking does't work for a street name, as some streets
        #consist of alpha/numeric names such as E 5th Street
    '''
        for idx in range(len(strtName)):
            # Error check to ensure the Street Name is alpha only
            #Prints a message and lets the user re-enter the name 
            if (strtName[idx].isnumeric() == True):
                print('Invalid Input: Alpha charaters only')
                break
            elif (idx == len(strtName) - 1):
               isValid = True
    '''
    #Reset the initial Bool value
    isValid = False
    while(not isValid):
        
        #Gets the city name
        if (j == 1 and peopleCount > 1):
           cityName = input('What is the first person\'s city\'s name? ')

        elif (peopleCount == 1):
            cityName = input('What is the person\'s city\'s name? ')

        elif (j == 2):
            cityName = input('What is the second person\'s city\'s name? ')
     
        elif (j == 3):
            cityName = input('What is the third person\'s city\'s name? ')
       
        else:
            cityName = input('What is the ' +str(j)+'th person\'s city\'s name? ')
        

        for idx in range(len(cityName)):
            # Error check to ensure the Street Name is alpha only
            #Prints a message and lets the user re-enter the name 
            if (cityName[idx].isnumeric() == True):
                print('Invalid Input: Alpha charaters only')
                break
            elif (idx == len(cityName) - 1):
                isValid = True

    #Reset the initial Bool value
    isValid = False
    while(not isValid):
        
        #Gets the State name
        if (j == 1 and peopleCount > 1):
           stateName = input('What is the first person\'s state\'s name abbreviation? ')

        elif (peopleCount == 1):
            stateName = input('What is the person\'s state\'s name abbreviation? ')

        elif (j == 2):
            stateName = input('What is the second person\'s state\'s name abbreviation? ')
     
        elif (j == 3):
            stateName = input('What is the third person\'s state\'s name abbreviation? ')
       
        else:
            stateName = input('What is the ' +str(j)+'th person\'s state\'s name abbreviation? ')
        

        for idx in range(len(stateName)):
            # Error check to ensure the Street Name is alpha only
            #Prints a message and lets the user re-enter the name 
            if (stateName[idx].isnumeric() == True or len(stateName) > 2):
                print('Invalid Input: The abbreviation should be alpha character and consist of two letters only')
                print('For example, Texas should be entered as "TX"')
                break
            elif (idx == len(stateName) - 1):
                isValid = True

    #Reset the initial Bool value
    isValid = False
    while(not isValid):
        
        #Gets the zip code
        if (j == 1 and peopleCount > 1):
           zipCode = input('What is the first person\'s zip code? ')

        elif (peopleCount == 1):
            zipCode = input('What is the person\'s zip code? ')

        elif (j == 2):
            zipCode = input('What is the second person\'s zip code? ')
     
        elif (j == 3):
            zipCode = input('What is the third person\'s zip code? ')
       
        else:
            zipCode = input('What is the ' +str(j)+'th person\'s zip code? ')
        

        for idx in range(len(zipCode)):
            # Error check to ensure the Street Name is alpha only
            #Prints a message and lets the user re-enter the name 
            if (zipCode[idx].isnumeric() == True or len(zipCode) > 2 or len(zipCode) < 5):
                print('Invalid Input: Zip code should consist of five numbers only')
                break
            elif (idx == len(stateName) - 1):
                address.append(strtNum + ' ' + strtName + ', ' + cityName + ', ' + stateName.upper() + ', ' + zipCode + '.')
                isValid = True
                    
        
    k = 0
    while k < peopleCount:
        print(firstName[k], ' ', lastName[k], 'aged', age[k], 'years, works as a', occupation[k], 'lives at', address[k])
    i += 1 
   