import itertools
class Solution(object):
    def maxSubArray(self, nums):    # 暴力解法
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        l = len(nums)
        for i in range(1,l+1):
            for j in range(l-i+1):
                print('j = {}'.format(j))
                res.append(list(nums[j:j+i]))
                print('res = {}'.format(res))
        return max(map(sum,res))

    def maxSubArray2(self, nums: List[int]) -> int:     #动态规划
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            res = max(dp[i], res)
        return res
if __name__ == '__main__':
    s = Solution()
    answer = s.maxSubArray([1,2,3])
    print(answer)