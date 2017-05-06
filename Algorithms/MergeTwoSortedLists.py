"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(0)
        cur1=l1
        cur2=l2
        pre = dummy
        if not cur1 and not cur2:
            []
        while cur1 != None or cur2 != None:
            if cur1 == None:
                pre.next=cur2
                return dummy.next
            elif cur2 == None:
                pre.next=cur1
                return dummy.next
            elif cur1.val < cur2.val:
                pre.next = cur1
                pre=cur1
                cur1 = cur1.next
            else:
                pre.next=cur2
                pre=cur2
                cur2 = cur2.next
        return dummy.next
            
