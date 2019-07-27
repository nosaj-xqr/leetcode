# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = head
        while True:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
            if p.next == None:
                break
        return head
