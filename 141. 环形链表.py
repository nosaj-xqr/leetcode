# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
思路1：哈希表
给每一个值都标记键值为空，如果能再次找到此键值，表明为环形，否则不为环形
'''
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        while head.next and head.val != None:
            head.val=None
            head = head.next
        if not head.next:
            return False
        return True
        
'''
思路2：快慢指针
设定两个指针，一个走的慢，一个走的快，入为环形，两指针必定相遇
'''
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
