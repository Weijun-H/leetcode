class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = []
        # print(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:    # 去重
                continue
            left = i + 1
            right = n - 1
            while left < right:     # 左指针小于右指针
                cur_sum = nums[i] + nums[left] + nums[right]    #三数之和是否为0
                if cur_sum == 0:
                    tmp = [nums[i], nums[left], nums[right]]
                    res.append(tmp)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    left += 1
        return res


if __name__ == '__main__':
    s = Solution()
    answer = s.threeSum([-1, 0, 1, 2, -1, -4])
    print(answer)
