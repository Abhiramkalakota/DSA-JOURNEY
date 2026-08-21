class Solution(object):
    def isPalindrome(self, x):
        num=x
        prev=num
        rev=0
        while(num>0):
            lastdigit=num%10
            rev=(rev*10)+lastdigit
            num//=10
        if(prev<0):
            return False
        elif(prev==rev):
            return True
        else :
            return False