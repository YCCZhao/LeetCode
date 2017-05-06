"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        S={}
        T={}
        for i in s:
            S[i] = S.get(i,0) +1
        for i in t:
            T[i] = T.get(i,0) +1
        return S==T
            
