class Solution(object):
    def countCommas(self, n):
        res = 0
        for i in range(1, 6):
            res += max(0, n - (1000 ** i) + 1)
        return res