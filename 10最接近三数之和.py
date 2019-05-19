class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:     # 使用双指针
        nums.sort()
        length = len(nums)
        cur_tar = nums[0] + nums[1] + nums[2]
        res = [nums[0], nums[1], nums[2]]
        if length > 3:
            for i in range(length-2):
                l = i+1
                r = length - 1
                while ( l < r ) :
                    temp_tar = nums[i] + nums[l] + nums[r]
                    if abs(target-cur_tar) > abs(target-temp_tar):
                        cur_tar = temp_tar
                    if cur_tar == target:
                        return target
                    if target-temp_tar > 0:
                        l += 1
                    elif target-temp_tar < 0 :
                        r -= 1
        return cur_tar



if __name__ == '__main__':
    s = Solution()
    answer = s.threeSumClosest([-1,2,1,-4],1)
    print(answer)
