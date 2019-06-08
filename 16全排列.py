class Solution:
    def permute(self, nums) :
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,1]))