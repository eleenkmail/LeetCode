class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0 
        j = i+1

        nums_set = set(nums)
        nums[:len(nums_set)-1] = sorted(list(nums_set))

        return len(nums_set)