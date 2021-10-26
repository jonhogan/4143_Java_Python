i = 0  #Counter
isInvalid = True

#Prompt user for number of people to add
peopleCount=int(input("How many people to enter?"))

#Loop to add all the people
while i < peopleCount:


    #Input information about people
    while(isInvalid):
        j = 1
        try:
            if (j == 1 & peopleCount > 1):
                firstName=str(input("What is the first person's first name?"))
                j += 1
            elif (peopleCount == 1):
                firstName=str(input("What is the person's first name?"))
            elif (j == 2):
                firstName=str(input("What is the second person's first name?"))
                j += 1

        except:
            raise ValueError('Invalid Name: Please enter a valid first name')
        if firstName.isnumeric(): #check if the name is entered as a number
            ErrorWarning= ValueError("Invalid input, insert correct First Name using non numeric values")
            print(ErrorWarning)
        else: #else if the occupation is correct
            break
        
    while(True):
        try:
            LastName=str(input("What is the persons last  name?"))# user prompt
        except:
            raise ValueError('Last Name  is not valid')
        if LastName.isnumeric(): #chek if occupation contains only numeric value or not
            ErrorWarning= ValueError("Invalid input, insert correct Last Name using non numeric values")
            print(ErrorWarning)
        else: #else if the occupation is correct
            break
    

    # start try catch block that will catch invalid data  whcih consists of nums between 0 and 150
    
    while True:
        try:
            Age= int((input(" Enter the person Age(must be less than 150).  ")))
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
            Occupation= str(input("What is their occupation?"))# prompt the user
        except:
            raise ValueError('Occupation is not valid')# if invalid say invalid
        if Occupation.isnumeric(): #chek if occupation contains only numeric value or not
            ErrorWarning= ValueError("Invalid input, insert correct occupation using non numeric values")
            print(ErrorWarning)# printing the error warning
        else: #else if the occupation is correct
            break
    
    # try catch me to get valid address
    while(True):
        try:
            Address=str(input(" What is this persons Address?"))
        except:
            raise ValueError('address  is not valid')
        if Address.isnumeric(): #chek if address contains only numeric value or not
            ErrorWarning= ValueError("address was invalid")
            print(ErrorWarning)
        else: #else if the occupation is correct
            break

    # format the output for each individual person to be this  formatted
    print(FirstName, LastName, " aged", Age," years, worked as a ",Occupation,
             " and currently lives at ",Address,".\n")
    i+=1# increment the ocunter variable go back to loop begining until satisfied
# end of the program exitting out