class Solution(object):
    def canAliceWin(self, n):
        i = 10
        alice = True

        while n >= i:
            n -= i
            i -= 1
            alice = not alice

        return not alice