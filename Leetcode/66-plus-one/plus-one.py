class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1]!=9:
            digits[-1]+=1
        else:
            for i in range(len(digits)-1,-1,-1):
                if digits[i]==9:
                    digits[i]=0
                elif digits[i]!=9:
                    digits[i]+=1
                    return digits
        if digits[0]==0:
            digits.insert(0,1)
        return digits

        