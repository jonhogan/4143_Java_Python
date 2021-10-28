'''
Author      Jonathan Hogan
Class       Dr.Das - CMPS 4143 Contemporary Programming Languages
Due         10/27/21                                                   
 
Program for Question 3:

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed
integer (similar to C/C++'s atoi function). (40 points)

The algorithm for myAtoi(string s) is as follows:
    a) Read in and ignore any leading whitespace.

    b) Check if the next character (if not already at the end of the string) is '-'
       or '+'. Read this character in if it is either. This determines if the final
       result is negative or positive respectively. Assume the result is positive if
       neither is present.

    c) Read in next the characters until the next non-digit character or the end
       of the input is reached. The rest of the string is ignored.

    d) Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If
       no digits were read, then the integer is 0. Change the sign as necessary
       (from step 2).

    e) If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then
       clamp the integer so that it remains in the range. Specifically, integers less
       than -231 should be clamped to -231, and integers greater than 231 - 1 should
       be clamped to 231 - 1.

    f) Return the integer as the final result.

Note:
 Only the space character ' ' is considered a whitespace character.

 Do not ignore any characters other than the leading whitespace or the rest of the
 string after the digits.
'''

def myStoi(s):
   isNeg = False
   numAdded = False
   s = s.strip()
   
   if s[0] == '-':
       isNeg = True

   number = ''

   for idx in range(len(s)):
       if (s[idx].isnumeric() == True):
           number += s[idx]
           numAdded = True
           if(s[idx-1].isnumeric() == True and s[idx].isnumeric() == False):
              break

   number = int(number)

   if isNeg: #Return a negative value
      number = (-1) * number

   if number < -(2**31): #Keep the int value within the min int size
      print("That number was too small and will be clamped to the min int size.")
      return str(-(2**31))
   elif number > (2**31 - 1): #Keep the int value within the max int size
      print("That number was too large and will be clamped to the max int size.")
      return str(2**31-1)
   elif numAdded:
      return str(number)
   else:
      return '0'


loopAgain = True

while loopAgain:
   
   numString = input('Please enter a string: ')

   convertedNum = myStoi(numString)

   print('The number in that string is ' + convertedNum)

   answer = input('Enter another? Yes/No: ')

   answer = answer.lower()
   
   invalidAnswer = True
   while invalidAnswer:
      if answer == 'yes':
         invalidAnswer = False
      elif answer == 'no':
         invalidAnswer = False
         print("Good day.\n\n\n\n\n\n\nI said good day!")
         loopAgain = False
      else:
         print("Invalid response: Yes or No")