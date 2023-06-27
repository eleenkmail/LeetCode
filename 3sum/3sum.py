class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        i = 0 
       
        result = []
        for i in range(len(nums)):
            j = len(nums)-1
            k = i+1

            while(k<j):
                if nums[i]+nums[k]+nums[j] < 0:
                    k+=1

                elif nums[i]+nums[k]+nums[j] > 0:
                    j-=1
                else:
                    correct = [nums[i],nums[k],nums[j]]
                    j-=1
                    k+=1
                    if correct not in result:
                        result.append(correct)
                    else:
                        continue
                    
            
        return result


    