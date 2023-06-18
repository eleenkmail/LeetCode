class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        k_beauty = 0
        number_as_str = str(num)
        for index in range(len(number_as_str)-k+1):
            divisor = number_as_str[index:index+k]
            if divisor == "0" * len(divisor):
                continue
            
            elif (num % int(divisor))==0:
                k_beauty+=1
        
        return k_beauty
            
            
