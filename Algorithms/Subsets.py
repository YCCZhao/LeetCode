"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        import copy
        rlist = []
        for i in nums:
            rlist.append([i])
        temp = copy.copy(rlist)
        for i in range(len(nums)-1):
            nextlevel=[]
            for j in temp:           
                for k in [x for x in nums if x > max(j)]:
                    a=copy.copy(j)
                    a.append(k)
                    nextlevel.append(a)
                    rlist.append(a)
            temp = nextlevel
        rlist.append([])
            
        return rlist
