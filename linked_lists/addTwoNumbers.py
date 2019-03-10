'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.


Gotchas :
1) What if one list if shorter than the other ? 1->2 + 2->3->4->5
2) What if the answer has more digits ? 1 + 9

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        carr = 0
        dummy = ListNode(0)
        curr = dummy
        while A or B:
            valA = 0
            valB = 0
            if A != None:
                valA = A.val
            if B != None:
                valB = B.val
            value = (valA + valB + carr) % 10
            carr = (valA + valB + carr) // 10  # 5 // 10 = 0 vs. 5 / 10 = 0.5
            curr.next = ListNode(value)
            curr = curr.next
            if A != None:
                A = A.next
            else:
                A = None
            if B != None:
                B = B.next
            else:
                B = None
        if carr != 0:
            curr.next = ListNode(carr)

        return dummy.next


def test_addTwoNumbers():
    s = Solution()
    # assert (Solution.addTwoNumbers(s, [3, 2, 4, 3], [3, 5, 6, 4]) == [3, 7, 0, 8])


if __name__ == "__main__":
    test_addTwoNumbers()
