class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums = sorted(nums)
        min_difference = float('inf')
        result = 0
        
        for i in range(len(nums)-2):
            j = len(nums)-1
            k = i+1

            while(k<j):

                summation = nums[i]+nums[k]+nums[j]

                if summation == target:
                    return target

                if summation > target:
                    j-=1
                
                else:
                    k+=1
                
                diference = abs(target - summation)

                if diference < min_difference:
                
                    min_difference = diference
                    result = summation

                    

        return result
            