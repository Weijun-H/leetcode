class Solution(object):
    def majorityElement(self, nums):    # 列表
        """
        :type nums: List[int]
        :rtype: int
        """
        res = {}
        for i in nums:
            if i not in res.keys():
                res.setdefault(i,1)
            else:
                res[i] += 1
        print(res)
        return max(res.items(),key = lambda x:x[1])[0]

    def majorityElement(self, nums):    # 摩尔投票
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        major = nums[0]
        for i in nums[1:]:
            if i == major:
                count += 1
                continue
            else:
                count -= 1
                if count <= -1:
                    count = 1
                    major = i

        return major