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
        A Stack is a LIFO structure, new data will always be 
        at the top of a stack
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
                raise Exception("Empty Stack")
            else:
                temp = self.top
                self.top = self.top.next
                tempdata = temp.data
                self.size = self.size - 1
                del temp
                return tempdata
        except Exception as error:
            print(str(error))