class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = {}
        seen[n] = 1
        
        while(True):
            summ = 0
            while n != 0:
                summ += (n%10)**2
                n = n/10

            n = summ


            if n == 1:
                return True

            if seen.get(n, 0) + 1 > 1:
                return False

            seen[n] = seen.get(n, 0) + 1


        