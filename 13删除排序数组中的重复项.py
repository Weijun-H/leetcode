class Solution:
    def removeDuplicates(self, nums):
        fast = 0
        slow = 0
        n = len(nums)
        while fast < n :
            while nums[fast] == nums[fast+1] and fast < n - 1:
                fast += 1
                # print(fast)

            nums[slow] = nums[fast]
            slow += 1
            fast += 1
        return slow


if __name__ == '__main__':
    s = Solution()
    answer = s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    print(answer)
