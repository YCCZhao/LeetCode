# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next=head
        prev = dummy
        while prev.next and prev.next.next:
            a=prev.next
            b=a.next
            bnext = b.next
            
            prev.next=b
            b.next=a
            a.next=bnext
            
            prev = a
            
        return dummy.next
