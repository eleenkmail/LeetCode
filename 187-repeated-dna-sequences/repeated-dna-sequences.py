class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        seen = {}
        res = []

        for i in range(len(s)-9):

            seen[s[i:i+10]] = seen.get(s[i:i+10], 0) + 1

            if seen[s[i:i+10]] == 2:

                res.append(s[i:i+10])


        return res


        
