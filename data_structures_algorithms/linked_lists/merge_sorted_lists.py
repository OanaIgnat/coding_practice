# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeTwoLists_recursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        else:
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2

    def mergeTwoLists_iterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)
        prev = prehead
        while l1 and l2:
            if l1.val > l2.val:
                prev.next = l2
                l2 = l2.next
            else:
                prev.next = l1
                l1 = l1.next
            prev = prev.next

        prev.next = l1 if l1 is not None else l2

        return prehead.next



if __name__ == "__main__":
    s = Solution()
    s.mergeTwoLists_iterative(l1=[1, 2, 4], l2=[1, 3, 4])