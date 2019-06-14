class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums1 = set(nums)
        if len(nums) != len(nums1):
            return True
        return False