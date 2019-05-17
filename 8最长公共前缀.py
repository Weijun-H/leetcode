class Solution:
    def longestCommonPrefix1(self, strs) :#利用python特性 直接比较各个位置的字母
        res = ""
        for tmp in zip(*strs): #['abc','a','abc'] -> ('a'.'a','a')
            print(tmp)
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res

    def longestCommonPrefix2(self, s: List[str]) -> str:#直接遍历
        if not s:
            return ""
        res = s[0]
        i = 1
        while i < len(s):
            while s[i].find(res) != 0:
                res = res[0:len(res)-1]
            i += 1
        return res
if __name__ == '__main__':
    solution = Solution()
    strs =  ["flower","fooooooo","flight"]
    solution.longestCommonPrefix(strs)