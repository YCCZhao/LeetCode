"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        index = []
        self.num = 0
        self.s = s
        n = len(self.s)
        for i in range(n):
            if self.s[i] =='(':
                stack.append([s[i],i])
            elif self.s[i] ==')' and len(stack) > 0:
                stack.pop()
            else:
                index.append(i)
                
        for list in stack:
            index.append(list[1])
        index.sort()
        index.append(n)
        self.num = 0       
        head = 0
        for i in index:
            length = i - head
            head = i+1
            if length > self.num:
                self.num = length
        return self.num
        
