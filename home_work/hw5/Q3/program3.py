'''
Author      Jonathan Hogan
Class       Dr.Das - CMPS 4143 Contemporary Programming Languages
Due         11/24/21

(35 points) Write a python code to find the average from a stream. The input of this 
program will receive a stream of numbers and a window size to find the moving average 
of all the numbers in the sliding window. Write your code in OOP style and solve the 
program with queue and or stack data structure

'''

from typing import AsyncGenerator


class StackClass:
    def __init__(self):
        self.stack = []

    #Get the size of the stack
    def get_size(self):
        return len(self.stack)

    #Add data to the stack
    def push(self, data):
        self.stack.append(data)
    
    #Remove and return the top of the stack
    def pop(self):
        temp = self.stack[-1]
        self.stack.remove[-1]
        return temp

    #Return the top of the stack
    def get_top(self):
        return self.stack[-1]

    def is_empty(self):
        return (len(self.stack) == 0)
    
    def get_element(self, element):
        return self.stack[element]

    def get_avg_list(self, window):
        for ele in range(len(self.stack.get)):
            count = 0
            offset = 0
            if (ele - window) < 0:
                offset = ele
                while (offset - window) < 0:
                    offset += 1

                if (offset - window) == 0:
                    avgstack.push(mystack[0])
                else:
                    for i in range(offset-window):
                    sum += mystack[i]
                    count += 1
                avgstack.push(sum/count)
        else:
            for element in mystack[(ele - window): ele]:
                sum += element

        avgstack.push(sum/window)

        print(avgstack)

#While loop control variable
flag = False #Default value

mystack = StackClass()

#Input validation loop
#Will be plenty of these
while flag == False:
    num_count = input('How many numbers will you be entering: ')

    if num_count.isnumeric() == True:
        num_count = int(num_count)
        flag = True
    
    else:
        print('Invalid Input: Please enter a number\n\n\n')

#Reset flag
flag = False

while flag == False:
    window = input('What is the window size: ')

    if window.isnumeric() == True:
        window = int(window)
        flag = True
    
    else:
        print('Invalid Input: Please enter a number\n\n\n')

for num in range(num_count):
    flag = False

    while flag == False:
        number = input('Please enter number ' + str(num +1) +': ')

        if number.isnumeric() == True:
            number = int(number)
            mystack.push(number)
            flag = True
    
        else:
            print('Invalid Input: Please enter a number\n\n\n')
'''
avgstack = StackClass()

for ele in range(mystack.get_size()):
    count = 0
    offset = 0
    if (ele - window) < 0:
        offset = ele
        while (offset - window) < 0:
            offset += 1

        if (offset - window) == 0:
            avgstack.push(mystack[0])
        else:
            for i in range(offset-window):
                sum += mystack[i]
                count += 1
            avgstack.push(sum/count)
    else:
        for element in mystack[(ele - window): ele]:
            sum += element

        avgstack.push(sum/window)

print(avgstack)
'''