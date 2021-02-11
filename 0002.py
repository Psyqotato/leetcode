# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum, k = 0, 1
        while l1 != None or l2 != None:
            if l1 != None:
                sum = sum + l1.val * k
                l1 = l1.next
            if l2 != None:
                sum = sum + l2.val * k
                l2 = l2.next
            k = k * 10
        p = ListNode(sum%10)
        l3 = p
        sum = sum // 10
        while sum != 0:
            p.next = ListNode(sum%10)
            p = p.next
            sum = sum // 10
        return l3