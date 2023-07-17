class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        

        indexes = {}
        longest = 0
        offset = 0

        for i in range(len(s)):

            if s[i] in indexes and indexes[s[i]] >= offset:

                
                offset = indexes[s[i]] + 1
                
                
            else:
                longest = max(longest, i - offset + 1)

            indexes[s[i]] = i
            

        if len(s) == 1:
            return 1

        return longest