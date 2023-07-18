class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        counts = {}
        window, max_freq = 0, 0

        for i in range(len(s)):
            
            counts[s[i]] = counts.get(s[i], 0) + 1
            max_freq = max(max_freq, counts[s[i]])

            if max_freq + k > window:
                window += 1
            
            else:
                counts[s[i - window]] -= 1

        return window
        
