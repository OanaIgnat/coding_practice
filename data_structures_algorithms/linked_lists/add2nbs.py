# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        c = 0
        nb1 = 0
        while l1:
            nb1 += l1.val * (10 ** c)
            c += 1
            l1 = l1.next

        c = 0
        nb2 = 0
        while l2:
            nb2 += l2.val * (10 ** c)
            c += 1
            l2 = l2.next

        nb3 = nb1 + nb2


        s = str(nb3)[::-1]
        head = prev = None
        for ch in s:
            node = ListNode(int(ch))
            if prev:
                prev.next = node
            prev = node
            if not head:
                head = prev
            print(prev.val, head.val)
        # print(head.val)
        # print(head.next.val)
        # print(head.next.next.val)
        # print(head.next.next.next)
        return head

def test_addTwoNumbers():
    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    s.addTwoNumbers(l1, l2)


if __name__ == "__main__":
    test_addTwoNumbers()