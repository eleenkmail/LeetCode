class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        index_s = 0
        iteration_s = len(s)

        index_t = 0
        iteration_t = len(t)

        while index_s < iteration_s:
            
            if index_s == 0 and s[index_s] == "#": 
                s = s[1:]
                iteration_s-=1
                continue

            if s[index_s] == "#":
                s = s[:index_s-1]+s[index_s+1:]
                index_s-=2
                iteration_s-=2
                
            index_s +=1 


        while index_t < iteration_t:
        
            if index_t == 0 and t[index_t] == "#": 
                t = t[1:]
                iteration_t-=1
                continue

            if t[index_t] == "#":
                
                t = t[:index_t-1]+t[index_t+1:]
                index_t-=2
                iteration_t-=2
                
            index_t +=1 


        if s == t:
            return True
        else: 
            return False