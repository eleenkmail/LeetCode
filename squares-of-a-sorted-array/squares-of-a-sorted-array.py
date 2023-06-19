class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        i = 0
        j = len(nums)-1

        while(i<=j):
            if i==j:
                nums[i]**=2
            else:
                nums[i]**=2
                nums[j]**=2

            i+=1
            j-=1
        return sorted(nums)