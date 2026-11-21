class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        count=0
        max1=0
        a=prices[0]
        for i in prices[1::]:
            if i<a:
                a=i
            elif a<i:
                max1=max(max1,i-a)
        return max1
            
        