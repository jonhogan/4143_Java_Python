'''
Author      Jonathan Hogan
Class       Dr.Das - CMPS 4143 Contemporary Programming Languages
Due         11/24/21

(35 points) A stack data structure has following functionalities like empty(), size(), top(),
push() and pop(). See the lecture slides for the details (how it works, complexity, etc.) I
have shown you in the class how to implement a stack using a list data structure. You
need to implement the stack with Linkedlist data structure in python. Implement the
stack means, all of the stack functionalities including the construction of stacks should
present on your code.
'''
#Bool flag, used globally
flag = False


class Node: #Defining the node structure for a linked list
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack: #Defining the stack structure/class
    
    #Constructor for the stack
    def __init__(self): 
        self.top = None
        self.size = 0

    def push(self, data):
        '''
        Create and add a new node for data being pushed to
        the stack
        '''
        temp = Node(data)

        #Set the new Node as the top of the stack
        if self.top is None:
            self.top = temp
            self.size = self.size + 1
        else:
            temp.next = self.top
            self.top = temp
            self.size = self.size + 1

    def pop(self):
        #Removes the top element from the stack
        try:
            if self.top is None:
                raise Exception("Error: Stack is Empty")
            else:
                temp = self.top
                self.top = self.top.next
                tempdata = temp.data
                self.size = self.size - 1
                del temp
                return tempdata
        except Exception as error:
            print(str(error))

    def get_top(self):
        #Removes the top element from the stack
        try:
            if self.top is None:
                raise Exception("Error: Stack is Empty")
            else:
                return self.top.data
        except Exception as error:
            print(str(error))

    def get_size(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
    
#User menu
def menu():
    print('1. Add an item to the stack\n2. Remove the top element')
    print('3. Get the size of the stack\n4. Check if the stack is empty')
    print('5. Check the top of the stack\n6. Exit')

    flag = False
    while flag == False:
        selection = input('Please enter the number of your selection: ')

        if selection.isnumeric() == False: #Error checking for selection, should be numeric only
            print('Your selection should only contain numeric characters')
        else:
            selection = int(selection)
            flag = True
        
    return selection


flag = True
stack = Stack()

while flag == True:
    
    option = menu()

    if option == 1:
        data = input('Enter the data to add to the stack: ')
        print()
            
        if data.isnumeric() == True:
            data = int(data)
        
        stack.push(data)
        
    elif option == 2:
        print('You popped', stack.pop(), 'from the stack\n' )

    elif option == 3:
        print('The stack has', stack.get_size(), 'elements\n')

    elif option == 4:
        if stack.is_empty():
            print('The stack is empty\n')

        else:
            print('The stack is not empty\n')

    elif option == 5:
        print('The top element is:', stack.get_top(),'\n')
        
    elif option == 6:
        print('Goodbye')
        flag = False

    else:
        print('Invalid selection\n')