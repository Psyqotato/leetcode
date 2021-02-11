# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:return None
        if head.next == None:return head
        nums = 0
        temp1 = head
        while temp1:
            nums = nums + 1
            temp1 = temp1.next
        cur = ListNode(0)
        l3 = cur
        l3.next = head
        for i in range(1,nums):
            if i % 2 == 1:   
                temp = cur.next
                a, b = temp, temp.next
                a.next, b.next = b.next, a
                cur.next = b
            cur = cur.next
        return l3.next