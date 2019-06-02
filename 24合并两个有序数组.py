class Solution:
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:   # 插入排序
        while(n):
            if m and nums1[m-1]>nums2[n-1]:
                nums1[m+n-1],m=nums1[m-1],m-1
            else:
                nums1[m+n-1],n=nums2[n-1],n-1

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:   # 先插入后排序
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i+m] = nums2[i]
        nums1.sort()