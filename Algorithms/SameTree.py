"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def compare(p,q):
            if p == None and q == None:
                return True
            elif p and q and p.val == q.val:
                return True and compare(p.left,q.left) and compare(p.right,q.right)
            else:
                return False
        return compare(q,p)
            
                
