class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left=0
        right=0
        sum1=0
        max1=float('-inf')
        while right<len(nums):
            sum1+=nums[right]
            if right-left+1==k:
                if max1<sum1:
                    max1=sum1
                sum1-=nums[left]
                left+=1
            right+=1
        return float(max1)/k