class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        low=0
        high=len(s)-1
        while(low<high):
            if(not s[low].isalnum()):
                low+=1
            elif(not s[high].isalnum()):
                high-=1
            elif(s[low]==s[high]):
                low+=1
                high-=1
            else:
                return False
        return True

            
        