'''
Yahoo, Google, Facebook
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

'''

'''
LIFO Stack: list.append(), list.pop()
FIFO Queue: from collections import deque; deque.append(), deque.popleft()
'''
class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        operators = ['+', '-', '*', '/']
        stack = []

        for i in range(0, len(A)):

            if A[i] in operators:
                el1 = int(stack.pop())
                el2 = int(stack.pop())
                if A[i] == '+':
                    val = el2 + el1
                elif A[i] == '-':
                    val = el2 - el1
                elif A[i] == '*':
                    val = el2 * el1
                elif A[i] == '/':
                    val = el2 / el1
                stack.append(val)
            else:
                stack.append(A[i])

        val = stack.pop()
        return val

def test_evalRPN():
    s = Solution()
    assert (Solution.evalRPN(s, ["2", "1", "+", "3", "*"]) == 9)
    assert (Solution.evalRPN(s, ["4", "13", "5", "/", "+"]) == 6)


if __name__ == "__main__":
    test_evalRPN()
