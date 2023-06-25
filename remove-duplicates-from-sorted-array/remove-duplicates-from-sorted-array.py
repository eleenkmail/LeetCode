class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = j = 0 
       
        while j<len(nums):
            if nums[i] == nums[j]:
                j+=1
            else:
                i+=1
                nums[i] = nums[j]

        return i+1
                
                       

       
        
