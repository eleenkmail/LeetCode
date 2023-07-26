class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = {}
        seen[n] = 1
        summ = 0
        
        while(True):

            summ += (n%10)**2
            n = n/10

            if n == 0:
                n = summ
                summ = 0
                if n == 1:
                    return True

                if seen.get(n, 0) + 1 > 1:
                    return False

                seen[n] = seen.get(n, 0) + 1



            

            

            


        