class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        Sum = 0
        Len = float('inf')
        
        for r in range(len(nums)):
			
            Sum += nums[r]
            
            while Sum >= target and l <= r:
                
                Len = min(Len, (r - l)+1)
				
                if Len == 1:
                    return 1
				
                Sum -= nums[l]
                l += 1

        if Len != float('inf'):
            return Len
        else:
            return 0


        

