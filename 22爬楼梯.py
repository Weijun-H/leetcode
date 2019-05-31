class Solution(object):
    def __index__(self):
        self.map = None

    def climbStairs1(self, n): # 斐波那契数列
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        num1 = 1
        num2 = 2
        numN = 0
        for i in range(3,n+1):
            numN = num1 + num2
            num1 , num2 = num2 , numN
        return numN

    def climbStairs2(self, n):  # 动态规划
        if n <= 2:
            return n
        self.map = [0] * (n+1)
        self.map[1] = 1
        self.map[2] = 2
        for i in range(3,n+1):
            self.map[i] = self.map[i-1] + self.map[i-2]
        return self.map[-1]


if __name__ == '__main__':
    s = Solution()
    answer = Solution.climbStairs(10)
    print()