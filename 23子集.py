class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:  # 库函数
        res = []
        for i in range(len(nums) + 1):
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
        return res

    def subsets2(self, nums: List[int]) -> List[List[int]]:  # 回溯算法
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])
        return res