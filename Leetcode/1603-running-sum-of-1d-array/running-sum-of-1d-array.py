class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        prev=0
        for i in nums:
            prev=prev+i
            a.append(prev)
        return a