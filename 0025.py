# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        nums = 0
        temp1 = head
        while temp1:
            nums = nums + 1
            temp1 = temp1.next
        cur = ListNode(0)
        l3 = nodes = cur
        l3.next = head
        for i in range(1,nums - k + 2):
            if i % k == 1:   
                for x in range(1,k):
                    temp = nodes.next
                    cur = nodes
                    for y in range(1,k-x+1):
                        a, b = temp, temp.next
                        a.next, b.next = b.next, a
                        cur.next = b
                        cur = cur.next
            cur, nodes = cur.next, nodes.next
        return l3.next