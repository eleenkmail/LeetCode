class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
 
        nums = sorted(nums)
        result = []

       
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):

                l = j+1
                r = len(nums)-1


                while(l<r):

                    summation = nums[i]+nums[j]+nums[l]+nums[r]
                    if summation < target:
                        l+=1

                    elif summation > target:
                        r-=1

                    else:
                        correct = [nums[i],nums[l],nums[r],nums[j]]
                        l+=1
                        r-=1

                        
                        if correct not in result:
                            result.append(correct)

                        else:
                            continue
                    
            
        return result