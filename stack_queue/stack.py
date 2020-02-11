from collections import deque


# def is_array_stack_permutation(input1, input2):
#     length = len(input2)
#     if input1[-1] == input2[0]:
#
#         for i in range(length-1):
#             if input1[i] != input2[length-i]:
#                 print("False")
#                 break
#         print("True")
#         return
#     else:

# def parathesis_checker(exp):


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
    # stack_as_list()
    # stack_as_dequeue()



if __name__ == "__main__":
    main()
