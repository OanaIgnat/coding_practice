from collections import deque


# Python program for implementation of stack 
# import maxsize from sys module  
# Used to return -infinite when stack is empty 
from sys import maxsize 
  
# Function to create a stack. It initializes size of stack as 0 
def createStack(): 
    stack = [] 
    return stack 
  
# Stack is empty when stack size is 0 
def isEmpty(stack): 
    return len(stack) == 0
  
# Function to add an item to stack. It increases size by 1 
def push(stack, item): 
    stack.append(item) 
    print(item + " pushed to stack ") 
      
# Function to remove an item from stack. It decreases size by 1 
def pop(stack): 
    if isEmpty(stack):
        return str(-maxsize -1) # return minus infinite 
      
    return stack.pop() 
  
# Function to return the top from stack without removing it 
def peek(stack): 
    if isEmpty(stack):
        return str(-maxsize -1) # return minus infinite 
    return stack[len(stack) - 1] 
  
# Driver program to test above functions     
stack = createStack() 
push(stack, str(10)) 
push(stack, str(20)) 
push(stack, str(30)) 
print(pop(stack) + " popped from stack") 


# reverse a string without stack
# Function to reverse a string
def reverse(string):
    string = string[::-1]
    return string

def is_palindrome(input):
    input = str(input)
    input_reverse = input[::-1]
    if input == input_reverse:
        print(input + " is palindrome")
    else:
        print(input + " is not palindrome")

def stack_as_dequeue():
    stack = deque()

    stack.append(1)
    stack.append(2)
    stack.append(3)

    print(stack)

    print("Elements popped from stack: ")
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


def stack_as_list():
    l = []

    l.append(1)
    l.append(2)
    l.append(3)

    print(l)

    print("Elements popped from stack: ")
    print(l.pop())
    print(l.pop())
    print(l.pop())


def main():
    stack_as_list()
    # stack_as_dequeue()



if __name__ == "__main__":
    main()
