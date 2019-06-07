class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return nums[0]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or i == len(nums)-1:
                if nums[0] != nums[1]:
                    return nums[0]
                elif nums[len(nums)-1] != nums[len(nums)-2]:
                    return nums[len(nums)-1]
            elif nums[i-1] != nums[i] and nums[i] != nums[i+1]:
                return nums[i]