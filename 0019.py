# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        global num
        num = 0
        def find(node):
            global num
            if node.next != None:
                node.next = find(node.next)
            num = num + 1
            if num == n:
                return node.next
            else:return node
        return find(head)