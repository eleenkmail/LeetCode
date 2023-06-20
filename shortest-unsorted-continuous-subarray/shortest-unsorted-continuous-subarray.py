class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

      
        i = 0
        j = len(nums) - 1
   
    
        while (i < j) and (nums[i] <= nums[i+1] or nums[j] >= nums[j-1]):
            if nums[i] <= nums[i+1]:
                i += 1
            
            if nums[j] >= nums[j-1]:
                j -= 1
        
        
        if i == j:
            return 0

        
        for index in range(i, j+1):
            while i-1 >= 0 and nums[index] < nums[i-1]:
                i -= 1
            
            while j+1 < len(nums) and nums[index] > nums[j+1]:
                j += 1
        
        
        return j - i + 1
                