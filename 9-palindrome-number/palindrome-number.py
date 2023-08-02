class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x = str(x)
        mid = len(x) // 2


        if len(x) == 1:
            return True
            
        if len(x) % 2:
            if x[:mid] == x[:mid:-1]:
                return True
        else: 
            if x[:mid] == x[:mid-1:-1]:
                return True

        return False