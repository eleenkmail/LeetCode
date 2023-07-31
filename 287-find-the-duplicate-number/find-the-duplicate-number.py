class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        slow, fast = nums[0], nums[nums[0]]

        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]


        start = 0

        while start != slow:
            start = nums[start]
            slow = nums[slow]


        return slow