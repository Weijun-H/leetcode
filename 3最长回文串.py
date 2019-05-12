class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        max_len = 0
        res = ""
        for i in range(n):
            for j in range(i,-1,-1):
                if s[i] == s[j] and (i-j<=1 or dp[i-1][j+1]):
                    dp[i][j] = 1
                if max_len < i-j+1 and dp[i][j]:
                    max_len = i-j+1
                    res = s[j:i+1]
        return res