class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums))

        i = 1
        for num in nums:
            if num == i:
                i += 1
        return i