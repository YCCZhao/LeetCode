"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n:
            return head
        else: 
            preNode = ListNode(0)
            preNode.next = head
            left = preNode
            for i in range(m-1):
                left = left.next
            Rtail = left.next #2
            
            current = left.next 
            prev = None

            for i in range(m,n+1):
                next = current.next #3 4 5 
                current.next = prev #None 2 3
                prev = current #2 3 4
                current = next #3 4 5
            Rtail.next = current
            left.next = prev
            return preNode.next

                

                
