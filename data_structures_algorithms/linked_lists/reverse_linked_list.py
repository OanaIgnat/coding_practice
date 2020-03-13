# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverseList(self, head):  # Iterative
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

    # https://www.youtube.com/watch?v=njTh_OwMljA
    def recursive_reverseList(self, head):
        if not head or not head.next:
            return head
        p = self.recursive_reverseList(head.next)
        head.next.next = head  # 3-> 4 becomes 4 ->3
        head.next = None  # remove previous link 3-> 4
        return p


def test_addTwoNumbers():
    s = Solution()
    s.merge_sorted_lists(l1=[1, 2, 4], l2=[1, 3, 4])


if __name__ == "__main__":
    test_addTwoNumbers()
