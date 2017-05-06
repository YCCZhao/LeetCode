"""
Given a digit string, return all possible letter combinations that the number could represent.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        index = {"2":'abc', "3": 'def',"4": 'ghi',"5": 'jkl',"6": 'mno',"7": 'pqrs',"8": 'tuv',"9": 'wxyz'}
        ret = [""]
        for x in digits:
            temp = []
            for y in ret:
                for key in index[x]:
                    temp.append(y + key)
            ret = temp
        return ret
