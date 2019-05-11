'''
my solution
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_num = len(nums1)+len(nums2)
        odd = True
        if len_num % 2 == 0 :
            median_len = len_num/2
            odd = False
        else:
            median_len = (len_num+1)/2
        print(median_len)
        if nums1 != [] and nums2 != []:
            nums = sorted(nums1+nums2)
            if odd:
                return nums[median_len-1]
            else:
                return (nums[median_len-1]+nums[median_len])/2.0
        else:
            if nums1 == []:
                if odd:
                    return nums2[median_len-1]
                else:
                    return (nums2[median_len-1]+nums2[median_len])/2.0
            else:
                if odd:
                    return nums1[median_len-1]
                else:
                    return (nums1[median_len-1]+nums1[median_len])/2.0
