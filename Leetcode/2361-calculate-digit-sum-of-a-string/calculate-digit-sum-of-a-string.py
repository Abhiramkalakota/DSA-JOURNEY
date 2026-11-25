class Solution(object):
    def digitSum(self, s, k):
        while len(s) > k:
            ans = ""
            for i in range(0, len(s), k):
                total = 0
                for j in range(i, min(i + k, len(s))):
                    total += int(s[j])
                ans += str(total)
            s = ans
        return s
        